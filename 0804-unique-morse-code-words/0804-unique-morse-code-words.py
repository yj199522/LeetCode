class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_array = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        if len(words) < 2:
            return len(words)
        result = set()
        for word in words:
            word = word.lower()
            transformations = ""
            for chr in word:
                transformations += morse_code_array[ord(chr) - 97]
            result.add(transformations)
        return len(result)
                