#!/usr/bin/node

const request = require('request');
const urlBase = process.argv[2];

request(urlBase, function (err, response, body) {
  if (err) throw err;
  const films = JSON.parse(body).results;
  const count = films.reduce((acc, film) => {
    return acc + (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/') ? 1 : 0);
  }, 0);
  console.log(count);
});
