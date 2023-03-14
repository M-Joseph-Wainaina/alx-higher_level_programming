#!/usr/bin/node

const cmdLineArgs = process.argv.slice(2);
const factor = Number(cmdLineArgs[0]);

function factorial (factor) {
  if (factor === 1) {
    return 1;
  } else {
    return factor * factorial(factor - 1);
  }
}

if (!factor) {
  console.log(1);
} else {
  console.log(factorial(factor));
}
