#!/usr/bin/node
const [,, firstArg] = process.argv;
const number = parseInt(firstArg);
if (!isNaN(number)) {
 console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
