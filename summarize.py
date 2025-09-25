from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import ssl 
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')
nltk.download('punkt')
with open('wikipedia.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
stopWords = set(stopwords.words('english'))

print(text)
tokens_word = word_tokenize(text)
print(tokens_word)



freqTable = dict()
for tokens_word in tokens_word:
    tokens_word = tokens_word.lower()
    if tokens_word in stopWords:
        continue
    if tokens_word in freqTable:
        freqTable[tokens_word] += 1
    else:
        freqTable[tokens_word] = 1
print(freqTable)

sentences = sent_tokenize(text)
print(sentences)

sentences[0]

def getsentenceValue():
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
    return sentenceValue
    print(sentenceValue)
sentenceValue = getsentenceValue()
print(sentenceValue)

def getsumValue():
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    average = int(sumValues / len(sentenceValue))
    return average

average = getsumValue()
print(average)

    
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
print(summary)



