#!/usr/bin/node

const cmdLineArgs = process.argv.slice(2);
const toNumber = Number(cmdLineArgs[0]);

if (!toNumber) {
  console.log('Not a number');
} else {
  console.log('My number: ' + toNumber);
}
