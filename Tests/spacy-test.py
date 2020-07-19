import spacy
import sys

# Load the spacy model that you have installed
nlp = spacy.load('en_core_web_md')
sentence = ' '.join(sys.argv[2:])

# process a sentence using the model
doc = nlp(sentence)

# It's that simple - all of the vectors and words are assigned after this point
# Get the vector for 'text':
print(doc[0],doc[0].vector)

# Get the mean vector for the entire sentence (useful for sentence classification etc.)
print(doc.vector)
