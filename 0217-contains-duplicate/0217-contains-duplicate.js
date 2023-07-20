/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    const numberHash = {}
    for (let i = 0; i < nums.length; i++) {
        let v = nums[i]
        numberHash[v] = numberHash[v] + 1 || 1
        if (numberHash[v] == 2) {
            return true
        }
    }
    return false
};