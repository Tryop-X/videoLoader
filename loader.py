from youtube_transcript_api import YouTubeTranscriptApi
from models import video as vid
from serviceDB import videoRepository
import json

with open('listaVideos.txt', 'r') as file:
    urls = file.readlines()

urls = [url.strip() for url in urls]

videos = []
videos_fail = []


def get_transcription(transcript_list):
    for t in transcript_list:
        return t


for url in urls:
    try:
        id_url = url.split('&')[0].split('?v=')[1]
        transcriptions = []

        transcript_list = YouTubeTranscriptApi.list_transcripts(id_url)

        transcript = None
        for t in transcript_list:
            transcript = t.fetch()
            break

        for entry in transcript:
            content = vid.Contenido(start=entry['start'], content=entry['text'], end=entry['duration'])
            transcriptions.append(content)
        video = vid.Video(url=url, transcription=transcriptions, description=[], resume='no data', category='no data')
        videos.append(video)
    except Exception as e:
        print(e, '<---[ERROR]---')
        videos_fail.append(url)
        continue

# json_videos = json.dumps([video.to_dict() for video in videos], indent=4)
db_conn = videoRepository.DataBaseConnection(database_name="videoCollection", collection_name="video")
db_conn.insert_videos(videos=videos)
db_conn.close()
