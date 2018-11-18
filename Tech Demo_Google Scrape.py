import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
import re
from nltk.corpus import wordnet as wn
import numpy as np
from nltk.corpus import genesis
from nltk.corpus import wordnet_ic


searchEngineId = "016802530785826462080:dcrmsc81elm"

apiKey = "AIzaSyBS7qVnVRyjFO2bpmIc2lW2IwN8EhtHwDw"

searchKeywords = "cell+phones+buy+important+parameters"

url = "https://www.googleapis.com/customsearch/v1?key=" + \
        apiKey + "&cx=" + searchEngineId + "&q=" + searchKeywords +\
        "&lr=lang_en" #+ "&num=1"

# patterned search keywords: steps+to+buy+the+right+cell+phone

url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyBS7qVnVRyjFO2bpmIc2lW2IwN8EhtHwDw&cx=016802530785826462080:dcrmsc81elm&q=steps+to+buy+the+right+cell+phone&lr=lang_en"

result = urlopen(url)

dataDict = json.load(result)

webUrl = dataDict["items"][0]["link"]

soup = BeautifulSoup(urlopen(webUrl), 'lxml')

text = soup.get_text()

text = re.sub(r'[^\w\s]','',text)

engWords = set(nltk.corpus.words.words()) # this is almost all the english words that NLTK has.

tokenizedText = set(word_tokenize(text)) # separate the text into words and put'em into a list

tokenedEng = engWords & tokenizedText # eliminate non-englihs words

stopWords = set(stopwords.words("english")) # eliminate meaningless words

tokenedEng = tokenedEng - stopWords 

tokenedEng = [w for w in tokenedEng if len(w) > 4] # short words tend not to have strong connections w/ target words

tagged = nltk.pos_tag(tokenedEng)
# Pos Tag List: https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/

nouns = [w[0] for w in tagged if w[1] == "NN"] # eliminating non-Noun words

phone = wn.synset('phone.n.01') # set reference for comparison
# Wordnet and lexicon similarity reference: http://www.nltk.org/howto/wordnet.html

##path_similarity:
# scoreList = []
# pairList = []
# for w in nouns:
# 	if wn.synsets(w):
# 		word = wn.synsets(w)[0]
# 		simScore = wn.path_similarity(phone, word)
# 			if simScore:
# 				simScore = round(simScore, 3)
# 				scoreList.append(simScore)
# 				pairList.append((w, simScore))

# array = np.array(scoreList)
# quarterQuantile = np.percentile(array, 90)
# pairList = [p for p in pairList if p[1] >= quarterQuantile]
# print(pairList)

#wup_similarity: Wu-Palmer Similarity
# scoreList = []
# pairList = []
# for w in nouns:
# 	if wn.synsets(w):
# 		word = wn.synsets(w)[0]
# 		simScore = wn.wup_similarity(phone, word)
# 		if simScore:
# 			simScore = round(simScore, 3)
# 			scoreList.append(simScore)
# 			pairList.append((w, simScore))

# array = np.array(scoreList)
# quarterQuantile = np.percentile(array, 90)
# pairList = [p for p in pairList if p[1] >= quarterQuantile]
# print(pairList)

##lch_similarity: Leacock-Chodorow Similarity
# scoreList = []
# pairList = []
# for w in nouns:
#     if wn.synsets(w):
#         word = wn.synsets(w)[0]
#         try:
#             simScore = wn.lch_similarity(phone, word)
#         except:
#             simScore = 0
#         if simScore:
#             simScore = round(simScore, 3)
#             scoreList.append(simScore)
#             pairList.append((w, simScore))

# array = np.array(scoreList)
# quarterQuantile = np.percentile(array, 90)
# pairList = [p for p in pairList if p[1] >= quarterQuantile]
# print(pairList)





