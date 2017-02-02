import tweepy

from textblob import TextBlob



# Step 1 - Authenticate

consumer_key= 'vgutZ5MhVexdYgFrdFsMEiqXO'

consumer_secret= 'h6rOF6Y3idoX51G3nfIq4zKnW6zYpauTJxPeglPpf4mrJgi0fG'



access_token='826478757795868672-N2SNXdsfYsYnnXgHMroOJG8ZHkPGlCA'

access_token_secret='zRGOlb56I5oZsQTEOxS7dltRilrO8iUEjDe6tMLbnXP0a'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)



api = tweepy.API(auth)



#Step 3 - Retrieve Tweets

public_tweets = api.search('Food')







#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file

#and label each one as either 'positive' or 'negative', depending on the sentiment 

#You can decide the sentiment polarity threshold yourself





for tweet in public_tweets:

    print(tweet.text)

    

    #Step 4 Perform Sentiment Analysis on Tweets

    analysis = TextBlob(tweet.text)

    print(analysis.sentiment)

    print("")