words = ['python', 'java', 'javascript', 'go', 'rust', 'accops']


# Find Words greater than 4 chars

long_words = list(filter(lambda word : len(word) > 4 , words))
print(long_words)

#Find the words which starts with 'J'

j_word = list(filter(lambda word : word[0] == 'j' , words))
print(j_word)

#Find the words containing 'a'

a_word = list(filter(lambda word : 'a' in word , words))
print(a_word)