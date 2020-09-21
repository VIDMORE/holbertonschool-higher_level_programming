#!/usr/bin/node
var counter = 0;
exports.logMe = (item) => { console.log(`${counter}: ${item}`); counter++; };
