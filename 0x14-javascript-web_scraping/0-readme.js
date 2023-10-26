#!/usr/bin/node

const f = require('fs');
const filename = process.argv[2];

f.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
