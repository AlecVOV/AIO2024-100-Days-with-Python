corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]
input_text = ["Tôi thích AI thích Toán"]

all_words = sorted({word.lower().strip() for sentence in corpus for word in sentence.split()})


#Step 1: Divide sentence into vocabularies and pre-process all the words:
def tokenize(sentence):
    words = sentence.lower().split() #delete all the punctuations and lower case
    return words

#Step 2: create a collection with all the vocab that appear in the text without any similar component
unique_words = set() #creating a set of vocab that appear the text, and sorted it in alphabet
for input_sentence in corpus: 
    words = tokenize(input_sentence)
    unique_words.update(words)

unique_words = sorted(unique_words)


#Step 3: demonstrate the input in vector
def vectorize(sentence, unique_words):
    words = tokenize(sentence)
    #initalize the vector with countable system with 1st appear is 0:
    vector = [0] * len(unique_words)
    #couting the words that appear in the sentence:
    for word in words:
        if word in unique_words:
            idx = unique_words.index(word)
            vector[idx] += 1
    return vector


#Illustrate reach sentence in the inputs to become a vector:
vectors = [vectorize(sentence, unique_words) for sentence in input_text]


#Printing the result
print(f"Unique words: {unique_words}")
for i, vector in enumerate(vectors):
    print(f"Vector {i + 1}: {vector}")

