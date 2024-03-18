#!/usr/bin/node
const arg = parseInt(process.argv[2], 10);

if (isNaN(arg) === false) {
  for (let countx = 0; countx < arg; countx++) {
    let line = '';
    for (let county = 0; county < arg; county++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
