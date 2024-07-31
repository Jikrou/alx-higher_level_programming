#!/usr/bin/node

const request = require('request');
const urlBase = process.argv[2];
const urlCode = urlBase.replace('films', 'people/18');

request(urlCode, function (err, response, body) {
  if (err) throw err;
  const data = JSON.parse(body);
  const dataFil = data.films;
  console.log(dataFil.length);
});
