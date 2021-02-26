function countConstruct(s, arr) {
    const table = Array(s.length + 1).fill(0);
    table[0] = 1;

    for (let i = 0; i <= s.length; i++) {
        if (table[i] !== 0) {
            for (let word of arr) {
                if (s.slice(i, i + word.length) === word && i + word.length <= s.length) {
                    table[i+word.length] += table[i];
                }
            }
        }
    }
    return table[s.length];
}

console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def","ef", "abcd"]));
console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "e", "eee", "ee", "eeeee"]));