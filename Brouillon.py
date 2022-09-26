
import tweepy

auth = tweepy.OAuthHandler("CxCkNuSCmuelWNslaQhm9G7bq" , "gJMNhCM6GoBAeK086LELVSunbdfSo1a02yeR0ehmAKtA8pkUZT")
auth.set_access_token("1365307419291746313-i2bEAmjz6NPErFs3cVhyE1LG0KF7SO" , "KUCoEdshHZ7VUqKrY7S7FVUrFmjOPaD6uznOoHjzXQhMo")

api = tweepy.API(auth)

### Test De L'API ###

try : 
    api.verify_credentials()
    print("API : Connected")
except : 
    print("API : Not connected")

                                              ###### CONFIG PARAMETRES ######         

### Configuration du mot recherché ###
    
keyword = "Speed"
keyword_filterRT = keyword + " -filter:retweets"

max_tweets = 10

date_until = ""

result_type = "recent"

lang = ""

count = 100

geocode = ""



tweets = tweepy.Cursor(api.search_tweets, q = keyword_filterRT, count = count, tweet_mode = 'extended', lang = lang, geocode = geocode, result_type = result_type, until = date_until).items(max_tweets)

i = 0

for tweet in tweets:

    tweet_text = str(tweet.full_text)

    tweetId = tweet.id
    tweet_link = "https://twitter.com/i/web/status/" + str(tweetId)
    tweet_time = str(tweet.created_at).replace("+00:00", "")
    tweet_source = tweet.source
    tweet_user = str("@" + str(tweet.author.screen_name))
    i = i + 1
    print("Tweet " + str(i) + "\n" + tweet_text + "\n" + tweet_link + "\n" + tweet_user + "\n" + tweet_time + "\n" + tweet_source + "\n"  )
