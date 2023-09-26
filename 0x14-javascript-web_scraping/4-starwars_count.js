#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let cownter = 0;

request(url, (err, res, body) => {
  if (err) console.log(err);
  body = JSON.parse(body).results;
  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];
      if (characterId === '18') cownter += 1;
    }
  }
  console.log(cownter);
});
