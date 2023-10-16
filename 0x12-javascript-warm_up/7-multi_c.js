#!/usr/bin/node


const lang = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let e = 0; e < parseInt(process.argv[2]); e++) {
    console.log(lang);
  }
}
