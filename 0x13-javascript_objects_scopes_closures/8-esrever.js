#!/usr/bin/node

exports.esrever = function (list) {
  const reverlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverlist.push(list[i]);
  }

  return (reverlist);
};
