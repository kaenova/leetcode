/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    const symbolDict = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    }

    let total = 0

    let strLength = s.length
    let i = 0
    while (i < strLength) {
        let char = s[i]
        let adder = 0

        // Lookup ahead one time if only it's now overflow
        if (i + 1 <= strLength - 1) {
            let nextChar = s[i + 1]
            if (char == "I" && ["V", "X"].indexOf(nextChar) !== -1) {
                adder += symbolDict[nextChar] - symbolDict["I"]
            } else if (char == "X" && ["L", "C"].indexOf(nextChar) !== -1) {
                adder += symbolDict[nextChar] - symbolDict["X"]
            } else if (char == "C" && ["D", "M"].indexOf(nextChar) !== -1) {
                adder += symbolDict[nextChar] - symbolDict["C"]
            }
        }

        if (adder !== 0) {
            total += adder
            i += 2
        } else {
            total += symbolDict[char]
            i += 1
        }
        // console.log(i, char, total)
    }

    return total
};