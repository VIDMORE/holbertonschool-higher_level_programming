#!/usr/bin/node
const val = process.argv[2];
if (isNaN(val)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < val; i++) {
    console.log('C is fun');
  }
}