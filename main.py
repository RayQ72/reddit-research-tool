import os
import praw
import pandas as pd
from datetime import datetime
import time

class RedditResearchTool:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        print(f"✅ Authenticated as: {self.reddit.user.me()}")

    def search_and_analyze(self, subreddit_name, query, limit=50):
        print(f"\n🔍 Searching r/{subreddit_name} for '{query}'...")
        
        posts_data = []
        subreddit = self.reddit.subreddit(subreddit_name)
        
        for submission in subreddit.search(query, limit=limit):
            text = submission.title + " " + submission.selftext
            positive_words = ['good', 'great', 'excellent', 'love', 'like', 'best']
            score = sum(1 for word in positive_words if word in text.lower())
            sentiment = 'Positive' if score > 0 else 'Neutral'
            
            posts_data.append({
                'title': submission.title,
                'url': submission.url,
                'score': submission.score,
                'comments': submission.num_comments,
                'created_utc': datetime.fromtimestamp(submission.created_utc),
                'sentiment_estimate': sentiment
            })
            time.sleep(1)

        df = pd.DataFrame(posts_data)
        filename = f"reddit_{subreddit_name}_{query}_{datetime.now().strftime('%Y%m%d')}.csv"
        df.to_csv(filename, index=False)
        print(f"📊 Saved {len(df)} posts to {filename}")
        return df

if __name__ == "__main__":
    CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "YOUR_CLIENT_ID")
    CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "YOUR_CLIENT_SECRET")
    USER_AGENT = "script:reddit-research-tool:v0.1 (by u/RayQ72)"

    tool = RedditResearchTool(CLIENT_ID, CLIENT_SECRET, USER_AGENT)
