#!/usr/bin/node
import { argv } from 'node:process';
const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
    console.log(`My number: ${parseInt(arg)}`);
} else {
    console.log("Not a number");
}