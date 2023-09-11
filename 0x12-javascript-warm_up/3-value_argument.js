#!/usr/bin/env node
import { argv } from 'node:process'
const arg = process.argv[2];

if (arg !== undefined) {
    console.log(arg);
} else {
    console.log("No argument");
}