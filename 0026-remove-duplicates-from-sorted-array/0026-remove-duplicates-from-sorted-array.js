/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    // Edge case only one element
    if (nums.length === 1) {
        return 1
    }

    // Edge case only two element
    if (nums.length === 2) {
        if (nums[0] !== nums[1]) {
            return 2
        }
        return 1
    }

    let head1 = 0
    let head2 = 1

    while (head2 < nums.length) {
        if (nums[head1] === nums[head2]) {
            nums.splice(head2, 1)
        } else {
            head2 += 1
            head1 += 1
        }
    }

    return nums.length
};