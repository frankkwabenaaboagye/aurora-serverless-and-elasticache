import redis

# Redis connection details
redis_host = "frankleaderboard.bisby0.ng.0001.use1.cache.amazonaws.com"  # Your Redis endpoint
redis_port = 6379  # Redis default port

# Connect to Redis
try:
    print("Attempting to connect to Redis...")
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
    if redis_client.ping():
        print("Successfully connected to Redis.")
except Exception as e:
    print("Unable to connect to Redis:", e)
    exit()

# Function to fetch and display leaderboard data
def fetch_leaderboard():
    print("Fetching leaderboard data from Redis...")

    # Retrieve data from the sorted set, sorted by score in descending order
    leaderboard = redis_client.zrevrange('Overall Leaderboard', 0, -1, withscores=True)

    if not leaderboard:
        print("Leaderboard is empty.")
        return

    print("\n--- Leaderboard (Highest to Lowest) ---")
    for rank, (username, score) in enumerate(leaderboard, start=1):
        print(f"Rank {rank}: {username.split('|')[0]} - Score: {int(score)}")

# Call the function to fetch leaderboard data
fetch_leaderboard()

# Closing Redis connection
print("Closing Redis connection...")
redis_client.close()
print("Connection closed successfully.")
