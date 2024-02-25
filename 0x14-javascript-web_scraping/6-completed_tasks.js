#!/usr/bin/node
//Script that computes the number of tasks completed by user id.

const request = require("request");
const url = process.argv[2];

request(url, (error, response, body)=> {
	if (error){
		console.error('Error: ', error);
		return;
	}

	if (response.statusCode !== 200){
		console.error('Invalid response', response.statusCode);
		return;
	}

	const todos = JSON.parse(body);
	const completedTasksByUser = {};

	todos.forEach(todo=> {
		if (todo.completed) {
			if (completedTasksByUser[todo.userId]) {
				completedTasksByUser[todo.userId]++;
			}
			else{
				completedTasksByUser[todo.userId] = 1;
			}
		}
	});
	console.log(completedTasksByUser);
});
