import fitz
from collections import Counter
import nltk
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

def main():

    filepath = "datasets/libro.pdf"

    texto_str  = get_text(filepath)         # texto es un string
    texto_list = preprocess_text(texto_str) # new_texto es una lista
    frequency_distribution = nltk.FreqDist(texto_list)
    most_common_element    = frequency_distribution.max()
    
    word_counts = Counter(texto_list)       # Frecuencia de aparicion de las palabras
    clean(texto_str)                        # Limpiamos caracteres no deseados  

    # print(type(texto_str))
    # print(type(texto_list))
    # print(texto_str)
    # print(texto_list)
    # print("\nPalabra mas común: ", most_common_element)    
    # print("\nExtracto de la lista Top Ten: ", Most_Common(texto_list))
    # print("\nTamaño del libro en palabras: ", len(texto_list))
    # print("\nFrecuencia de aparición: ", word_counts)

    tf_idf(texto_str, texto_list) # Aplicamos TF-IDF

def tf_idf(texto_str, texto_list):

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texto_list)
    analyze = vectorizer.build_analyzer()

    print("Documento: ",analyze(texto_str))
    print("Documento transformado: ", X.toarray())
    print("Caracteristicas del texto: ", vectorizer.get_feature_names())


def clean(texto_str):
    text_clean = ' '  
    
    for x in texto_str:       # Replace chars not wanted
        text_clean += ' ' + x
    
    text_clean = text_clean.replace("—", "")
    text_clean = text_clean.replace(".", "")
    text_clean = text_clean.replace("!", "")
    text_clean = text_clean.replace("¡", "")
    text_clean = text_clean.replace("?", "")
    text_clean = text_clean.replace("¿", "")
    text_clean = text_clean.replace(",", "")
    text_clean = text_clean.replace(":", "")
    text_clean = text_clean.replace(";", "")
    text_clean = text_clean.replace("(", "")
    text_clean = text_clean.replace(")", "")
    text_clean = text_clean.replace("[", "")
    text_clean = text_clean.replace("]", "")
    text_clean = text_clean.replace("http//", "")
    text_clean = text_clean.replace("http://", "")
    text_clean = text_clean.replace("@", "")
    text_clean = text_clean.replace("c/", "")
    text_clean = text_clean.replace("«", "")
    text_clean = text_clean.replace("»", "")
    text_clean = text_clean.lower()

    return text_clean

def get_text(filepath: str) -> str:
    with fitz.open(filepath) as doc:
        text = ""
        for page in doc:
            text += page.get_text().strip()
        return text

def Most_Common(text):
    data = Counter(text)
    return data.most_common(10)

def preprocess_text(text):
    # Tokenise words while ignoring punctuation
    tokeniser = RegexpTokenizer(r'\w+')
    tokens = tokeniser.tokenize(text)
    
    # Lowercase and lemmatise 
    lemmatiser = WordNetLemmatizer()
    lemmas = [lemmatiser.lemmatize(token.lower(), pos='v') for token in tokens]
    
    # Remove stopwords
    keywords= [lemma for lemma in lemmas if lemma not in stopwords.words('english')]
    return keywords

if __name__ == "__main__":
    main()