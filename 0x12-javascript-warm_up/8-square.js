#!/usr/bin/node
const len = process.argv[2];
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < len; i++) {
    console.log('X'.repeat(len));
  }
}
