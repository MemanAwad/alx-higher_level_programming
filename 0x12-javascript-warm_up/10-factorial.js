#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const myNum = parseInt(process.argv[2], 10);
console.log(factorial(myNum));