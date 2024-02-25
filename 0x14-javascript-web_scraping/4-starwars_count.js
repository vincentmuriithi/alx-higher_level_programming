#!/usr/bin/node
//Script that that prints the number of movies where the character “Wedge Antilles” is present.

const request = require("request");
const url = process.argv[2];
const characterId = 18;

request(url, (error, response, body)=> {
	if (error)
		console.error(error);
	else{
		const filmData = JSON.parse(body).results;
		let k = 0;
		filmData.forEach(film => {
			if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`))
				k++;
		});
	console.log(k);
	}
});
