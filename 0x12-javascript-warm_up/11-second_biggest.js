#!/usr/bin/node

const cmdLineArgs = process.argv.slice(2);
const len = cmdLineArgs.length;

if (len === 0 || len === 1) {
  console.log(0);
} else {
  const sortedArr = cmdLineArgs.sort(function (a, b) { return (a - b); });
  console.log(sortedArr[len - 2]);
}
