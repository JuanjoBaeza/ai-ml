from sklearn.feature_extraction.text import TfidfVectorizer
Document1= "It is going to rain today."
Document2= "Today I am not going outside."
Document3= "I am going to watch the season premiere."
Doc = [Document1 ,
       Document2 , 
       Document3]
print(Doc)
['It is going to rain today.', 'Today I am not going outside.', 'I am going to watch the season premiere.']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(Doc)
analyze = vectorizer.build_analyzer()

print('Document 1',analyze(Document1))

print('Document 2',analyze(Document2))

print('Document 3',analyze(Document3))

print('Document transform',X.toarray())