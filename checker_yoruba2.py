import re
from collections import Counter


def preprocess_text(text):
    # Remove non-alphabetic characters and convert to lowercase
    # text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

def build_ngrams(text, n):
    words = text.split()
    ngrams = [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
    return ngrams

def train_model(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        preprocessed_text = preprocess_text(text)
        ngrams = build_ngrams(preprocessed_text, n)
        model = Counter(ngrams)
    return model

def check_grammar(sentence, model, n):
    preprocessed_sentence = preprocess_text(sentence)
    sentence_ngrams = build_ngrams(preprocessed_sentence, n)
    for ngram in sentence_ngrams:
        if ngram not in model:
            print("Potential grammar issue: ", ' '.join(ngram))
        else:
            print('No Grammar issue')

# Example usage
file_path = 'bibeli_Mimo.txt'
n = 3  # Set the desired n-gram size
model = train_model(file_path, n)

# Test the grammar checker
test_sentence = input("Enter your sentence: ")
check_grammar(test_sentence, model, n)
