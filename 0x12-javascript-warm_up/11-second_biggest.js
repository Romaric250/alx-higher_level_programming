#!/usr/bin/node
import {argv} from "node:process";
function findSecondBiggest(args) {
  const integers = args.map(arg => parseInt(arg));
  const sortedIntegers = integers.sort((a, b) => b - a);
  return sortedIntegers[1] || 0;
}

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(findSecondBiggest(args));
}
