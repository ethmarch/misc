import tweepy
import json
from tweepy import OAuthHandler
import codecs


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# limit handler function from:
# http://docs.tweepy.org/en/v3.5.0/code_snippet.html
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def gettweets(handle, filename):
    file = codecs.open(filename, 'w', encoding='utf8')
    file.truncate()
    for status in limit_handled(tweepy.Cursor(api.user_timeline, screen_name=handle, include_rts=False).items(5000)):
        file.write(status.text)
        file.write("\r\n")
    file.close()

#gettweets('@realDonaldTrump','trumptweets2.txt')
gettweets('@HillaryClinton','clintontweets2.txt')
