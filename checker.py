import re
from collections import Counter

def get_ngrams(text, n):
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    # Tokenize the text into words
    words = text.split()
    # Create n-grams using a sliding window
    ngrams = zip(*[words[i:] for i in range(n)])
    # Return the n-grams as a list
    return list(ngrams)

def train_grammar_model(corpus, n):
    # Initialize the n-gram model
    model = Counter()
    # Process each sentence in the corpus
    for sentence in corpus:
        # Generate n-grams for the sentence
        ngrams = get_ngrams(sentence, n)
        # Update the model with the n-grams
        model.update(ngrams)
    # Return the trained model
    return model

def check_grammar(sentence, model, n):
    # Generate n-grams for the sentence
    ngrams = get_ngrams(sentence, n)
    # Check the frequency of each n-gram in the model
    for ngram in ngrams:
        if model[ngram] == 0:
            print("Possible grammar error: ", ngram)
        else:
            print("No Grammar error")    

# Example usage:
# Train the grammar model using a corpus of sentences
corpus = [
    "The cat is sitting on the mat.",
    "I am going to the park.",
    "She plays the piano beautifully.",
    "The dog is running"
]
n = 3
model = train_grammar_model(corpus, n)

# Check the grammar of a sentence
sentence = "The dog running"
check_grammar(sentence, model, n)
