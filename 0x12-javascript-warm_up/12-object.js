#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

const newObject = myObject;
newObject.value = 89;
console.log(myObject);
