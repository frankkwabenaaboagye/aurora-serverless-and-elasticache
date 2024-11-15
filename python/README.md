# Real-Time Leaderboard

This project demonstrates a **real-time leaderboard** implementation using **PostgreSQL (Amazon Aurora)** and **Redis (Amazon ElastiCache)**. The application fetches data from PostgreSQL, processes it, and loads it into Redis for optimized real-time ranking and display.

## Key Features
1. **PostgreSQL (Amazon Aurora)**:
   - Used for persistent storage of leaderboard data.
   - Fetches sorted data based on scores.

2. **Redis (Amazon ElastiCache)**:
   - Used for in-memory caching and fast leaderboard updates.
   - Efficiently ranks and retrieves user scores.

3. **Integration**:
   - Python scripts utilizing `psycopg2` for PostgreSQL connections.
   - Redis client library for Python (`redis`) for interactions with Redis.

## How It Works
1. **Database Connection**:
   - Connects to an Amazon Aurora PostgreSQL database to retrieve leaderboard data.
   - Utilizes Python’s `boto3` for managing AWS credentials.

2. **Redis Caching**:
   - Connects to Amazon ElastiCache for Redis to store and update leaderboard data in real-time.

3. **Data Synchronization**:
   - Fetches scores from PostgreSQL and uploads them into Redis' sorted sets for real-time ranking.

## Acknowledgments
This implementation builds upon the knowledge gained from:
- [AWS Tutorials](https://aws.amazon.com/tutorials/)
- [AWS Samples](https://github.com/aws-samples) 

Feel free to explore, customize, and optimize the project!
