/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const bracketsStack = []

    for (let i = 0 ; i < s.length ; i++) {
        switch (s[i]){
            case "(":
                bracketsStack.push("()")
                break
            case ")":
                if (bracketsStack.pop() !== "()") return false
                break
            case "[":
                bracketsStack.push("[]")
                break
            case "]":
                if (bracketsStack.pop()  !== "[]") return false
                break
            case "{":
                bracketsStack.push("{}")
                break
            case "}":
                if (bracketsStack.pop()  !== "{}") return false
                break
        }
    }

    if (bracketsStack.length !== 0) {
        return false
    }

    return true
};