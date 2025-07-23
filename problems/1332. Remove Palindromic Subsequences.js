/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function (s) {
    if(s.length  === 0) return 0;
    return s === s.split("").reverse().join("") ? 1 : 2;

}

const input = {
  one: "ababa",
  two: "abb",
  three: "baabb",
};

console.log(removePalindromeSub(input.one)); // 1
console.log(removePalindromeSub(input.two)); // 2
console.log(removePalindromeSub(input.three)); // 3
