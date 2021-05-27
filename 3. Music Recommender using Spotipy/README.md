
# Music Recommender using Spotipy

![image](https://user-images.githubusercontent.com/81169091/119808387-5c94ab00-bee4-11eb-9347-e4cbd69fe313.png)

### Objective :

- [ ] 1. Webscrape Music sites
- [ ] 2. Use music data to train a model - this will be unsurpervised
- [ ] 3. Use the Spotipy recommender function to recommend music
- [ ] 4. Write a Music Recommender Function

### 1. Webscraping 

- [X] First I webscraped the billboard top 100 
- [X] Put the data into a DataFrame to use it for the Music recommender 

### 2. Machine Learning 

- [X] I got a dataset from kaggle to train the my model.
- [X] I also only use certain features.
- [X] Machine learning model is K-means.
       - [X]   From this i will take the clusters and use it to recommend the music.
       - [X]   The dataset i used had about 130663 song.
       - [X]   scaling the dataset as well
       - [X]   Unsupervised training it to give me the clusters
       - [X]   We have about 5 clusters
       - [X]  **validation**
        ![kmeas](https://user-images.githubusercontent.com/81169091/119847695-7e555880-bf0b-11eb-8b54-234061a5f798.png)
        
- [X] Put the Dataframe back together.

### 3. Spotipy Recommender
 
- [X] using the spotipy API to get songs from Spotify

```
def spotify_query(inp,offs = 0):
    tracks_query = sp.search(str(inp), limit=10, type='track', offset=offs)['tracks']['items']    #queries 10 song names to spotify api
    songs = []
    for track in tracks_query:
        sp_song = track['name']
        sp_artists = ", ".join([artist['name'] for artist in track['artists']])
        sp_id = track['id']
        songs.append((sp_song,sp_artists,sp_id))
    return songs
 ```

  
### 4. Music Recommender
Now I write a function for a user to input a song and then we give them 10 different recommendations

![2021-05-27 (2)](https://user-images.githubusercontent.com/81169091/119849182-b4470c80-bf0c-11eb-81bd-7b2131e22468.png)


![image](https://user-images.githubusercontent.com/81169091/119850533-ed33b100-bf0d-11eb-9907-6804dd38918a.png)


