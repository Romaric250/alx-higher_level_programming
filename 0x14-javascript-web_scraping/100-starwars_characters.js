#!/usr/bin/node

const req = require('request');

const movie_Id = process.argv[2];
const url = `https://swapi.dev/api/films/${movie_Id}/`;

req.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  const chars = data.characters;
  for (const chars of chars) {
    req(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
