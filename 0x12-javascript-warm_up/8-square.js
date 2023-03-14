#!/usr/bin/node

const cmdLineArgs = process.argv.slice(2);
const occurences = Number(cmdLineArgs[0]);

if (!occurences) {
  console.log('Missing size');
} else {
  for (let i = 0; i < occurences; i++) {
    for (let j = 0; j < occurences; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
