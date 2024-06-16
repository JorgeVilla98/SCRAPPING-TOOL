import os
import sys
import pandas as pd


directory = os.getcwd()

#Listamos todos los csv en el directorio actual
csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

# Lista vacia en la que iremos almacenando los diferentes datframes
data_frames = []

# Leemos cada csv y concatenamos el dataframe a nuestra lista
for csv_file in csv_files:
    csv_file_path = os.path.join(directory, csv_file)
    df = pd.read_csv(csv_file_path, sep = '|')
    data_frames.append(df)

# Creamos un nuevo Dataframe con nuestra lista de datframes
merged_df = pd.concat(data_frames, ignore_index=True)

# Guardamos nuestro nuevo dataframe en un csv con el nombre del archivo destino
merged_csv_filename = sys.argv[1]
merged_df.to_csv(merged_csv_filename, index=False, sep ='|')

print(f'Todos los comentarios han sido fusionados en {merged_csv_filename}')

# Borramos todos los csv individuales excepto el que hemos usado para fusionar nuestros comentarios
for csv_file in csv_files:
    if csv_file != merged_csv_filename:
        os.remove(os.path.join(directory, csv_file))

print(f'Archivos individuales eliminados (excepto {merged_csv_filename}).')
