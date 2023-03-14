#!/usr/bin/node

const cmdLineArgs = process.argv.slice(2);

function add (a, b) {
  return (a + b);
}

const num1 = Number(cmdLineArgs[0]);
const num2 = Number(cmdLineArgs[1]);

console.log(add(num1, num2));
