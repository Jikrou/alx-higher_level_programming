#!/usr/bin/node

const fs = require('fs');
const r = process.argv[2];
fs.readFile(r, (err, wr) => {
  if (err) throw err;
  else {
    console.log(wr.toString());
  }
});
