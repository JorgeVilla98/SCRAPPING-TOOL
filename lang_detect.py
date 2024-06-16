import os
import sys
import pandas as pd
from langdetect import detect

filename = sys.argv[1]

comments_df = pd.read_csv(filename, sep='|')

# Function para detectar el idioma usando el modulo langdetect
def detect_language(comment):
    try:
        return detect(comment)
    except:
        return 'unknown'

# Aplicamos la funcion de detección de idioma a cada comentario y creamos una columna nueva con el idioma
comments_df['Language'] = comments_df['Comment'].apply(detect_language)

# Filtramos y eliminamos los comentarios que no estan en ingles
en_comments_df = comments_df[comments_df['Language'] == 'en']

# Creamos una copia del DataFrame antes de realizar la asignación
en_comments_df_copy = en_comments_df.copy()

# Realizamos la asignación en la copia
en_comments_df_copy['ID'] = en_comments_df_copy.index

# Reorganizamos las columnas para que 'ID' esté al principio
en_comments_df_copy = en_comments_df_copy[['ID'] + [col for col in en_comments_df_copy.columns if col != 'ID']]

en_comments_df_copy.to_csv(filename, sep='|', index=False)

print(f'Lenguaje detectado')
