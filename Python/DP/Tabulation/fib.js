//Usually the table is of size inputLen+1

//[0 0 0 0 0 0 0] -> for fib(6)

//Init as [0 1 0 0 0 0 0]

/*
    Iterations
    1. [0 1 1 0 0 0 0]
    2. [0 1 1 2 0 0 0]
    3. [0 1 1 2 3 0 0]
    4. [0 1 1 2 3 5 0]
    5. [0 1 1 2 3 5 8]
*/

function fib(n){
    const a = Array(n+1).fill(0);
    a[0] = 0;
    a[1] = 1;

    for (let i=2;i<=n;i++){
        a[i] = a[i-1] + a[i-2]
    }
    return a[n];
}

console.log(fib(50));
