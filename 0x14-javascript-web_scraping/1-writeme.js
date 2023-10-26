#!/usr/bin/node

const f = require('fs');

const filename = process.argv[2];
const content = process.argv[3];

f.writeFile(filename, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
