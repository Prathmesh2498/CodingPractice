function canSum(sum, arr){
 const table = Array(sum+1).fill(false);
 table[0] = true;
 for (let i=0;i<=sum;i++){
    if (table[i] === true){
        for (let j of arr){
            if ((i+j) <= sum){
                table[i+j] = true;
            }
        }
    }
 }
 return table[sum];
}

console.log(canSum(300, [7,5,14]));
