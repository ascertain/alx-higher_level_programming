#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((film) => {
      film.characters.forEach((character) => {
        const characterId = character.split('/')[5];

        if (characterId === '18') {
          count++;
        }
      });
    });
    console.log(count);
  }
});