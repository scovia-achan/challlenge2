def countVowels(word):
    if isinstance(word,str):

        vowels = "aeiou"
        # changing the word into lower case
        new_word = word.lower()
        # the set property ensures there is no duplicate letter in the string
        no_duplicates = set(new_word)
        duplicates = len(new_word) - len(no_duplicates)
        vowel_string = ""

        for letter in vowels:
            if letter in no_duplicates:
                vowel_string += str(letter)

        return (vowel_string, duplicates)
    else:
        return "invalid input"

print(countVowels('didida'))
