import botometer
import json

rapidapi_key = "abc" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': 'abc',
    'consumer_secret': 'abc'
    }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

def check_bot(acc):
    for key, value in bom.check_account(acc)['raw_scores']['universal'].items():
        print(key, value)
