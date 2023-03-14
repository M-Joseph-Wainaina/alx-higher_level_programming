#!/usr/bin/node

const cmdLineArgs = process.argv.slice(2);

if (!cmdLineArgs[0]) {
  console.log('No argument');
} else {
  console.log(cmdLineArgs[0]);
}
