/**
 * @param {number[]} prices
 * @return {number}
 */

// O(n)
var maxProfit = function (prices) {
    let minimumPriceProposeIdx = 0
    let minimumPriceIdx = 0
    let maximumPriceIdx = 0

    let currentProfit = 0

    prices.forEach((v, i) => {

        // If we found price that is lower then current but dunno if we found any maximum Price, we save it as a propose
        if (v < prices[minimumPriceProposeIdx]) {
            minimumPriceProposeIdx = i
        }

        // We update if we found maximum idx ahead of minimum price proposal
        if (v - prices[minimumPriceProposeIdx] > currentProfit) {
            minimumPriceIdx = minimumPriceProposeIdx
            maximumPriceIdx = i
            currentProfit = v - prices[minimumPriceProposeIdx]
        }
    })

    return prices[maximumPriceIdx] - prices[minimumPriceIdx]
};


/*
// O(n^n)
var maxProfit = function(prices) {
    let maximumProfit = 0
    for (let pivot = 1 ; pivot < prices.length ; pivot++) {
        for (let i = 0 ; i < pivot ; i++) {
            let profit = prices[pivot] - prices[i]
            if (profit > maximumProfit) {
                maximumProfit = profit
            }
        }
    }
    
    return maximumProfit
};
*/