import m3u8
import requests
import subprocess

#url = 'https://videos-3.earthcam.com/fecnetwork/20288.flv/chunklist_w572133256.m3u8'
url = 'http://s52.ipcamlive.com/streams/34ny8mfzjmlablvi6/stream.m3u8'

r = requests.get(url)

m3u8_master = m3u8.loads(r.text)

#print(m3u8_master.data)

#playlist_url = m3u8_master.data['playlists'][0]['uri']

#r = requests.get(playlist_url)

#playlist = m3u8.loads(r.text)

#print('https://videos-3.earthcam.com/fecnetwork/20288.flv/' + m3u8_master.data['segments'][0]['uri'])
print('http://s52.ipcamlive.com/streams/34ny8mfzjmlablvi6/' + m3u8_master.data['segments'][0]['uri'])

#r = requests.get('https://videos-3.earthcam.com/fecnetwork/20288.flv/' + m3u8_master.data['segments'][0]['uri'])
r = requests.get('http://s52.ipcamlive.com/streams/34ny8mfzjmlablvi6/' + m3u8_master.data['segments'][0]['uri'])

with open("video.ts", 'wb') as f:
    for segment in m3u8_master.data['segments']:
        #url = 'https://videos-3.earthcam.com/fecnetwork/20288.flv/' + segment['uri']
        url = 'http://s52.ipcamlive.com/streams/34ny8mfzjmlablvi6/' + segment['uri']
        r = requests.get(url)
        f.write(r.content)

subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])
