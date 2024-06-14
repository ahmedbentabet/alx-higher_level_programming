#!/usr/bin/node

// Access command-line arguments
const args = process.argv.slice(2);

// Determine the number of arguments
if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
