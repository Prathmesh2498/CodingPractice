function bestSum(sum, arr){
    const table = Array(sum+1).fill(null);
    table[0] = [];

    for (let i=0;i<=sum;i++){
        if (table[i]!==null){
            for (let j of arr){
                if (i+j<=sum){
                    const combination = [...table[i], j]; 
                    if (!table[i+j] || table[i+j].length > combination.length){
                        table[i+j] = combination;
                    }
                }
            }
        }
    }

    return table[sum];
}

console.log(bestSum(8, [2,3,5]))
console.log(bestSum(200, [100, 5, 2, 4]))
