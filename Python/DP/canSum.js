function canSum(sum, arr=[]){
    if (sum === 0){
        return true;
    }
    if(sum < 0){
        return false;
    }

    for (let i of arr){
        const remainder = sum - i;
        if (canSum(remainder, arr)){
            return true;
        }
    }
    return false; 
    /*
        We write false here because we only know that the target sum is
        not possible after all possibilities are checked, i.e. arr traversal is completed. 
    */
}

console.log(canSum(7, [1,2,3,4]));


function canSumMemo(sum, arr=[], memo={}){
    if (sum in memo){
        return memo[sum];
    }
    if (sum === 0){
        return true;
    }
    if(sum < 0){
        return false;
    }

    for (let i of arr){
        const remainder = sum - i;
        if (canSumMemo(remainder, arr, memo)){
            memo[sum] = true;
            return true;
        }
    }
    memo[sum] = false;
    return false; 
    /*
        We write false here because we only know that the target sum is
        not possible after all possibilities are checked, i.e. arr traversal is completed. 
    */
}

console.log(canSumMemo(7, [1,2,3,4]));
console.log(canSumMemo(300, [7,14]));