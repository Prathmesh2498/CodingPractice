function canConstruct(s,arr){
    const table =   Array(s.length+1).fill(false);
    table[0] = true;
    
    for (let i=0;i<=s.length;i++){
        if(table[i] === true){
            for(let j of arr){
                if (j === s.slice(i, i+j.length)  && i+j.length<= s.length){
                    table[i+j.length] = true;
                }
            }
        }
    }

    return table[s.length];
}

console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "e", "eee", "ee", "eeeee"]));