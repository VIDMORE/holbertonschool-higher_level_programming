#!/usr/bin/node
exports.logMe = ((item) => {
  var counter = 0;
  return (item) => { console.log(`${counter}: ${item}`); counter++; };
})();
