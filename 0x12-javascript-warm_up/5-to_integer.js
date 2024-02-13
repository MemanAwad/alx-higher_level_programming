#!/usr/bin/node
const myVar = process.argv[2];
const myVar2 = parseInt(myVar);
if (!isNaN(myVar2)) {
  console.log('My number:', myVar2);
} else {
  console.log('Not a number');
}
