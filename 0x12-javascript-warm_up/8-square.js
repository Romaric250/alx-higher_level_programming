#!/usr/bin/env node
import {argv} from 'node:process';
const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
  const size = parseInt(arg);

  if (size <= 0) {
    console.log("Missing size");
  } else {
    const row = "X".repeat(size);
    for (let i = 0; i < size; i++) {
      console.log(row);
    }
  }
} else {
  console.log("Missing size");
}
