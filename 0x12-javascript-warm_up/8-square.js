#!/usr/bin/node
const av = process.argv;
const x = av[2];

if (Number(x)) {
  for (let i = 0; i < x; i++) {
    let sz = [];
    for (let j = 0; j < x; j++) {
      sz += 'X';
    }
    console.log(sz);
  }
} else {
  console.log('Missing size');
}
