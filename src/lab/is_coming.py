from nltk.tokenize import word_tokenize, sent_tokenize

print(word_tokenize("This is the queen's castle. Yay!"))
# ['This', 'is', 'the', 'queen', "'s", 'castle', '.', 'Yay', '!']
print(sent_tokenize(got)[1:3])
# ['"The wildlings are \ndead."', '"Do the dead frighten you?"']
