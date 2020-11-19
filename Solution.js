"use strict";
//solution with division
var input = [1, 2, 3, 4, 5];
var mul = input.reduce((a, b) => a * b);


input.forEach(myfunction);

function myfunction(element, index) {

    input[index] = mul / element;
}
console.log(input);
//solution without division
var input = [1, 2, 3, 4, 5];
let output = new Array(input.length);
for (let i = 0; i < input.length; ++i) output[i] = 1;
for (var i in input) {
    for (var k in input) {
        if (k != i) {
            output[i] = output[i] * input[k];
        }
    }
}

console.log(output);
