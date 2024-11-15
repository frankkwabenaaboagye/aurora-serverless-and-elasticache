// Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
const AWS = require('aws-sdk')

const rdsdataservice = new AWS.RDSDataService();

const params = {
  resourceArn: "arn:aws:rds:us-east-1:740352710963:cluster:frankleaderboard",
  secretArn: "arn:aws:secretsmanager:us-east-1:740352710963:secret:leaderboard-database-LT500w",
  database: 'frankleaderboard',
  sql: 'SELECT 1'
}

rdsdataservice.executeStatement(params, function(err, data) {
  if (err) {
    console.log(err, err.stack)
  } else {
    console.log(JSON.stringify(data, null, 2))
  }
})
