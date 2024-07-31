#!/usr/bin/node

const request = require('request');
const urlBase = 'https://swapi-api.alx-tools.com/api/films/';
const uId = process.argv[2];
const urlCode = urlBase + uId;

request(urlCode, function (err, response, body) {
  if (err) throw err;
  const data = JSON.parse(body);
  console.log(data.title);
});
