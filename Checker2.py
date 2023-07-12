import nltk
from nltk.util import ngrams

# Load your specific dataset
dataset = [
    "This is a test sentence"
    ]  # Your dataset goes here

# Create n-grams from the dataset
n = 1  # Choose the desired value of n for your n-grams
ngram_model = list(ngrams(dataset, n))

def check_grammar(sentence):
    words = nltk.word_tokenize(sentence)
    sentence_ngrams = list(ngrams(words, n))

    if sentence_ngrams in ngram_model:
        return "Grammar is correct!"
    else:
        return "Possible grammar error!"

# Example usage
sentence = "This is a test sentence"
result = check_grammar(sentence)
print(result)
