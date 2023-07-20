/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let listHead = 0
    while (listHead < nums.length) {
        if (nums[listHead] == val) {
            nums.splice(listHead, 1)
        } else {
            listHead += 1
        }
    }
    return nums.length
};