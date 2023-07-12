import nltk

# Dataset
yoruba_sentences = [
    "Mo ti lo si ile",
    "O seun ti lo si ile",
    "Iya mi nlo si ile",
    "Awon omo yin nlo si ile",
    # Add more Yoruba sentences from your dataset
]

# Preprocess the dataset
preprocessed_sentences = []
for sentence in yoruba_sentences:
    preprocessed_sentences.append(nltk.word_tokenize(sentence))

# Function to generate n-grams
def generate_ngrams(sentence, n):
    ngrams = []
    for i in range(len(sentence) - n + 1):
        ngrams.append(tuple(sentence[i:i+n]))
    return ngrams

# Build n-grams model
n = 3  # Specify the value of n for n-grams (can be adjusted)
ngrams_model = []
for sentence in preprocessed_sentences:
    ngrams_model += generate_ngrams(sentence, n)

# Function to check Yoruba grammar using n-grams
def check_yoruba_grammar(text):
    tokens = nltk.word_tokenize(text)
    ngrams = generate_ngrams(tokens, n)
    
    for ngram in ngrams:
        if ngram not in ngrams_model:
            return False
    return True

# Example usage
sentence_to_check = "Awon yin nlo si ile"
if check_yoruba_grammar(sentence_to_check):
    print("Yoruba grammar is correct.")
else:
    print("Yoruba grammar contains errors.")
