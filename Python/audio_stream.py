import requests

#stream_url = 'https://www.liveatc.net/play/asx/ksan2.asx'
#stream_url = 'https://s1-fmt2.liveatc.net/ksan1_twr?nocache=2021070414143045414'
stream_url = 'https://s1-fmt2.liveatc.net/khuf_twr'
#stream_url = 'https://s1-fmt2.liveatc.net/klax_twr'
stream_url = 'https://s1-fmt2.liveatc.net/phnl1_twr'

r = requests.get(stream_url, stream=True)

#with open('stream.mp3', 'wb') as f:
with open('stream2.wav', 'wb') as f:
      try:
          for block in r.iter_content(1024):
              f.write(block)
              #print(block)
      except KeyboardInterrupt:
          pass
