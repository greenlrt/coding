import requests

#stream_url = 'https://www.liveatc.net/play/asx/ksan2.asx'
stream_url = 'https://s1-fmt2.liveatc.net/ksan1_twr?nocache=2021070414143045414'

r = requests.get(stream_url, stream=True)

#with open('stream.mp3', 'wb') as f:
with open('stream.wav', 'wb') as f:
      try:
          for block in r.iter_content(1024):
              f.write(block)
              #print(block)
      except KeyboardInterrupt:
          pass
