import m3u8, requests

# TODO: A Good Test Site: https://www.aljazeera.com/program/people-power/2020/9/24/bureau-39-cash-for-kim/

# From https://video.stackexchange.com/questions/10730/combine-video-and-audio-ts-segments-coming-from-hls-stream
# ffmpeg -i <audio-stream> -i <video-stream> -async 1 -c copy test.m3u8

# https://www.streamingmedia.com/Articles/Editorial/What-Is-.../What-Is-HLS-(HTTP-Live-Streaming)-78221.aspx?utm_source=related_articles&utm_medium=gutenberg&utm_campaign=editors_selection
# https://www.akamai.com/us/en/products/media-delivery/
# https://www.streamingmedia.com/Articles/Editorial/Featured-Articles/How-to-Encode-Video-for-the-iPad-iPhone-and-iPod-Touch-75899.aspx

# Cute: https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=139529

# Target m3u8 to download
#infile = r"B:\Share\AJMovies\DarkSideGreenEnergy\rendition.m3u8"
infile = r"B:\Share\AJMovies\DarkSideGreenEnergy\rendition(1).m3u8"
localpl = m3u8.load(infile)

#fileprefix = 'left'
fileprefix = 'right'
chunk_size = 128

print()

for num,segment in enumerate(localpl.segments):
    uri = segment.absolute_uri
    print(uri)
    r = requests.get(uri)
    #print(tmp)
    with open(fileprefix+str(num)+'.ts','wb') as outfile:
        for chunk in r.iter_content(chunk_size=chunk_size):
            outfile.write(chunk)
    print('\t\t\t...Done')
    print()
