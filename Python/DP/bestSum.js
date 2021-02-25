function bestSumMemo(sum, arr=[], memo={}){
    if (sum in memo){
        return memo[sum];
    }
    if (sum === 0) return [];
    if (sum < 0) return null;

    let curr = null;
    for (let i of arr){
        const remainder = sum - i;
        const result = bestSumMemo(remainder, arr, memo);
        if (result !== null){
            const combination = [...result, i];
            if (curr === null || curr.length > combination.length){
                curr = combination;
            }
        }
    }
    memo[sum] = curr;
    return curr;
}

console.log(bestSumMemo(8, [2,3,5]))
console.log(bestSumMemo(200, [2,3,5, 25, 50]))
