# Build a Real-Time Leaderboard with Amazon Aurora Serverless and Amazon ElastiCache
This project implements a real-time leaderboard using Amazon Aurora Serverless and Amazon ElastiCache. 
The implementation follows the tutorial provided by AWS.

# Tutorial Reference
I used the following AWS tutorial as a guide for this project:
[https://aws.amazon.com/tutorials/real-time-leaderboard-amazon-aurora-serverless-elasticache/](https://aws.amazon.com/tutorials/real-time-leaderboard-amazon-aurora-serverless-elasticache/)


## Data

```bash

node scripts/testDatabase.js

node scripts/fetchHighScoresForUser.js


node scripts/fetchHighScoresForUser2.js


node scripts/testRedis.js

node scripts/loadRedis.js

```

---


``` bash

# This script runs the ZREVRANGE command to fetch the top five scores from the overall leaderboard.
node scripts/getTopOverallScores.js

``

```bash

# Authentication

curl -X GET ${BASE_URL}/users/ubecker


# register  a new user

curl -X POST ${BASE_URL}/users \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "spencer",
	"password": "Mypassword1",
	"email": "spencer@gmail.com"
}'


# login-fetch credential

curl -X POST ${BASE_URL}/login \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "spencer",
	"password": "Mypassword1"
}'



export ID_TOKEN=


#add user score

curl -X POST ${BASE_URL}/users/spencer \
 -H 'Content-Type: application/json' \
  -H "Authorization: ${ID_TOKEN}" \
  -d '{
	"level": 37,
	"score": 6541
}'


curl -X GET ${BASE_URL}/users/ubecker



# fetch top score
curl -X GET ${BASE_URL}/users/spencer


curl -X GET ${BASE_URL}/scores/2019-11-08

```






