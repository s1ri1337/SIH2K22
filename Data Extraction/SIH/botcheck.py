import botometer
import json

rapidapi_key = "4c6dc379fbmsh35a272cc401c728p1a5a84jsn6d453d48d7e8" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': 'MUVqEWqOkXFQozG9wB1Uw7ro0',
    'consumer_secret': 'oujuq1NFeXuEMATdXdITk8rj41DzZyxrGbxYfnFvnb12395Dgj'
    }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

def check_bot(acc):
    for key, value in bom.check_account(acc)['raw_scores']['universal'].items():
        print(key, value)
