#!/usr/bin/node
const av = process.argv.length;
const avg = process.argv;

if (av === 2) {
  console.log(0);
} else if (av === 3) {
  console.log(1);
} else {
  let mx = -Infinity;
  let seMx = -Infinity;
  for (let i = 2; i < av; i++) {
    const nm = Number(avg[i]);
    if (nm > mx) {
      seMx = mx;
      mx = nm;
    } else if (nm > seMx) {
      seMx = nm;
    }
  }
  console.log(seMx);
}
