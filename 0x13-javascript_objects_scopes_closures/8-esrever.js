#!/usr/bin/node
exports.esrever = function (list) {
  let thisList = [];
  let e;
  for (e = list.length - 1; e >= 0; e--) {
    thisList.push(list[e]);
  }
  return thisList;
};
