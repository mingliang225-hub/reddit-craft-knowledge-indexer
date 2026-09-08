import os
import time
import praw

# Fully compliant User-Agent using your Reddit account
USER_AGENT = "desktop:CraftKnowledgeIndexer:v1.0 (by /u/Willing_Row_9848)"

def get_reddit_instance():
    """
    Initialize Reddit API client via OAuth with read-only permissions.
    """
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=USER_AGENT
    )

def fetch_community_troubleshooting_topics(subreddit_name="Leathercraft", limit=50):
    """
    Read-only retrieval of public posts to identify recurring troubleshooting topics.
    Author identities and personal metadata are discarded to respect privacy.
    """
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)
    
    records = []
    for submission in subreddit.hot(limit=limit):
        # Exclude usernames and profiling data
        records.append({
            "id": submission.id,
            "title": submission.title,
            "score": submission.score,
            "created_utc": submission.created_utc,
            "permalink": submission.permalink
        })
        time.sleep(1)  # Throttled request pacing to stay well under API rate limits
        
    return records

if __name__ == "__main__":
    print("Community knowledge indexing pipeline initialized in read-only mode.")
