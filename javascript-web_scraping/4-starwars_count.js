#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const wedgeId = 18;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  const films = data.results;

  const count = films.filter((film) => film.characters.some(
    (character) => character.endsWith(`/${wedgeId}/`)
  )).length;

  console.log(count);
});
