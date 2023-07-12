import re
from collections import defaultdict

def generate_ngrams(sentence, n):
    words = re.findall(r'\w+', sentence)
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i+n])
        ngrams.append(ngram)
    return ngrams

def train_model(dataset, n):
    model = defaultdict(list)
    with open(dataset, 'r', encoding='utf-8') as file:
        for line in file:
            sentence = line.strip()
            ngrams = generate_ngrams(sentence, n)
            for ngram in ngrams:
                model[ngram].append(sentence)
    return model

def check_grammar(sentence, model, n):
    ngrams = generate_ngrams(sentence, n)
    suggestions = []
    for ngram in ngrams:
        if ngram not in model:
            suggestions.extend(model[ngram])
    return suggestions

# Example usage
dataset_file = 'yo.txt[1]'  # Replace with the path to your dataset file
ngram_size = 1  # Specify the desired n-gram size

model = train_model(dataset_file, ngram_size)

# Example sentence to check grammar
sentence = "Mò ti lọ s ilè"  # Replace with your own sentence

suggestions = check_grammar(sentence, model, ngram_size)

if suggestions:
    print("Possible corrections:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("The sentence appears to be grammatically correct.")
