import json
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

tweets = []
filename = 'twitter-2019-05-01/tweet.js'

with open(filename, 'r') as f:
        datastore = json.load(f)

for tweet in datastore:
    
    retweet = 'RT @' in tweet['full_text']

# find out if there was any additional media (this is almost always a picture, but it could be something else)
    if 'media' in tweet['entities']:
        picture = True
    else:
        picture = False

    date_time_obj = dt.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')

    tweets.append([tweet['full_text'], date_time_obj, retweet, picture])

df = pd.DataFrame(tweets)
df.columns = ['Tweet', 'Date', 'RT', 'Picture']
# Create a DataFrame with a date index for use in resampling. Keep original df for 
# group by analysis
dated_df = df.set_index('Date')

# Collect my own tweets for later analysis
true_tweets = df[~df['RT']]
true_tweets = true_tweets.set_index('Date')

# Collect retweets for examination
retweets = df[df['RT']]
retweets = retweets.set_index('Date')


# Examine use of retweets
in_order_retweets = retweets.resample('M').count()
total_tweets = dated_df.resample('M').count()

# Create a single dataframe with all the information in it so that I can use linear 
# regression to look at relationship between number of tweets and use of RT
summary = pd.DataFrame(columns = ['Tweets', 'Retweets', 'PercentRT'])

summary['Tweets'] = total_tweets.Tweet
summary['Retweets'] = in_order_retweets.Tweet

summary['PercentRT'] = summary.Retweets/summary.Tweets
summary = summary.fillna(0)

# How has my twitter use changed over time?

plt.figure()
plt.title('Confessions of a Confused Tweeter')

plt.plot(total_tweets)


# Is there an annual pattern to my use of twitter?

plt.figure()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_tweets = df.groupby(df['Date'].dt.strftime('%b'))['Tweet'].count().reindex(months)
# monthly_retweets = retweets.groupby(df['Date'].dt.strftime('%b'))['Tweet'].count().reindex(months)
plt.title('Tweets per month')
plt.gcf().text(0.30, 0.2, 'I go outside for most of the summer')

plt.plot(monthly_tweets)


#What days of the week do I tweet most?

plt.figure()
days = ['Mon','Tue','Wed','Thu','Fri','Sat', 'Sun']
per_days = df.groupby(df['Date'].dt.strftime('%a')).count().reindex(days)

plt.bar(per_days.index, per_days.Tweet)
plt.title('What days of the week do I tweet most?')

# How has my use of RT changed over time?
plt.figure()

plt.plot(summary.PercentRT)
plt.title('A Rising Tide of Retweets')


# I thought that perhaps I RT more at times that I am using twitter more?

plt.figure()

plt.title('Do I RT more when I tweet more?')
plt.scatter(summary.Tweets, summary.PercentRT)


plt.show()
