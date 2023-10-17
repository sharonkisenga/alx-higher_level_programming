#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let e = 0;
  list.forEach(function (obj) {
    if (obj === searchElement) {
      e++;
    }
  });
  return e;
};
