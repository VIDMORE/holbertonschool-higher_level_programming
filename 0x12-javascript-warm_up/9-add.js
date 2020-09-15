#!/usr/bin/node
const add = (a, b) => parseInt(a) + parseInt(b);
console.log(add(process.argv[2], process.argv[3]));
