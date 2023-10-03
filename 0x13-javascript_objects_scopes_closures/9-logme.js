#!/usr/bin/node

let counts = 0;

exports.logMe = function count (item) {
  console.log(`${counts}: ${item}`);
  counts += 1;
};
