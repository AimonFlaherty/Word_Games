import loadDictionary

word_list = loadDictionary.load('dictionary.txt')
anagram_list = []

print('Enter your word: ')
base_word = input()

base_word = base_word.lower()
print('Input word: {}'.format(base_word))

sorted_word = sorted(base_word)
for word in word_list:
    word = word.lower()
    if word != base_word:
        if sorted(word) == sorted_word:
            anagram_list.append(word)
print()
if len(anagram_list) == 0:
    print('Anagram list is empty')
else:
    print('Anagrams:', *anagram_list, sep = '\n')
