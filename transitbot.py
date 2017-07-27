import numpy as np
import nltk
from nltk.tokenize import word_tokenize  # Separates a sentence
from googletrans import Translator  # Translat a sentence
from nltk.stem.wordnet import WordNetLemmatizer
from keras.models import load_model


model = load_model("multas.h5")
vector_string = np.load("vector_string.npy").item()
lemmatizer = WordNetLemmatizer()
translator = Translator()

useless_words = ["be","fin","fine","violate"]
total_words = 59


def processing(text):
    # print text
    translation = translator.translate(text).text
    print(translation)
    text2 = word_tokenize(translation)  # SPLIT THE SENTENCE
    # Deleting unnecessary words
    filtered_sentence = []

    tagging = nltk.pos_tag(text2)
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
def into_vectors(text,vector_string,total_words):
    data = np.zeros((1,total_words))
    words = processing(text)
    for i in words:
        print(words)
        try:
            data[0,vector_string[str(i)]] = 1
        except:
            None
    return data


# THE BEGINNING OF THE PREDICTION PART

def classifier(text):
    print (text)
    input = into_vectors(text,vector_string, total_words )
    print (input)
    aa = model.predict(input, batch_size = 1)
    b = aa[0]

    if np.argmax(b) < 0.90:
        print ("No tengo registro de esa situacion")

    else:
        print (b)
        print (np.argmax(b))
        print (str((np.amax(b)*100)) + "%")