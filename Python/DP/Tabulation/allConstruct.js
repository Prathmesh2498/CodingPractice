function allConstruct(s, arr){
    const table  = Array(s.length + 1).fill().map(()=>[]);
    table[0] = [[]];
    for (let i=0;i<=s.length;i++){
        for (word of arr){
            if (s.slice(i, i+word.length) === word){
                const combinations = table[i].map(subArray => [...subArray, word]);
                table[i+word.length].push(...combinations); 
            }
        }
    }

    return table[s.length];
}

console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]));
console.log(allConstruct("eeeeeeef", ["e", "e", "eee", "ee", "eeeee"]));
console.log(allConstruct("eeee", ["e", "eee", "ee", "eeee"]));