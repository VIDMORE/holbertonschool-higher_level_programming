#!/usr/bin/node
function factorial (a) {
  const number = parseInt(a);
  if (a === 0 || isNaN(number)) {
    return 1;
  }
  return a * factorial(number - 1);
}
console.log(factorial(process.argv[2]));
