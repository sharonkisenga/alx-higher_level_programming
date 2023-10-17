#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (mesure) {
    super(mesure, mesure);
  }
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    this.print(c);
  }
}
module.exports = Square;
