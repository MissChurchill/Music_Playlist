import requests
import json
import pandas as pd

print("Welcome! You can use this application to create a music playlist")  

while True:
    song=input("What song would you like to add to your playlist?")
    
    if (song.lower() == "quit"):
        print("Thank you for creating your playlist, Enjoy!")
        break # User said to quit in any case; exit the loop

    response = requests.get("https://itunes.apple.com/search?term="+song+"&limit=1")
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

    playlist ={
        "song_name": str((results['trackName'])),
        "musician": str((results['artistName'])),
        "recording":str((results['trackViewUrl'])) }    
    
df = pd.DataFrame(playlist, columns = ['Musician', 'Song Title', 'Link to Song'])
print(df)
