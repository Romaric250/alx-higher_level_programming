#!/usr/bin/node
import {argv} from "node:process";
function factorial(n) {
  if (Number.isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);

console.log(factorial(arg));
