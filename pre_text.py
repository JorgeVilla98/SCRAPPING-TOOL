import pandas as pd
import html
import re
import sys

filename = sys.argv[1]

df = pd.read_csv(filename ,sep ='|')

# Funcion para formatear nuestro texto
def clean_and_format_comment(comment):
    if isinstance(comment, str):
        # ELiminamos las marcas de tiempo
        comment = re.sub(r'\d+:\d+', '', comment)
        # Eliminamos etiquetas de tiempo
        comment = html.unescape(re.sub(r'<[^>]+>', '', comment))
        # Eliminamos emoticonos 
        comment = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U0001F004-\U0001F0CF\U0001F18E\U0001F191-\U0001F251❤]+', '', comment)
    return comment

# Aplicamos la funcion a todos los comentarios del dataframe
df['Comment'] = df['Comment'].apply(clean_and_format_comment)

# Convertimos todo a minusculas
df['Comment'] = df['Comment'].str.lower()

# Eliminamos comillas para evitar problemas de formatos
df['Comment'] = df['Comment'].str.replace('"', '')

df.to_csv(filename, index=False, sep='|')

print(f'Datos formateado y guardados en {filename}')
