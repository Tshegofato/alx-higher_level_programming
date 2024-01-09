#!/usr/bin/node
function add(a, b) {
  return a + b;
}
const [,, arg1, arg2] = process.argv;
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);
if (isNaN(num1) || isNaN(num2)) {
  console.log('Invalid arguments. Please provide two integers.');
} else {
  const result = add(num1, num2);
  console.log('The addition of ${num1} and ${num2} is: ${result}');
}
