#!/usr/bin/node
/*
 * this is a converter
 */
exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
