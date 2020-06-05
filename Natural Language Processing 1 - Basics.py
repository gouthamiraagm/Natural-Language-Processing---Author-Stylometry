import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

#tokenizing---1)word tokenizers......(seperated by words)
#             2)sentence tokenizers.....(seperated by sentence)
#lexicon and corporas
#corpora=it is just a body of text ex:medical journals,English language 
#lexicon--it is like a dictionary --the word and meanings
#investor speak....regular engkish speak

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(sent_tokenize(EXAMPLE_TEXT))
print(word_tokenize(EXAMPLE_TEXT))
for i in word_tokenize(EXAMPLE_TEXT):
    print(i)