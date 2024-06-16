import subprocess
import sys
import os

#destFile: nombre del fichero donde queremos guardar los comentarios
#idSourceFile: fichero desde el que extaremos los identificadores de cada video
destFile = sys.argv[1]
idSourceFile = sys.argv[2]

directory = os.getcwd()
#---------------------------------------------
#Borramos todos los archivos .csv existentes
all_files = os.listdir(directory)
csv_files = [file for file in all_files if file.endswith(".csv")]
for csv_file in csv_files:
    os.remove(os.path.join(directory, csv_file))
    print(f'Deleted: {csv_file}')
#-----------------------------------------------
# Leemos cada ID del video y extraemos la informacion de este
with open(idSourceFile, 'r') as file:
    video_ids = [line.strip() for line in file]
for video_id in video_ids:
    # Utilizamos el script yt_scrapper para extraer los comentarios
    scrape_command = ["python", "yt_scrapper.py", video_id]
    subprocess.run(scrape_command)

print("Todos los comentarios han sido extraidos")
#------------------------------------------------
#Combinamos todos los csv de cada video en uno unico
merge_command = ["python", "csv_merger.py", destFile]
subprocess.run(merge_command)
#Limpiamos y formateamos el csv de comentarios
clean_command = ["python", "pre_text.py", destFile]
subprocess.run(clean_command)
#Detectamos el idioma de cada comentario y eliminamos los que no son en ingles
detect_command = ["python", "lang_detect.py", destFile]
subprocess.run(detect_command)
#Analizamos el sentimiento de cada comentario
sentiment_command = ["python", "sentiment.py", destFile]
subprocess.run(sentiment_command)
#Tokenizamos y lematizamos los comentarios
tokenization_command = ["python", "tokenization.py", destFile]
subprocess.run(tokenization_command)


