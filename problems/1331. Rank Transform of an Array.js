/**
 * @param {number[]} arr
 * @return {number[]}
 */
const { performance } = require("perf_hooks");

var arrayRankTransform = function (arr) {
    const rankMap = new Map();
    const sArr = [...new Set(arr)].sort((a, b) => a - b);

    sArr.forEach((num,index)=>{
      rankMap.set(num, index+1);
    });

    return arr.map(num=>rankMap.get(num));
};

const input = {
  inputOne: [40, 10, 20, 30],
  inputTwo: [100, 100, 100],
  inputThree: [37, 12, 28, 9, 100, 56, 80, 5, 12],
};

console.log(arrayRankTransform(input.inputOne));
console.log(arrayRankTransform(input.inputTwo));
const start = performance.now();

// time calculation
console.log(arrayRankTransform(input.inputThree));
const end = performance.now();
console.log(`Execution time: ${(end - start).toFixed(4)} ms`);
