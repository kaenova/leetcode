/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Target 10
// Current i = 3
// 10 - 3 = 7
// 7 : i
// O(n)
var twoSum = function (nums, target) {
    var diffHash = {
        // Difference : substract index
    }

    for (let i = 0; i < nums.length; i++) {
        currentNumber = nums[i]
        let diff = target - currentNumber

        // Somehow we found the difference in i
        if (diffHash[nums[i]] !== undefined) {
            return [diffHash[currentNumber], i]
        } else {
            diffHash[diff] = i
        }

        if (i === 0) {
            continue
        }
    }
};

// O(n^2)
// var twoSum = function(nums, target) {
//     for (let i = 0 ; i < nums.length; i++){
//         for (let j = 1 ; j < nums.length; j++) {
//             if (nums[i] + nums[j] === target) {
//                 return [i, j]
//             }
//         }
//     }
// };