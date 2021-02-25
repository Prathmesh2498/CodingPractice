const fib = (n) => {
    if (n<=2){
        return 1;
    }
    else {
        return fib(n-1) + fib(n-2);
    }
}
//Won't run without breaking the computer
//console.log(fib(50));


//Memoization
const dpFib = (n, memo = {}) => {
    if (n in memo) return memo[n];
    if (n==0){
        return 0;
    }
    if (n<=2){
        return 1;
    }
    else {
        memo[n] = dpFib(n-1, memo) + dpFib(n-2, memo);
        return memo[n];
    }
}

console.log(dpFib(100));