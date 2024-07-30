#!/usr/bin/node

const request = require('request');
const urlCode = process.argv[2];
request(urlCode, function (err, response) {
  if (err) throw err;
  console.log('code:', response.statusCode);
});
