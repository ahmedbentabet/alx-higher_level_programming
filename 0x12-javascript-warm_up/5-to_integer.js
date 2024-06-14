#!/usr/bin/node

const args = process.argv.slice(2);
const toInt = parseInt(args[0]);

if (isNaN(toInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${toInt}`);
}
