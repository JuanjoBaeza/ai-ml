import pdftotext
from collections import Counter
import pandas as pd
import nltk
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

def main():

    # Load your PDF
    with open("datasets/libro.pdf", "rb") as f:
        pdf_page = pdftotext.PDF(f)     # pdf son las páginas

    #print(len(pdf_page))     # Numero de paginas

    text_list = []
    
    for page in pdf_page:     # Iterate over all the pages
        text_list.append(page.replace("\n", " "))

    #print(text_list)         # Creamos una lista con todas las páginas del libro

    text_var = ' '  
    
    for x in text_list:       # Replace chars not wanted
        text_var += ' ' + x
    
    text_var = text_var.replace("—", "")
    text_var = text_var.replace(".", "")
    text_var = text_var.replace("!", "")
    text_var = text_var.replace("¡", "")
    text_var = text_var.replace("?", "")
    text_var = text_var.replace("¿", "")
    text_var = text_var.replace(",", "")
    text_var = text_var.replace(":", "")
    text_var = text_var.replace(";", "")
    text_var = text_var.replace("(", "")
    text_var = text_var.replace(")", "")
    text_var = text_var.replace("[", "")
    text_var = text_var.replace("]", "")
    text_var = text_var.replace("http//", "")
    text_var = text_var.replace("http://", "")
    text_var = text_var.replace("@", "")
    text_var = text_var.replace("c/", "")
    text_var = text_var.lower()
    
    preprocess_text(text_var)

    text = text_var.split()               # Convertimos la variable tipo string text_var con todas las palabras del libro en una lista aplicando split

    print("Extracto de la lista(20): ")   # El libro ya en una var tipo string
    print(Most_Common(text))

    print("\nTamaño del libro en palabras: ", len(text))
    
    frequency_distribution = nltk.FreqDist(text) 
    print("La frecuencia de distribución es: " ,frequency_distribution)
    
    most_common_element = frequency_distribution.max()
    print ("Palabra mas común: " ,most_common_element)

    #print ("Palabras: " ,text)

    word_counts = Counter(text) # Contamos la frecuencia de aparicion de las palabras
    print(word_counts)

    lista_unica = set(text)  # Eliminamos las palabras repetidas convirtiendolo en un sret
    new_text = list(lista_unica) # Volvemos a convertir el set en una lista
    print("Después de eliminar duplicados: ", len(new_text))
    print("Texto final: ", new_text)

    

def Most_Common(text):
    data = Counter(text)
    return data.most_common(20)

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