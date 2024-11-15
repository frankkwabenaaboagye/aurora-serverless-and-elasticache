import psycopg2
import redis

# PostgreSQL connection details
pg_host = "frankleaderboard.cluster-c12maesqmaic.us-east-1.rds.amazonaws.com"  # Your Aurora PostgreSQL endpoint
pg_dbname = "frankleaderboard"  # Your PostgreSQL database name
pg_user = "postgres"  # Your master username
pg_password = "password"  # Your password

# Connect to PostgreSQL
try:
    print("Attempting to connect to PostgreSQL...")
    conn = psycopg2.connect(
        host=pg_host,
        dbname=pg_dbname,
        user=pg_user,
        password=pg_password
    )
    cursor = conn.cursor()
    print("Successfully connected to PostgreSQL.")
except Exception as e:
    print("Unable to connect to PostgreSQL:", e)
    exit()

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

# Function to fetch leaderboard data from PostgreSQL and load it into Redis
def load_data_to_redis():
    print("Fetching data from PostgreSQL...")
    cursor.execute("SELECT username, score FROM leaderboard ORDER BY score DESC")
    rows = cursor.fetchall()

    print(f"Fetched {len(rows)} rows from PostgreSQL.")

    for row in rows:
        username = row[0]
        score = row[1]
        print(f"Processing: Username={username}, Score={score}")

        # Create a unique Redis key based on username
        key = f"{username}|leaderboard"

        # Add the score to the Redis overall leaderboard
        print(f"Adding to Overall Leaderboard: {key} with score {score}")
        redis_client.zadd('Overall Leaderboard', {key: score})

    print("All data loaded into Redis successfully!")

# Call the function to load data into Redis
load_data_to_redis()

# Closing Redis and PostgreSQL connections
print("Closing connections...")
cursor.close()
conn.close()
redis_client.close()
print("Connections closed successfully.")
