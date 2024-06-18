#!/usr/bin/node
const av = process.argv;
const x = av[2];

if (Number(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
