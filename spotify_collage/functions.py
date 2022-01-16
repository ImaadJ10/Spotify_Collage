def search_artist(sp, artist_name):
    url_string = sp.search(q=artist_name, limit=1, offset=0, type='artist', market=None).get('artists').get('items')[0].get('external_urls').get('spotify')
    artist_id = url_string[32:]
    results = sp.artist_top_tracks(artist_id)

    for track in results['tracks']:
        top_tracks = []
        top_tracks.append([[track['name']],track['album']['images'][0]['url']])
        return top_tracks

def trending(sp):
    trending_id = "37i9dQZEVXbMDoHDwVN2tF"
    results = sp.playlist_items(trending_id)
    for track in results['items'][:20]:
        print('track    : ' + track['track']['name'])
        print('artist   : ' + track['track']['album']['artists'][0]['name'])
        print('cover art: ' + track['track']['album']['images'][0]['url'])
        print()


def search_genre(sp, genre_name):
    genres = sp.recommendation_genre_seeds()['genres']
    # genre_name = input("Search for a genre: ")
    if genre_name in genres:
        tracks = sp.recommendations(seed_genres=[genre_name])
        for track in tracks['tracks']:
            print('track    : ' + track['name'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print()
    else:
        print(genres)

def saved_songs(sp):
    results = sp.current_user_saved_tracks()
    saved_artists_and_tracks = []
    saved_pics = []
    saved_links = []

    for idx, item in enumerate(results['items']):
        # track.append(item['track'])
        saved_artists_and_tracks.append(str(item['track']['name']) + " - " + str(item['track']['album']['artists'][0]['name']))
        saved_pics.append(item['track']['album']['images'][0]['url'])
        saved_links.append(item['track']['album']['external_urls']['spotify'])


        # saved_tracks.append(str(item['track']['name']))

        # print(idx, track['artists'][0]['name'], " – ", track['name'])

    diction = {'songsNartists':saved_artists_and_tracks , 'savedPictures':saved_pics , 'savedLinks':saved_links}

    return diction