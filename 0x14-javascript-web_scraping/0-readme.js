#!/usr/bin/node
const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
