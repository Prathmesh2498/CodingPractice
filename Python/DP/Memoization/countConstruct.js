function countConstruct(s, arr=[], memo = {}){
    if (s in memo){
        return memo[s];
    }
    if(s === ''){
        return 1;
    }

    let total = 0;
    for (i of arr){
        if (s.indexOf(i) === 0){
            const waysToGenerateSuffix = countConstruct(s.slice(i.length), arr, memo); //Slice contains everything after index = i.length
            total += waysToGenerateSuffix;
        }
    }   
    memo[s] = total;
    return total;
}

console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "e", "eee", "ee", "eeeee"]));