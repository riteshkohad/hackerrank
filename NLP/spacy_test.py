import spacy
import en_core_web_sm
from spacy import displacy
from spacy.lang.en.stop_words import STOP_WORDS

f = open("../deleteMe.txt", "r")
this_text = f.read()
f.close()

nlp = spacy.load("en_core_web_sm")
document1 = nlp("I am learning natural language processing. The course is in London")

# doc_2 = nlp(this_text)
#
# for token in doc_2:
# 	print(f"{token.text} - {token.pos_}")

text = "IBM is a US company on information technology. It is located in San Francisco and revenue in " \
       "2018 was approximately 320 billion dollars"

doc3 = nlp(text)

# list out entities like Organization or Geo location or Name etc
# for ent in doc3.ents:
# 	print(f"{ent.text} -> {ent.label_}")

# print(STOP_WORDS)

origin = doc3[4]

print(origin.ancestors)
