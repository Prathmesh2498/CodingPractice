function howSum(sum, arr) {
    const table = Array(sum + 1).fill(null);
    table[0] = [];

    for (let i = 0; i <= sum; i++) {
        if (table[i] !== null) {
            for (let j of arr) {
                if (i + j <= sum) {
                    table[i + j] = [...table[i], j];
                }
            }
        }
    }
    return table[sum];
}

console.log(howSum(7, [5,3,4]));
console.log(howSum(7, [2,3]));
console.log(howSum(300, [7,14]));

