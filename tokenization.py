import pandas as pd
import stanza
import sys
import nltk
from nltk.corpus import stopwords

#Usamos stanza para la tokenizacion
stanza.download('en')
nlp = stanza.Pipeline(lang='en', processors='tokenize,lemma')

# Definimos una funcion para realizar la tokenizacion y lematizacion
def tokenize(text):
    
    doc = nlp(text)
    
    # Extraemos los tokens
    tokens = [word.text for sent in doc.sentences for word in sent.tokens]
    return tokens

#funcion para eliminar los stop words de los comentarios, una vez tokenizado el comentario
def remove_stopwords(tokenized_text):
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    filtered_text = [word for word in tokenized_text if word.lower() not in stop_words]
    return filtered_text


#funcion para lematizar los tokens
def lemmatize(tokenized_text):
    doc = nlp(" ".join(tokenized_text))  # Join tokens into a single string
    lemmas = [word.words[0].lemma if word.words else '' for sent in doc.sentences for word in sent.tokens]
    return lemmas


filename = sys.argv[1]
df = pd.read_csv(filename, sep='|')

comments = df['Comment']

# Aplicamos las funciones deifnidas previamente
results = comments.apply(tokenize).apply(remove_stopwords).apply(lemmatize)

# Creamos una nueva columna en la que guardar los lemas
df['TextData'] = results

df.to_csv(filename, sep='|', index=False)

print(f"Tokenizacion,eliminacion de stop words y lematizacion completadas. Resultados guardados en {filename}")
