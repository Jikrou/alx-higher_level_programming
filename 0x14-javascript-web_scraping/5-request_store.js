#!/usr/bin/node

// first argument the url request
// todo: get the body and write it into a file
// second arg the path to body response

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const bdText = process.argv[3];

request.get(url, function (err, body) {
  if (err) throw err;
  const d = body.body;
  fs.writeFile(bdText, d, (err) => {
    if (err) throw err;
  });
});
