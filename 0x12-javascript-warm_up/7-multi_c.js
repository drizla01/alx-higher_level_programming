#!/usr/bin/node
let argument = parseInt(process.argv[2], 10);

if (isNaN(argument) === false) {
  while (argument > 0) {
    console.log('C is fun');
    argument--;
  }
} else {
  console.log('Missing number of occurences');
}
