function allConstruct(s, arr, memo={}){
    if (s in memo){
        return memo[s];
    }
    if (s ===''){
        return [[]];
    }

    const result = [];

    for (let i of arr){
        if (s.indexOf(i) === 0){
            const suffix = s.slice(i.length);
            const suffixWays = allConstruct(suffix, arr, memo);
            const targetWays = suffixWays.map(way=>[ i , ...way] )
            result.push(...targetWays);
        }
    }

    memo[s] = result;
    return result;
}

console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]));
console.log(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "e", "eee", "ee", "eeeee"]));
console.log(allConstruct("eeee", ["e", "eee", "ee", "eeee"]));