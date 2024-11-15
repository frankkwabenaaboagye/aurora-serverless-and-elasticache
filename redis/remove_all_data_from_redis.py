import redis

# Redis connection details
redis_host = "frankleaderboard.bisby0.ng.0001.use1.cache.amazonaws.com"  # Your Redis endpoint
redis_port = 6379  # Redis default port

# Connect to Redis
try:
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
    print("Connected to Redis")
except Exception as e:
    print("Unable to connect to Redis", e)
    exit()

# Function to clear all data in the Redis database
def clear_redis_data():
    try:
        redis_client.flushdb()
        print("All data cleared from Redis successfully!")
    except Exception as e:
        print("Failed to clear data from Redis", e)

# Call the function to clear data
clear_redis_data()

# Close the Redis connection
redis_client.close()
