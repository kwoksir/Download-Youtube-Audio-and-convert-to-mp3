from pytube import YouTube
from pydub import AudioSegment
path = 'download'
yt = YouTube(input("Enter YouTube URL: "))
yt.streams.filter(mime_type='audio/mp4',only_audio=True).first().download(path)
print("Download is completed.")
print("Convert to mp3....")
t = yt.title
f = path + "/" + t
a = AudioSegment.from_file(f+".mp4", format="mp4")
a.export(f+".mp3",format="mp3")
print("Conversion is completed.")
