#!/usr/bin/node

const cmdLineArgs = process.argv.slice(2);
const len = cmdLineArgs.length;

if (len === 0 || len === 1) {
  console.log(0);
} else {
  let max = 0;
  for (let i = 0; i < len; i++) {
    if (max < cmdLineArgs[i]) {
      max = cmdLineArgs[i];
    }
  }
  console.log(max);
}
