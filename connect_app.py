import socket
import sys
import requests
import requests_oauthlib
import json
import bleach
from bs4 import BeautifulSoup

# Include your Twitter account details
# generate from https://developer.twitter.com/en/portal/projects/1511458470851141650/apps/23900580/keys
ACCESS_TOKEN = '1507801587577720844-SD48FcPJ8C52oRvlNXOPK2BhFFdE2j'
ACCESS_SECRET = 'udTagU4GQ7OVgDbOvq2QQwWGx38eAQm0ocJCCf9Xybt0N'
CONSUMER_KEY = 'IJITN5uRduo3Ji5KsP4j0O3I9'
CONSUMER_SECRET = '52QMjOljnQ9cbU3fGLhqDspuLhC3Bw1fv7fCGpXQMnJ7vtPiwV'
my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)


def get_tweets():
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    query_data = [('language', 'en'), ('locations', '-130,-20,100,50'), ('track', 'iphone')]
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=my_auth, stream=True)
    print(query_url, response)
    return response


def send_tweets_to_spark(http_resp, tcp_connection):
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text']
            print("Tweet Text: " + tweet_text)
            print("------------------------------------------")
            tweet_screen_name = "SN:" + full_tweet['user']['screen_name']
            print("SCREEN NAME IS : " + tweet_screen_name)
            print("------------------------------------------")
            source = full_tweet['source']
            soup = BeautifulSoup(source)
            for anchor in soup.find_all('a'):
                print("Tweet Source: " + anchor.text)
            tweet_source = anchor.text
            source_device = tweet_source.replace(" ", "")
            device = "TS" + source_device.replace("Twitter", "")
            print("SOURCE IS : " + device)
            print("------------------------------------------")
            tweet_country_code = "CC" + full_tweet['place']['country_code']
            print("COUNTRY CODE IS : " + tweet_country_code)
            print("------------------------------------------")
            single_twit = str(tweet_text + ' ' + tweet_country_code + ' ' + tweet_screen_name + ' ' + device + '\n')
            tcp_connection.send(single_twit.encode())

        except:
            continue


TCP_IP = '127.0.0.1'
TCP_PORT = 8080
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print("Waiting for TCP connection...")
conn, addr = s.accept()

print("Connected... Starting getting tweets.")
resp = get_tweets()
send_tweets_to_spark(resp, conn)