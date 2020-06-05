from nltk.corpus import stopwords
#set(stopwords.words('english')) ---type in console
from nltk.tokenize import word_tokenize
example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

words = word_tokenize(example_sent)

filtered_sentence=[]

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

#filtered_sentence = [w for w in word_tokens if not w in stop_words]
print(words)
print( filtered_sentence)