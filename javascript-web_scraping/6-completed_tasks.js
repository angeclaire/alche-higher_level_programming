#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const todos = JSON.parse(body);
  const completedByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedByUser[userId]) {
        completedByUser[userId] += 1;
      } else {
        completedByUser[userId] = 1;
      }
    }
  });

  console.log(completedByUser);
});
