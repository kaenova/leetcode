/**
 * @param {number} x
 * @return {boolean}
 */
// O(n/2)
var isPalindrome = function(x) {
    let strNumber = `${x}`
    let strLength = strNumber.length

    let i = 0
    let j = strLength - 1 
    while (i <= j) {
        if (strNumber[i] !== strNumber[j]){
            return false
        }
        i++
        j--
    }

    return true
};