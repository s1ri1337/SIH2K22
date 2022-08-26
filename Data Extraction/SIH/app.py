import tweepy
import sqlite3
import time
import pandas as pd
import streamlit as st
from streamlit_tags import st_tags
from st_aggrid import AgGrid
import traceback
import base64
import re

def get_csv_download_link(csv, filename):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """

    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download CSV</a>'
    return href

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

def main():
    try:
        st.title("Twitter Streaming")
        with st.form(key='scraper_form'):
            keywords = st_tags(label='### Enter Keywords:',
                                text='Press enter to add more',
                                maxtags = -1,
                                key='1')
            #taglist = " #".join(keywords)
            n = st.slider('Stream Time (in seconds):', 0, 600, step=30)
            output_csv = st.radio('Save a CSV file?', ['Yes', 'No'])
            file_name = st.text_input('Name the CSV file:')
            submit_button = st.form_submit_button(label='Stream')

            if submit_button:

                conn = sqlite3.connect("tweet_collection.db")
                conn.create_function("REGEXP", 2, regexp)
                c = conn.cursor()
                create_table = 'CREATE TABLE Tweets ('
                create_table += 'num INTEGER PRIMARY KEY AUTOINCREMENT, '
                create_table += 'Timestamp DATETIME, '
                create_table += 'Username VARCHAR(30), '
                create_table += 'Tweet VARCHAR(280), '
                create_table += 'Location TEXT, '
                create_table += 'Hashtags VARCHAR(1000), '
                create_table += 'Media VARCHAR(1000) '
                create_table += ')'

                c.execute('DROP table IF EXISTS Tweets;')
                c.execute(create_table)

                # Authenticate to Twitter
                auth = tweepy.OAuthHandler("MUVqEWqOkXFQozG9wB1Uw7ro0", "oujuq1NFeXuEMATdXdITk8rj41DzZyxrGbxYfnFvnb12395Dgj")
                auth.set_access_token("1461918883086962690-dG1vOx77k8aHqApTyUpgWlw4WGo9r3", "NcMPcu65NJfr6CdTDaM8WgT7c8C4Nj5ool3nNHTdTxnFL")

                class MyStreamListener(tweepy.StreamListener):
                    def __init__(self, api, time_limit=n):
                        self.start_time = time.time()
                        self.limit = time_limit
                        self.api = api
                        self.me = api.me()
                        super(MyStreamListener, self).__init__()

                    def on_status(self, status):
                        if (time.time() - self.start_time) < self.limit:
                            if not status.retweeted:
                                if hasattr(status, "extended_tweet"):
                                    tweet = status.extended_tweet["full_text"]
                                else:
                                    tweet = status.text
                                location = status.user.location
                                username = status.user.screen_name
                                created_at = status.created_at
                                media = []
                                hashtaglist = []
                                for url in status.entities['urls']:
                                    media.append(url['url'])
                                for hash in status.entities['hashtags']:
                                    hashtaglist.append(hash['text'])   
                                links = ", ".join(media)
                                hashtags = ", ".join(hashtaglist)
                            else:
                                created_at = username = tweet = location = hashtags = links = None  
                        else:
                            return False

                        c.execute('INSERT INTO Tweets (Timestamp, Username, Tweet, Location, Hashtags, Media) VALUES (?, ?, ?, ?, ?, ?)',
                                        (created_at, username, tweet, location, hashtags, links))
                        conn.commit()

                    def on_error(self, status):
                        print("Error detected")

                # Create API object
                api = tweepy.API(auth, wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True)

                tweets_listener = MyStreamListener(api)
                stream = tweepy.Stream(api.auth, tweets_listener)
                try:
                    stream.filter(track=keywords, languages=["en", "hi"])
                except AttributeError:
                    pass
                
                query = c.execute("SELECT * FROM Tweets WHERE Tweet NOT REGEXP '^RT'")
                cols = [column[0] for column in query.description]
                results_df = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
                AgGrid(results_df)

                if output_csv == 'Yes':
                    st.markdown(get_csv_download_link(results_df.to_csv(), file_name), unsafe_allow_html=True)
       
    except:
        st.error("An error occurred.")
        st.error(traceback.format_exc())

if __name__ == '__main__':
    main()