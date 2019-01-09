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

#function for remove stopword
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

print(applystemmer(data))
