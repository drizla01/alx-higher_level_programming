#!/usr/bin/node
function secondBiggestNumber (array) {
  const len = array.length;

  let largest = array[0];
  let secondLargest = 0;

  if (len < 2) {
    return (secondLargest);
  }
  for (let count = 1; count < len; count++) {
    if (array[count] > largest) {
      secondLargest = largest;
      largest = array[count];
    } else if (array[count] > secondLargest && array[count] !== largest) {
      secondLargest = array[count];
    }
  }
  return (secondLargest);
}

const myArray = process.argv.slice(2).map(Number);
const secondLargest = secondBiggestNumber(myArray);
console.log(secondLargest);
