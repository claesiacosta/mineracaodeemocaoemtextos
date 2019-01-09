import nltk

#nltk.download()

data = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

#manual stopwords
stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

#nltk function implemented - stopwords
stopwordsnltk = nltk.corpus.stopwords.words("portuguese")
#print(stopwordsnltk)

#stopwords removal
def removestopword(text):
	phrases = []

	for(words, emotion) in  text:
		withoutstop = [p for p in words.split() if p not in stopwordsnltk]
		phrases.append((withoutstop, emotion))

	return phrases

#print(removestopword(data))

#function for remove stem
def applystemmer(text):
	stemmer = nltk.stem.RSLPStemmer()
	stemmingphrases = []
	for (words, emotion) in text:
		withstemming = [str(stemmer.stem(p)) for p in words.split() if p not in stopwordsnltk]
		stemmingphrases.append((withstemming, emotion))
	return stemmingphrases

phraseswithstemming = applystemmer(data)
#print(phraseswithstemming)

#listing of all words
def searchwords(phrases):
	allwords = []
	for (words, emotion) in phrases:
		allwords.extend(words)
	return allwords

words = searchwords(phraseswithstemming)
print(words)

#single word extraction
def searchfrequency(words):
	words = nltk.FreqDist(words)
	return words

frequency = searchfrequency(words)
#print(frequency.most_common(50))

#print unique words/once
def searchuniquewords(frequency):
	freq = frequency.keys()
	return freq

uniquewords = searchuniquewords(frequency)
print(uniquewords)

#extraction of words from each sentence
def wordsextractor(document):
	doc = set(document)
	features = {}
	for words in uniquewords:
		features['%s' % words] = (words in doc)

	return features

featuresphrases = wordsextractor(['am','nov', 'dia'])

print(featuresphrases)