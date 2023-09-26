#!/usr/bin/node
const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (err, res, body) {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (cErr, cRes, cBody) {
      if (cErr) console.log(cErr);
      console.log(JSON.parse(cBody).name);
    });
  }
});
