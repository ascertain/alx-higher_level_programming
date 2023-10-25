#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const report = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        if (!report[todo.userId]) {
          report[todo.userId] = 0;
        }
        report[todo.userId]++;
      }
    });
    console.log(report);
  }
});