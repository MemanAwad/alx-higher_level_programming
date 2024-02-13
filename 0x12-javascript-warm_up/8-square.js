#!/usr/bin/node
const myVar = process.argv[2];
const myVar2 = parseInt(myVar);
if (!isNaN(myVar2)) {
  for (let i = 0; i < myVar2; i++) {
    for (let j = 0; j < myVar2; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
