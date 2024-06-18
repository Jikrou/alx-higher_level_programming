#!/usr/bin/node
const av = process.argv;
const a = Number(av[2]);

console.log(factFun(a));

function factFun (x) {
  let n = 1;
  if (isNaN(x) || x === 1 || x === 0) {
    return 1;
  } else {
    n = x * (factFun(x - 1));
  }
  return n;
}
