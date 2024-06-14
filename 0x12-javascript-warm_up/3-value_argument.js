#!/usr/bin/node

// Access command-line arguments
const args = process.argv.slice(2);

// print the first argument
if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
