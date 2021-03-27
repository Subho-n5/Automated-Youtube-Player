'''
Libraries needed:
python-vlc,pafy,pyaudio,ytdl (needed as sudo using pip)
For further problems and libraries refer documentation of each
'''


import vlc
import pafy
import re
import urllib.request
import time

def player(url):
	video = pafy.new(url)
	best = video.getbest()
	media = vlc.MediaPlayer(best.url)
	media.play()
	time.sleep(1000)
	#media.stop()

def link(keyword):
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + keyword)
	video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	utube_link = "https://www.youtube.com/watch?v=" + video_id[0]
	return utube_link

def key_generator(key):
	key = key.strip().split()
	tem = key[0]
	for i in range(1,len(key)):
		tem = tem + '+' + key[i]
	return tem

search = key_generator(input("Enter!\n"))
url = link(search)
player(url)
