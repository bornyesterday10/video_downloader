import m3u8, requests, os

# Local storage folder
localfolder = r'B:\Share\AJMovies\Softie'
# Chunks to use-- 128 should be fine
chunk_size = 128
# Target m3u8 to download
infile = r'https://ga.video.cdn.pbs.org/videos/pov/cb46ad08-0220-4158-9401-c32b84ac14eb/2000199277/hd-16x9-mezzanine-1080p/amdo3312-hls-16x9-1080p-540p-2000k.m3u8'

# TODO: A Good Test Site: https://www.aljazeera.com/program/people-power/2020/9/24/bureau-39-cash-for-kim/
# TODO: Another Good Test Site: https://www.pbs.org/pov/watch/softie/video-softie/

# From https://video.stackexchange.com/questions/10730/combine-video-and-audio-ts-segments-coming-from-hls-stream
# ffmpeg -i <audio-stream> -i <video-stream> -async 1 -c copy test.m3u8

# https://www.streamingmedia.com/Articles/Editorial/What-Is-.../What-Is-HLS-(HTTP-Live-Streaming)-78221.aspx?utm_source=related_articles&utm_medium=gutenberg&utm_campaign=editors_selection
# https://www.akamai.com/us/en/products/media-delivery/
# https://www.streamingmedia.com/Articles/Editorial/Featured-Articles/How-to-Encode-Video-for-the-iPad-iPhone-and-iPod-Touch-75899.aspx

# Cute: https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=139529

localfile = os.path.join(localfolder,'local.m3u8')

#infile = r"B:\Share\AJMovies\DarkSideGreenEnergy\rendition.m3u8"

fr = requests.get(infile)
with open(localfile,'wb') as m:
    for chunk in fr.iter_content(chunk_size=chunk_size):
        m.write(chunk)
localpl = m3u8.load(localfile)

print()

for num,segment in enumerate(localpl.segments):
    uri = segment.uri
    fullpath = 'https://ga.video.cdn.pbs.org/videos/pov/cb46ad08-0220-4158-9401-c32b84ac14eb/2000199277/hd-16x9-mezzanine-1080p/' + uri
    print(uri)
    r = requests.get(fullpath)
    #print(tmp)
    with open(os.path.join(localfolder,str(num)+'.ts'),'wb') as outfile:
        for chunk in r.iter_content(chunk_size=chunk_size):
            outfile.write(chunk)
    print('\t\t\t...Done')
    print()