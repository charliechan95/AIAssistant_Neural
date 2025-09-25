from matplotlib import pyplot as plt
import tkinter 
from nltk.corpus import stopwords 
from tkinter import filedialog
from tkinter import *

from nltk.tokenize import word_tokenize 
from nltk.tokenize import sent_tokenize 
from nltk.stem import PorterStemmer, WordNetLemmatizer 
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import wordnet 
import nltk
import ssl


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('vader_lexicon')



from nltk.probability import FreqDist 


window = tkinter.Tk()
window.title("My NLP App")
window.geometry("700x700")


def open_file():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())
    file.close()
button = Button(text="OpenFile", command=open_file)
button.pack()


window.mainloop()

def read_file():
    with open('shakespeare.txt', 'r') as f:
        text = f.read()
      
        return text
    




def tokenize_words():

    readtokens = read_file()
    tokens = word_tokenize(readtokens)
    

    return tokens

print(tokenize_words())


def displayfreq():
    freq = FreqDist(word_tokenize(read_file()))
    print(freq.most_common(10))
    freq.plot(30, cumulative=False)
    #plt.show()





def remove_stopwords():
    stop_words = stopwords.words('english')
    #print(stop_words)

#removed stop words and append to no_stopwords
    no_stopwords = []
    for w in tokenize_words():
        if w not in stop_words:
            no_stopwords.append(w)
    print(no_stopwords)


    print(set(tokenize_words())-set(no_stopwords))

    no_stopwords.append("doing")
    return no_stopwords

def lemmatize_and_stem():
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    for words in remove_stopwords():
        print(stemmer.stem(words), lemmatizer.lemmatize(words, "v"))

def sentiment_analysis():

    sia = SentimentIntensityAnalyzer()
    print(sia.polarity_scores(str(remove_stopwords())))



print(lemmatize_and_stem())
print(sentiment_analysis())


#find synonyms for word    
synon = []
for syn in wordnet.synsets("good"):
    for lemma in syn.lemmas():
        synon.append(lemma.name())
print(synon)





















