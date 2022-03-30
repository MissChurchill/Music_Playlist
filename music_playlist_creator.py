import requests
import json

#API source: https://itunes.apple.com
print("Welcome! You can use this application to create a music playlist")  

while True:
    song=input("What song would you like to add to your playlist?")
    response = requests.get('https://itunes.apple.com/search?term='+song+"&limit=1")
    jsonResponse=response.json()

    for results in jsonResponse['results']:
        print("Artist Name is")
        print(results['artistName'])
        print("Collection Name is")
        print(results['collectionName'])
        print("Track Name is")
        print(results['trackName'])
        print("Genre is")
        print(results['primaryGenreName'])
        print("Here is the album cover")
        print(results['artworkUrl30'])
        print("Here is the link to the song")
        print(results['trackViewUrl'])
            
music_array = []
music_array.append(results['trackViewUrl'])

if input == q:
    print ("Thank you for using our app. Enjoy your music playlist")
    exit()
