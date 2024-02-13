#!/usr/bin/node
const myVar1 = process.argv[2];
const myVar2 = parseInt(myVar1);
const myVar3 = process.argv[3];
const myVar4 = parseInt(myVar3);

if ((!isNaN(myVar2)) && (!isNaN(myVar4))) {
  console.log(myVar2 + myVar4);
} else {
  console.log('NaN');
}
