import scrabble
import string

## Check if any two same characters exist in a word
# for word in scrabble.wordlist:
#     for i in range(len(word)-1):
#         if(word[i] == word[i+1]):
#             print(word)
#             break

## Check if any English character doesn't exist double in a word
# for letter in string.ascii_lowercase:
#     exists = False
#     for word in scrabble.wordlist:
#         if letter * 2 in word:
#             exists = True
#             break
#     if not exists:
#         print("There are no English word with a double " + letter)

## Find words containing all 5 vowels
# vowels = "aeiou"
#
# def has_all_vowels(word):
#     for vowel in vowels:
#         if vowel not in word:
#             return False
#     return True
#
# for word in scrabble.wordlist:
#     if has_all_vowels(word):
#         print(word)


## Find the longest Palindrome
# def is_palindrome(word):
#     for i in range(len(word)//2):
#         if word[i] != word [-i-1]:
#             return False
#     return True
#
# longest = ""
#
# for word in scrabble.wordlist:
#     if is_palindrome(word):
#         if len(word) > len(longest):
#             longest = word
# if longest != "":
#     print("Longest Palindrome is '" + longest + "'")

longest = ""
for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
            longest = word
print(longest)