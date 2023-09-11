#!/usr/bin/node
import {argv} from 'node:process';
let arg = process.argv[2];
if (Number.isInteger(Number(arg))) {
while (parseInt(arg) > 0){
	console.log('C is fun');
	arg = arg - 1;

}}
else {
    console.log("Missing number of occurences");
}
