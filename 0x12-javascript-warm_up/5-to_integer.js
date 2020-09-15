#!/usr/bin/node
const val = process.argv[2]
if (isNaN(val)) {
	console.log('Not a number')
} else {
  console.log(`My number: ${parseInt(val)}`)
}
