
# pip3 install gensim==3.8.3
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords



f = open("deleteMe.txt", "r")
this_text = f.read()
f.close()

text = "Hello, people from the future! Welcome to Normalized Nerd! I love to create educational " \
       "videos on Machine Learning and Creative Coding. Machine learning and Data Science have " \
       "changed our world dramatically and will continue to do so. But how they exactly work?.." \
       "Find out with me. If you like my videos please subscribe to my channel."


print(summarize(this_text, ratio=0.2))
print(keywords(this_text, scores=True, lemmatize=True))

