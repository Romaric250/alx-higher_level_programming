#!/usr/bin/node

const req = require('request');
const movie_Id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_Id}`;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
