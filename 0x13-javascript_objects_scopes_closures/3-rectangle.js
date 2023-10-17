#!/usr/bin/node
class Rectangle {
  constructor (wt, ht) {
    if (wt > 0 && ht > 0) {
      this.width = wt;
      this.height = ht;
    }
  }

  print () {
    let e;
    let k;
    let build = '';
    for (e = 0; e < this.height; e++) {
      if (e > 0) {
        build += '\n';
      }
      for (k = 0; k < this.width; k++) {
        build += 'X';
      }
    }
    console.log(build);
  }
}
module.exports = Rectangle;
