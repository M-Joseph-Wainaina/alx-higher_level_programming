#!/usr/bin/node

const cmdLineArgs = process.argv.slice(2);
const occurences = Number(cmdLineArgs[0]);

if (!occurences) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < occurences; i++) {
    console.log('C is fun');
  }
}
