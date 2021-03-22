import loadDictionary

word_list = loadDictionary.load('dictionary.txt')

def findPalingrams():
    paligram_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    paligram_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    paligram_list.append((rev_word[:end-i], word))
    return paligram_list

paligrams = findPalingrams()
paligrams_sorted = sorted(paligrams)

print('\nNumber of paligrams = {}\n'.format(len(paligrams_sorted)))
for first, second in paligrams_sorted:
    print("{} {}".format(first, second))
