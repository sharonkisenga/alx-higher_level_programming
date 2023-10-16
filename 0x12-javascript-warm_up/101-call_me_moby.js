#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  for (let e = 0; e < x; e++) {
    theFunction();
  }
};
