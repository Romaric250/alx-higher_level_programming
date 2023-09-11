#!/usr/bin/node
import {argv} from 'node:process';
const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
  const x = parseInt(arg);
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
