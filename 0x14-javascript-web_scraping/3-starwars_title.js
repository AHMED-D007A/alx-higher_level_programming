#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(url, (err, res, body) => {
  if (err) console.log(err);
  const jsObj = JSON.parse(body);
  console.log(jsObj.title);
});
