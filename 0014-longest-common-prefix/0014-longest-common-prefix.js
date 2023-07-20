/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let longestPrefix = ""

    if (strs.length === 0) {
        return longestPrefix
    }

    // Search for longest word
    let minLength = strs[0].length
    for (let i = 1 ; i < strs.length ; i ++) {
        if (minLength > strs[i].length) {
            minLength = strs[i].length
        }
    }


    for (let i = 0 ; i < minLength ; i++) {
        let proposeChar = strs[0][i]
        let proposeCharValid = true
        for (let j = 1 ; j < strs.length; j++) {
            if (proposeChar !== strs[j][i]) {
                proposeCharValid = false
                break
            }
        }

        if (proposeCharValid) {
            longestPrefix += proposeChar
        } else {
            break
        }
    }


    return longestPrefix
};