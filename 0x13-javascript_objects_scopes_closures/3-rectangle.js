#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return 1;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let pRect = [];
      for (let j = 0; j < this.width; j++) {
        pRect += 'X';
      }
      console.log(pRect);
    }
  }
}

module.exports = Rectangle;
