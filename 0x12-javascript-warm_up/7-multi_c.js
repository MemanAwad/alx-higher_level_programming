#!/usr/bin/node
const myVar = process.argv[2];
const myVar2 = parseInt(myVar);
if (!isNaN(myVar2)) {
  for (let i = 0; i < myVar2; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
