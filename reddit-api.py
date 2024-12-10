#!/usr/bin/env python

import praw
import pandas as pd
import sqlite3
import os
import sys
from datetime import datetime
from tqdm import tqdm

# Initialize PRAW with your credentials from environment variables
reddit = praw.Reddit(
    client_id=os.environ.get('REDDIT_CLIENT_ID'),
    client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
    user_agent=f"script:praw:{praw.__version__} (by u/{os.environ.get('REDDIT_USERNAME')})"
)

def extract_subreddit_data(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    data = []
    try:
        for submission in tqdm(subreddit.new(limit=limit), desc="Fetching submissions"):
            submission.comments.replace_more(limit=0)
            comments = [comment.body for comment in submission.comments.list()]
            data.append({
                'post_id': submission.id,
                'title': submission.title,
                'selftext': submission.selftext,
                'author': str(submission.author),
                'created_utc': submission.created_utc,
                'comments': comments
            })
    except Exception as e:
        print(f"An error occurred while extracting data from r/{subreddit_name}: {e}")
    return pd.DataFrame(data)

def save_data(df, base_filename):
    try:
        # Save to JSON
        json_filename = f"{base_filename}.json"
        df.to_json(json_filename, orient='records', lines=True)
        print(f"Data saved to {json_filename}")

        # Save to CSV
        csv_filename = f"{base_filename}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Data saved to {csv_filename}")

        # Save to SQLite
        db_filename = f"{base_filename}.db"
        conn = sqlite3.connect(db_filename)
        df[['post_id', 'title', 'selftext', 'author', 'created_utc']].to_sql('posts', conn, if_exists='replace', index=False)
        comments_data = df.explode('comments')[['post_id', 'comments']].rename(columns={'comments': 'comment'})
        comments_data.to_sql('comments', conn, if_exists='replace', index=False)
        conn.close()
        print(f"Data saved to {db_filename}")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a subreddit name.")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    base_filename = f"subreddit_{subreddit_name.lower()}_{datetime.now().strftime('%Y-%m-%d')}"

    data = extract_subreddit_data(subreddit_name, limit=100)
    save_data(data, base_filename)
