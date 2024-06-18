#!/usr/bin/node
const av = process.argv;
if (av[2]) {
  console.log(av[2]);
} else {
  console.log('No argument');
}
