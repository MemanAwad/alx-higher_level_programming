#!/usr/bin/node
let myVar = process.argv[2];
let myVar2 = parseInt(myVar);
if (!isNaN(myVar2))
{
	console.log('My number:', myVar2)
}
else
{
	console.log('Not a number')
}
