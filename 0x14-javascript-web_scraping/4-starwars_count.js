#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const char_Id = '18';
let counter = 0;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(char_Id)) {
          counter += 1;
        }
      });
    });
    console.log(counter);
  }
});
