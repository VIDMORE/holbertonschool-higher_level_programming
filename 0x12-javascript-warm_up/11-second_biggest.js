#!/usr/bin/node
function secondBiggest (array) {
  if (array.length < 4) {
    return 0;
  }
  const data = array.sort();
  return data[data.length - 2];
}
console.log(secondBiggest(process.argv));
