#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(
  `https://swapi.dev/api/films/${movieId}/`,
  function (error, response, body) {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }

    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.reduce((prevPromise, characterUrl) => {
      return prevPromise.then(() => {
        return fetchAndPrintCharacterName(characterUrl);
      });
    }, Promise.resolve());
  }
);

const fetchAndPrintCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('Error fetching character data:', error);
        reject(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
      resolve();
    });
  });
};
