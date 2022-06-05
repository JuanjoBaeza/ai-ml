import numpy as np
import matplotlib.pyplot as plt

text = "y déjale el lugar a otro más valiente que tú shandon tenía esperanzas de que en el último momento recibiría instrucciones precisas sobre el objeto del viaje y que sería el capitán del barco todos los tripulantes profesaban la religión protestante en los largos viajes la oración en común y la lectura de la biblia tienden a unir los ánimos y asentarlos en las horas de decaimiento shandon conocía por experiencia la utilidad de estas prácticas y su influencia sobre la moral de una tripulación una vez reclutados los marineros shandon y sus dos ofíciales se ocuparon de las provisiones siguieron estrictamente las instrucciones del"

def get_num_words_per_sample(text):
    """Returns the median number of words per sample given corpus.

    # Arguments
        sample_texts: list, sample texts.

    # Returns
        int, median number of words per sample.
    """
    num_words = [len(s.split()) for s in text]
    return np.median(num_words)

def plot_sample_length_distribution(text):
    """Plots the sample length distribution.

    # Arguments
        samples_texts: list, sample texts.
    """
    plt.hist([len(s) for s in text], 50)
    plt.xlabel('Length of a sample')
    plt.ylabel('Number of samples')
    plt.title('Sample length distribution')
    plt.show()

print("Palabras(samples):", len(text))

get_num_words_per_sample(text)
plot_sample_length_distribution(text)