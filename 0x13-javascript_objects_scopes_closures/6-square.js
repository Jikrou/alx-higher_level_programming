#!/usr/bin/node

const SquAre = require('./5-square');

class Square extends SquAre {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let prinTc = [];
        for (let j = 0; j < this.width; j++) {
          prinTc += 'C';
        }
        console.log(prinTc);
      }
    }
  }
}

module.exports = Square;
