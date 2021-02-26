function canConstruct(s, arr=[], memo={}){
    if (s in memo){
        return memo[s];
    }
    if (s===''){
        return true;
    }
    for (let word of arr){
        if (s.indexOf(word) === 0){
            const suffix = s.slice(word.length);
            if (canConstruct(suffix, arr, memo)){
                memo[s] = true;
                return true;
            }
        }
    }
    memo[s] = false;
    return false;
}

console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "e", "eee", "ee", "eeeee"]));