import m3u8
import requests
import subprocess

#url = 'https://videos-3.earthcam.com/fecnetwork/20288.flv/chunklist_w572133256.m3u8'
url = 'http://s52.ipcamlive.com/streams/34ea8tvqxf3kngghf/'
#url = 'https://wms-prod-1.wetmet.net/live/174-01-01/'
#url = 'https://wms-prod-1.wetmet.net/live/174-02-01/'

m3u8_file = 'stream.m3u8'
#m3u8_file = 'chunks.m3u8'

r = requests.get(url + m3u8_file)

print(r.text)

m3u8_master = m3u8.loads(r.text)

print(m3u8_master.data)

#playlist_url = m3u8_master.data['playlists'][0]['uri']

#r = requests.get(playlist_url)

#playlist = m3u8.loads(r.text)

#print('https://videos-3.earthcam.com/fecnetwork/20288.flv/' + m3u8_master.data['segments'][0]['uri'])
print(url + m3u8_master.data['segments'][0]['uri'])

length = len(m3u8_master.data['segments'])
media_sequence = m3u8_master.data['media_sequence']

print(length)
print(media_sequence)

#r = requests.get('https://videos-3.earthcam.com/fecnetwork/20288.flv/' + m3u8_master.data['segments'][0]['uri'])
r = requests.get(url + m3u8_master.data['segments'][0]['uri'])

with open("video4.ts", 'wb') as f:
    for segment in m3u8_master.data['segments']:
        #url = 'https://videos-3.earthcam.com/fecnetwork/20288.flv/' + segment['uri']
        r = requests.get(url + segment['uri'])
        f.write(r.content)

    r = requests.get(url + m3u8_file)
    print(r.text)
    m3u8_master = m3u8.loads(r.text)
    print(m3u8_master.data)
    if (m3u8_master.data['media_sequence'] - media_sequence < length):
        #overlap
        start_index = len(m3u8_master.data['segments']) - (m3u8_master.data['media_sequence'] - media_sequence)
    else:
        start_index = 0
    for i in range(start_index, len(m3u8_master.data['segments'])):
        r = requests.get(url + m3u8_master.data['segments'][i]['uri'])
        f.write(r.content)

#subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])
