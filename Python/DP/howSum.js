function howSum(sum, arr=[]){
    if (sum === 0) return [];
    if (sum < 0) return null;

    for (let i of arr){
        const remainder = sum - i;
        const result = howSum(remainder, arr);
        if (result !== null){
            return [...result, i];
        }
    }

    return null;
}

console.log(howSum(7, [2,3]));
//console.log(canSumMemo(300, [7,14])); -- Won't run with brute force.

//Memoized
function howSumMemo(sum, arr=[], memo={}){
    if (sum in memo){
        return memo[sum];
    }
    if (sum === 0) return [];
    if (sum < 0) return null;

    for (let i of arr){
        const remainder = sum - i;
        const result = howSumMemo(remainder, arr, memo);
        if (result !== null){
            memo[sum] = [...result, i];
            return memo[sum];
        }
    }
    memo[sum] = null;
    return null;
}

console.log(howSum(7, [2,3]));
console.log(howSumMemo(300, [5,14]));

