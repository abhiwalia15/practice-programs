import pafy

import youtube_dl

#url of the video
url = 'https://youtu.be/ws1o-N024es?t=1'

# instant created
video = pafy.new(url)

#print title
print(video.title)

#print rating
print(video.rating)

#print viewcount
print(video.viewcount)

#print author and video length
print(video.author , video.length)

#print duration , likes ,dislikes adn description
print(video.duration , video.likes , video.dislikes , video.description)
