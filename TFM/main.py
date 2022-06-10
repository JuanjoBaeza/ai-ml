import pdftotext
from collections import Counter
import nltk

def main():

    # Load your PDF
    with open("datasets/libro.pdf", "rb") as f:
        pdf_page = pdftotext.PDF(f)             # pdf son las páginas

    #print(len(pdf_page))                       # Numero de paginas

    text_list = []
    # Iterate over all the pages
    for page in pdf_page:
        text_list.append(page.replace("\n", " "))

    #print(text_list)                          # Creamos una lista con todas las páginas del libro

    text_var = ' '  
    # Replace chars not wanted
    for x in text_list:
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
    text_var = text_var.replace("http//", "")
    text_var = text_var.replace("http://", "")
    text_var = text_var.replace("@", "")
    text_var = text_var.replace("c/", "")
    text_var = text_var.lower()
    
    text = text_var.split()               # Convertimos la variable tipo string text_var con todas las palabras del libro en una lista aplicando split

    print("Extracto de la lista(20): ")                          # El libro ya en una var tipo string
    print(Most_Common(text))

    print("\nTamaño del libro en palabras: ", len(text))
    
    frequency_distribution = nltk.FreqDist(text) 
    print("La frecuencia de distribución es: " ,frequency_distribution)
    
    most_common_element = frequency_distribution.max()
    print ("Palabra mas común: " ,most_common_element)

def Most_Common(text):
    data = Counter(text)
    return data.most_common(20)

if __name__ == "__main__":
    main()