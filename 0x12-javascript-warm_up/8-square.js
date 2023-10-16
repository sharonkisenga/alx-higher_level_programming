#!/usr/bin/node
// prints a square

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let e = 0; i < parseInt(process.argv[2]); e++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
