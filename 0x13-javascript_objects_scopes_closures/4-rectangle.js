#!/usr/bin/node
class Rectangle {
  constructor (wt, ht) {
    if (wt > 0 && ht > 0) {
      this.width = wt;
      this.height = ht;
    }
  }

  print (printC = 'X') {
    let e;
    let k;
    let build = '';
    for (e = 0; e < this.height; e++) {
      if (e > 0) {
        build += '\n';
      }
      for (k = 0; k < this.width; k++) {
        build += printC;
      }
    }
    console.log(build);
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
