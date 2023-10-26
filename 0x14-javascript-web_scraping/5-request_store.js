#!/usr/bin/node

const req = require('request');
const f = require('fs');
const url = process.argv[2];

const filename = process.argv[3];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    f.writeFile(filename, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
