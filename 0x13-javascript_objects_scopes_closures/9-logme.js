#!/usr/bin/node
exports.logMe = (function () {
  let counter = 0;
  return (item) => { console.log(`${counter}: ${item}`); counter++; };
}());
