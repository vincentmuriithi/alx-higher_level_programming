#!/usr/bin/node
//script for showing requets status code

const request = require('request');
const url = process.argv[2];

request(url, (error, response)=>{
if (error)
console.error(error);
else
console.log(`code: ${response.statusCode}`);
});
