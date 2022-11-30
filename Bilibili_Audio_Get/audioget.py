import requests
import json
import os

null = None
headers = {'User-Agent': 'bilibili Security Browser Edg/87.0.4280.88'}
list_api = 'https://api.bilibili.com/audio/music-service-c/menus/'
song_api = 'https://api.bilibili.com/audio/music-service-c/url?mid=6433840&mobi_app=iphone&platform=ios&privilege=2&quality=2&songid='



def getsong(id):
    song_info = json.loads(requests.get(song_api+str(id)).text)['data']
    song_title = song_info['title']
    song_url = song_info['cdns'][0]
    song_content = requests.get(song_url, headers=headers).content
    return [song_title,song_content]

def getlist(id):
    respons = requests.get(list_api+str(id), headers=headers)
    list_info = json.loads(respons.text)['data']
    list_title = list_info["menusRespones"]["title"]
    list_cover = list_info["menusRespones"]["coverUrl"]
    songslist = list_info['songsList']
    return[list_title,list_cover,songslist]

def getcover(id):
    cover_content = requests.get(getlist(id)[1], headers=headers).content
    return cover_content

def savelist(id):
    
    list_get = getlist(id)
    
    if os.path.exists(list_get[0]):
        pass
    else:
        os.mkdir(list_get[0])
    
    if os.name == 'posix':
        with open(list_get[0]+'/'+'cover.jpg','wb') as cover:
            cover.write(getcover(id))
        
        for each_song in list_get[2]:
            song_id = each_song['id']
            song_get = getsong(song_id)
            with open(list_get[0]+'/'+song_get[0]+'.m4a','wb') as song:
                song.write(song_get[1])
    else:
        with open(list_get[0]+'\\'+'cover.jpg','wb') as cover:
            cover.write(getcover(id))
        
        for each_song in list_get[2]:
            song_id = each_song['id']
            song_get = getsong(song_id)
            with open(list_get[0]+'\\'+song_get[0]+'.m4a','wb') as song:
                song.write(song_get[1])

def savesong(id):
    
    song_get = getsong(id)
    
    with open(song_get[0]+'.m4a','wb') as song:
        song.write(song_get[1])
