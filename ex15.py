# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

def solution1(words):
    revSentence = ''
    for i in words[::-1]:
        revSentence += i + ' '
    return revSentence

def solution2(words):
    return ' '.join(words[::-1])

sentence = input('Write a sentence: ')
words = sentence.split()

print(sentence)
print(solution1(words))
print(solution2(words))