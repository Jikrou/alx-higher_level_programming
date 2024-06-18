#!/usr/bin/node

function add (a, b) {
  const av = process.argv;
  let sum = 0;

  a = Number(av[2]);
  b = Number(av[3]);
  sum = a + b;
  console.log(sum);
}

add();
