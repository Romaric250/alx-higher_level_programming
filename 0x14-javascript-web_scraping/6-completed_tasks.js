#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const complete = {};
  body.forEach((todotask) => {
    if (todotask.completed) {
      if (!complete[todotask.userId]) {
        complete[todotask.userId] = 1;
      } else {
        complete[todotask.userId] += 1;
      }
    }
  });

  console.log(complete);
});
