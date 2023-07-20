/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let currentNum = num
    let countSteps = 0
    while (currentNum != 0) {
        if (currentNum % 2 == 0) {
            currentNum = currentNum / 2
        } else {
            currentNum = currentNum - 1
        }
        countSteps += 1
    }

    return countSteps
};