#!/usr/bin/node
const len = process.argv[2];
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
}
