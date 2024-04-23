#!/usr/bin/node
const request = require('request');

const Uee = process.argv[2];

const data = {
};

request(Uee, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    for (const task of todos) {
      if (task.completed && !(task.userId in data)) {
        data[task.userId] = 0;
      }
      if (task.completed) {
        data[task.userId] += 1;
      }
    }
    console.log(data);
  }
});
