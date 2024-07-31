#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

// Initialize the userCompletedCount object
const userCompletedCount = {};

request(url, function (err, response, body) {
  if (err) throw err;

  const data = JSON.parse(body);

  // Iterate over each task
  data.forEach(task => {
    if (task.completed) {
      if (userCompletedCount[task.userId]) {
        userCompletedCount[task.userId] += 1;
      } else {
        userCompletedCount[task.userId] = 1;
      }
    }
  });

  // Output the result
  console.log(userCompletedCount);
});
