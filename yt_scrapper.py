import pandas as pd
import requests
import sys

api_key = 'AIzaSyCut7GWauHbjoyDGxYYJT8MzTyjW1TSwdw'

#Identificador del video 
video_id = sys.argv[1]

#YouTube Data API endpoint
api_endpoint = f'https://www.googleapis.com/youtube/v3/commentThreads'

#Nuestros datos de comentarios incialmente contendran el nombre de usuario, el comentario en si y el numero de likes
comment_data = {
    'User': [],
    'Comment': [],
    'Likes': [],
}

#Parametros para la API
params = {
    'part': 'snippet,replies',
    'videoId': video_id,
    'key': api_key,
    'maxResults': 3000, 
}

next_page_token = None

while True:
    if next_page_token:
        params['pageToken'] = next_page_token

    response = requests.get(api_endpoint, params=params)
    data = response.json()

    for item in data['items']:
        snippet = item['snippet']['topLevelComment']['snippet']
        comment_data['User'].append(snippet['authorDisplayName'])
        comment_data['Comment'].append(snippet['textDisplay'])
        comment_data['Likes'].append(snippet['likeCount'])

    next_page_token = data.get('nextPageToken')

    if not next_page_token:
        break

# Creamos el DataFrame
df = pd.DataFrame(comment_data)

#Guardamos el dataframe en un CSV. Como nuestros comentarios pueden tener comas, nuestro separador sera |
csv_filename = f"{video_id}_comments.csv"
df.to_csv(csv_filename, sep = '|', index=False)

print(f"Datos guardados en {csv_filename}")
