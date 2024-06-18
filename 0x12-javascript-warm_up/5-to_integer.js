#!/usr/bin/node
const av = process.argv;
if (Number(av[2])) {
  const avInt = Math.trunc(av[2]);
  console.log('My number:', avInt);
} else {
  console.log('Not a number');
}
