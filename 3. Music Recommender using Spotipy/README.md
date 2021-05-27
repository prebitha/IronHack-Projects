
# Music Recommender using Spotipy API
### WEBSCRAPPING | MACHINELEARNING | API

![image](https://user-images.githubusercontent.com/81169091/119850533-ed33b100-bf0d-11eb-9907-6804dd38918a.png)

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


    - 1.From this i will take the clusters and use it to recommend the music.
    - 2. The dataset i used had about 130663 song.
    - 3. scaling the dataset as well
    - 4.  Unsupervised training it to give me the clusters
    - 5.  We have about 5 clusters
    
    
  **validation**  ![kmeas](https://user-images.githubusercontent.com/81169091/119847695-7e555880-bf0b-11eb-8b54-234061a5f798.png)
        
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

Hmm yes I do like Chasing After You | Ryan Hurd With Maren Morris 

### CONCLUSION:

My Function does have some glitches, I keep working on it and thats why you will find me updating this on a weekly basis.

ok bye !!
![Alt Text](https://theikondesign.files.wordpress.com/2021/01/1e91b53e-4aab-4d8a-8d6b-8768550e95e9.gif)



