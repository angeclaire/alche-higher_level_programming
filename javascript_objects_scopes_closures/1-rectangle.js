#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w ? Number(w) : 0;
    this.height = h ? Number(h) : 0;
  }
}

module.exports = Rectangle;
