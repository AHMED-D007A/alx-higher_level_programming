#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], (err, response) => {
  if (err) console.log(err);
  console.log('code:', response.statusCode);
});
