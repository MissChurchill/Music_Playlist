from unittest import result
import requests
import json
import pandas as pd

print("Welcome! You can use this application to create a music playlist")  

df = pd.DataFrame()

while True:
    song=input("What song would you like to add to your playlist?")
    
    if (song.lower() == "quit"):
        print("Thank you for creating your playlist, Enjoy!")
        break # User said to quit in any case; exit the loop

    response = requests.get("https://itunes.apple.com/search?term="+song+"&limit=1")
    jsonResponse=response.json()
   
    for results in jsonResponse['results']:
        musician =results['artistName']
        title =results['trackName']
        recording =results['trackViewUrl']
        
        print("Artist Name is")
        print(results['artistName'])
        musician =results['artistName']
        print("Collection Name is")
        print(results['collectionName'])
        print("Track Name is")
        print(results['trackName'])
        title =results['trackName']
        print("Genre is")
        print(results['primaryGenreName'])
        print("Here is the album cover")
        print(results['artworkUrl30'])
        print("Here is the link to the song")
        print(results['trackViewUrl'])
        recording =results['trackViewUrl']
       
        playlist ={
        "musician": musician,
        "title": title,
        "recording":recording }   
           
        df = df.append({'musician':musician, 'title':title, 'recording':recording},ignore_index=True)
    
print(df)
