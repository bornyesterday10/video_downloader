import m3u8, requests

infile = r"B:\Share\AJMovies\DarkSideGreenEnergy\rendition.m3u8"

#outfile = r'out-'

localpl = m3u8.load(infile)
#print(localpl.segments)
#print(localpl.target_duration)
#print(localpl.keys)

print()

#for cnt,playlist in enumerate(localpl.playlists):
#    print(playlist.uri)
#    print(playlist.stream_info)
#    #with open(outfile+str(cnt)+'.ts','wb') as writefile:
#    #    writefile.write(playlist.media)
#    #print(playlist.media[0])
#    print()

for num,segment in enumerate(localpl.segments):
    uri = segment.absolute_uri
    print(uri)
    r = requests.get(uri)
    #print(tmp)
    with open('left'+str(num)+'.ts','wb') as outfile:
        for chunk in r.iter_content(chunk_size=128):
            outfile.write(chunk)
    print('\t\t\t...Done')
    print()
