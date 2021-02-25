/*
Q: Find no of ways to travel from top left to bottom right of m * n grid 
   such that only right and down moves are allowed.
*/

const gridTrav = (m,n, memo={}) => { 
    const key = m + ',' + n;
    const revkey = n + ',' + n;
    if (key in memo){
        return memo[key];
    }
    if (m==0 || n == 0){
        return 0;
    }
    if (m==1 && n==1){
        return 1;
    }
    memo[key] = gridTrav(m-1, n, memo) + gridTrav(m, n-1, memo); 
    return memo[key];
}

console.log(gridTrav(18,18));