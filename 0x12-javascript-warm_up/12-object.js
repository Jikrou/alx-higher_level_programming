#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
const newObject = myObject;
newObject.value = 89;
console.log(myObject);
