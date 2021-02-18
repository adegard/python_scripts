import pafy
url="https://www.youtube.com/watch?v=nfWlot6h_JM"
video=pafy.new(url)
video.title
audiostreams=video.audiostreams
audiostreams[1].download()
