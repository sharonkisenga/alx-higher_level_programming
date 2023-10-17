#!/usr/bin/node
class Rectangle {
  constructor (wt, ht) {
    if (wt > 0 && ht > 0) {
      this.width = wt;
      this.height = ht;
    }
  }
}

module.exports = Rectangle;
