import pdftotext

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
    
    text = text_var.split() 

    #print(text)                           # El libro ya en una var tipo string
    print(len(text))                       # Numero de palabras del documento

if __name__ == "__main__":
    main()