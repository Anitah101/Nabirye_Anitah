import tweepy
import datetime
import os
import socket
import time

# Step 1: Wait for internet connection (try for up to 2 minutes)
def is_connected():
    try:
        socket.create_connection(("api.twitter.com", 443), timeout=5)
        return True
    except OSError:
        return False

for _ in range(120):  # wait max 2 mins (120 seconds)
    if is_connected():
        break
    time.sleep(1)
else:
    print("❌ Internet not available. Tweet not sent.")
    exit()

# Step 2: Check if already posted today
today = datetime.datetime.now().strftime("%Y-%m-%d")
weekday = datetime.datetime.now().strftime("%A")

log_file = "last_posted.txt"
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        last_date = f.read().strip()
    if last_date == today:
        print("✅ Already posted today. Skipping.")
        exit()

# Step 3: Tweet today's quote
quotes = {
    "Monday": "Start strong. The rest of the week will thank you.",
    "Tuesday": "Great things never come from comfort zones.",
    "Wednesday": "Keep going — you're halfway to your goals.",
    "Thursday": "Discipline is doing what needs to be done, even when you don't feel like it.",
    "Friday": "Your future is created by what you do today, not tomorrow.",
    "Saturday": "Invest in rest. Recharge to rise again.",
    "Sunday": "A new week is a new chance to grow. Reflect and reset."
}

quote = quotes.get(weekday, "Stay inspired.")

# Twitter credentials
API_KEY = 'wHqBFJJ4iWRUz4dLlHgwCJEsj'
API_SECRET_KEY = '1YolTZz6rGqZhVRoDcnFSL1QmBxc3wCtupQ4Roju0oCnniD79Q'
ACCESS_TOKEN = '1942584488128581633-HeCxJgMtYxS1TtKPjlVyo85qyE9y82'
ACCESS_TOKEN_SECRET = 'q0ePstBU7ASy4U7qyxxsX5CTdwbAbPsHeKyOl064yXDJu'


# Step 4: Post the tweet
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

try:
    response = client.create_tweet(text=quote)
    print(f"✅ Posted: {quote}")
    with open(log_file, "w") as f:
        f.write(today)
except Exception as e:
    print(f"❌ Failed to post tweet: {e}")
