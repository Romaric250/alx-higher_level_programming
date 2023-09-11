#!/usr/bin/node
import {argv} from 'node:process';
function add(a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (Number.isNaN(arg1) || Number.isNaN(arg2)) {
  console.log("NaN");
} else {
  console.log(add(arg1, arg2));
}
