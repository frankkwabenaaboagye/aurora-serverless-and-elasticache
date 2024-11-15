import redis

# Redis connection details
redis_host = "frankleaderboard.bisby0.ng.0001.use1.cache.amazonaws.com"  # Your Redis endpoint
redis_port = 6379  # Redis default port

try:
    # Connect to Redis
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    # Test the connection by sending a ping
    response = redis_client.ping()
    
    # If ping response is True, the connection is successful
    if response:
        print("Successfully connected to Redis!")
    else:
        print("Failed to connect to Redis.")
except redis.ConnectionError as e:
    print(f"Error: Unable to connect to Redis. {e}")
