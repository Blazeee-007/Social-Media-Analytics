import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Authenticate with the Twitter API
def authenticate_twitter(api_key, api_secret, access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(consumer_key=api_key, consumer_secret=api_secret,
                                    access_token=access_token, access_token_secret=access_token_secret)
    api = tweepy.API(auth)
    return api

# Fetch tweets from a user's timeline
def get_user_tweets(api, username, count=100):
    tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
    tweet_data = []
    for tweet in tweets:
        tweet_data.append({
            'created_at': tweet.created_at,
            'text': tweet.full_text,
            'likes': tweet.favorite_count,
            'retweets': tweet.retweet_count,
            'mentions': len(tweet.entities['user_mentions']),
        })
    return pd.DataFrame(tweet_data)

# Visualize engagement metrics (Likes and Retweets)
def plot_engagement(df):
    plt.figure(figsize=(12, 6))
    sns.set(style="whitegrid")
    
    # Plot likes vs retweets
    sns.scatterplot(x='likes', y='retweets', data=df, color='blue', s=100, marker='o')
    
    plt.title('Likes vs Retweets', fontsize=16)
    plt.xlabel('Likes', fontsize=12)
    plt.ylabel('Retweets', fontsize=12)
    plt.show()

# Main function
if __name__ == "__main__":
    # Replace with your credentials
    API_KEY = 'your_api_key'
    API_SECRET_KEY = 'your_api_secret_key'
    ACCESS_TOKEN = 'your_access_token'
    ACCESS_TOKEN_SECRET = 'your_access_token_secret'
    
    # Authenticate and fetch data
    api = authenticate_twitter(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # Replace with the username you're interested in
    username = 'elonmusk'  
    tweets_df = get_user_tweets(api, username, count=100)
    
    # Print data sample
    print(tweets_df.head())
    
    # Plot engagement metrics
    plot_engagement(tweets_df)
