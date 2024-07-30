#!/usr/bin/node

const fs = require('fs');
const w = process.argv[2];
const r = process.argv[3];
fs.writeFile(w, r, (err) => {
  if (err) throw err;
});
