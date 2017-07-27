from collections import Counter
import numpy as np
# Text pre processing
import nltk
# from nltk.corpus import stopwords #Delete useless

from nltk.tokenize import word_tokenize  # Separates a sentence
from googletrans import Translator  # Translat a sentence
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
translator = Translator()
useless_words = ["be", "fin", "fine", 'violate']


def processing(text):
    # print text
    translation = translator.translate(text).text
    # print translation
    text = word_tokenize(translation)  # SPLIT THE SENTENCE
    # Deleting unnecessary words
    filtered_sentence = []

    tagging = nltk.pos_tag(text)
    # print tagging
    words = []
    tags = []
    verbs = []
    nouns = []
    other = []
    special = []
    adjetives = []

    words.extend([x[0] for x in tagging])
    tags.extend([x[1] for x in tagging])

    for i in range(0, len(words), 1):
        x = list(tags[i])
        if x[0] == 'V':
            verbs.append(lemmatizer.lemmatize(words[i], 'v'))
        elif x[0] == 'N':
            nouns.append(lemmatizer.lemmatize(words[i]))
        elif x[0] == "J":
            adjetives.append(lemmatizer.lemmatize(words[i]))
        else:
            other.append(lemmatizer.lemmatize(words[i]))

        if words[i] == "not":
            special.append(words[i])

    words = verbs + nouns + adjetives + special

    for w in words:
        if w not in useless_words:
            filtered_sentence.append(w)

    return filtered_sentence


def open_questions(text):
    text = open("Agente-de-transito.txt", "r").readlines()
    value = 0
    j = 0
    sentences = []
    words = []
    target = np.zeros((130,1))
    for i in range(0, len(text), 1):
        try:
            value = (int(text[i]))
        except:
            sentences.append(text[i])
            target[j] = value
            j += 1
    target = np.trim_zeros(target, 'b')

    print len(target)
    print len(sentences)

    # Obtain the length and values of the input vector
    for i in sentences:

        words.extend(processing(i))

    palabras = dict(Counter(words))
    words = sorted(palabras.keys())

    vector_string = {}
    for counter, value in enumerate(words):
        print(counter, value)
        vector_string[str(value)] = counter

    print vector_string

    data = np.zeros((counter+1,len(target)))

    for i in range(0,len(sentences),1):
        words = processing(sentences[i])
        for j in words:
            try:
               data[vector_string[str(j)],i] = 1
            except:
                None

    data=np.concatenate((data,target.transpose()))

    return data,vector_string

data,vector_string = open_questions("Agente-de-transito.txt")

np.save("database",data)
np.save("vector_string", vector_string)

print data