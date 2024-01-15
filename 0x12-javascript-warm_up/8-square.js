#!/usr/bin/node
const [,, arg] = process.argv;
const size = parseInt(arg);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let squareLine = '';
    for (let j = 0; j < size; j++) {
      squareLine += 'X';
    }
    console.log(squareLine);
  }
}
