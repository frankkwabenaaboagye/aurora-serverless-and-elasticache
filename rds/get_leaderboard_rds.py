import psycopg2
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Set up AWS CLI (boto3) to interact with AWS services
def get_aws_credentials():
    try:
        # Use boto3 to fetch credentials from the environment or IAM role
        session = boto3.Session()
        credentials = session.get_credentials()
        return credentials
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error fetching AWS credentials: {e}")
        return None

# Connect to Aurora PostgreSQL
def connect_to_postgres():
    # Fetch AWS credentials using boto3
    aws_credentials = get_aws_credentials()

    if aws_credentials is None:
        return None

    # Aurora PostgreSQL connection details
    host = "frankleaderboard.cluster-c12maesqmaic.us-east-1.rds.amazonaws.com"  # Your RDS Endpoint
    dbname = "frankleaderboard"  # Replace with your DB name
    user = "postgres"  # Master username
    password = "password"  # Replace with your password

    try:
        # Connect to Aurora PostgreSQL using psycopg2
        print("connecting to rds...")

        # Print the credentials and connection details
        print("Aurora PostgreSQL connection details:")
        print(f"Host (RDS Endpoint): {host}")
        print(f"Database Name: {dbname}")
        print(f"Username: {user}")
        print(f"Password: {password}")
        print("+++++++++++++++++++++++++++")

        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Fetch leaderboard data from PostgreSQL
def fetch_leaderboard_data():
    conn = connect_to_postgres()
    
    if conn is None:
        print("Could not connect to database.")
        return

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM leaderboard ORDER BY score DESC")
        leaderboard_data = cursor.fetchall()

        # Print the leaderboard data
        print("Leaderboard Data:")
        for row in leaderboard_data:
            print(f"Username: {row[0]}, Score: {row[1]}")

    except Exception as e:
        print(f"Error fetching data: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    fetch_leaderboard_data()
    print("+++++++++++++++++++++++++++")
