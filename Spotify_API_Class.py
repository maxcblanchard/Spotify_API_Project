import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import pandas

# My Spotify Developer API id and key
client_id = 'fdb778fb2ac648489fec11c10f331937'
client_secret = '27acaaaefda14305941ba37cb661cae1'

# Connecting my client id and secret to Spotify's API
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class Spotify:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.id_list = []

    def get_track_ids(self):
        self.id_list = []
        results = sp.playlist_tracks(self.playlist_id)
        songs = results['items']
        while results['next']:
            results = sp.next(results)
            songs.extend(results['items'])
        for i in songs:
            song = i['track']
            self.id_list.append(song['id'])
        return self.id_list

    def get_track_features(self, track_list):
        track_info = sp.track(track_list)
        track_feature = sp.audio_features(track_list)

        name = track_info['name']
        length = track_info['duration_ms']
        artists = track_info['artists'][0]['name']
        explicit = track_info['explicit']
        popularity = track_info['popularity']

        acousticness = track_feature[0]['acousticness']
        danceability = track_feature[0]['danceability']
        energy = track_feature[0]['energy']
        instrumentalness = track_feature[0]['instrumentalness']
        liveness = track_feature[0]['liveness']
        loudness = track_feature[0]['loudness']
        valence = track_feature[0]['valence']
        speechiness = track_feature[0]['speechiness']
        tempo = track_feature[0]['tempo']
        time_signature = track_feature[0]['time_signature']

        features_info = [name, length, artists, explicit, popularity, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness,
                         valence, tempo, time_signature]

        return features_info

    def duration_calc(self, tracks):
        total_duration = 0
        for i in range(len(tracks)):
            total_duration += tracks[i][1]
        average_duration = (total_duration/len(tracks))/1000
        return average_duration

    def artist_list(self, tracks):
        artist_list = []
        for i in range(len(tracks)):
            artist_list.append(tracks[i][2])
        return artist_list

    def explicit_calc(self, tracks):
        explicit_count = 0
        for i in range(len(tracks)):
            explicit_count += tracks[i][3]
        return explicit_count

    def popularity_calc(self, tracks):
        total_popularity = 0
        for i in range(len(tracks)):
            total_popularity += tracks[i][4]
        return total_popularity

    def acoustincess_calc(self, tracks):
        total_acousticness = 0
        for i in range(len(tracks)):
            total_acousticness += tracks[i][5]
        average_acousticness = total_acousticness / len(tracks)
        return average_acousticness

    def danceability_calc(self, tracks):
        total_danceability = 0
        for i in range(len(tracks)):
            total_danceability += tracks[i][6]
        average_danceability = total_danceability / len(tracks)
        return average_danceability

    def energy_calc(self, tracks):
        total_energy = 0
        for i in range(len(tracks)):
            total_energy += tracks[i][7]
        average_energy = total_energy / len(tracks)
        return average_energy

    def instrumentalness_calc(self, tracks):
        total_instrumentalness = 0
        for i in range(len(tracks)):
            total_instrumentalness += tracks[i][8]
        average_instrumentalness = total_instrumentalness / len(tracks)
        return average_instrumentalness

    def liveness_calc(self, tracks):
        total_liveness = 0
        for i in range(len(tracks)):
            total_liveness += tracks[i][9]
        average_liveness = total_liveness / len(tracks)
        return average_liveness

    def loudness_calc(self, tracks):
        total_loudness = 0
        for i in range(len(tracks)):
            total_loudness += tracks[i][10]
        average_loudness = total_loudness / len(tracks)
        return average_loudness

    def valence_calc(self, tracks):
        total_valence = 0
        for i in range(len(tracks)):
            total_valence += tracks[i][11]
        average_valence = total_valence / len(tracks)
        return average_valence

    def speechiness_calc(self, tracks):
        total_speechiness = 0
        for i in range(len(tracks)):
            total_speechiness += tracks[i][12]
        average_speechiness = total_speechiness / len(tracks)
        return average_speechiness

    def tempo_calc(self, tracks):
        total_tempo = 0
        for i in range(len(tracks)):
            total_tempo += tracks[i][13]
        average_tempo = total_tempo / len(tracks)
        return average_tempo

    def time_signature_calc(self, tracks):
        total_time_signature = 0
        for i in range(len(tracks)):
            total_time_signature += tracks[i][14]
        average_time_signature = total_time_signature / len(tracks)
        return average_time_signature

    def create_list(self):
        tracks = []
        for i in range(len(self.id_list)):
            track = self.get_track_features(self.id_list[i])
            tracks.append(track)
        return self.duration_calc(tracks), self.artist_list(tracks), self.explicit_calc(tracks), \
            self.popularity_calc(tracks), self.acoustincess_calc(tracks), self.danceability_calc(tracks), \
            self.energy_calc(tracks), self.instrumentalness_calc(tracks), self.liveness_calc(tracks), \
            self.loudness_calc(tracks), self.speechiness_calc(tracks), self.tempo_calc(tracks), \
            self.time_signature_calc(tracks)

    def test_list(self):
        tracks = []
        for i in range(len(self.id_list)):
            track = self.get_track_features(self.id_list[i])
            tracks.append(track)
        return self.artist_list(tracks)

    def playlist_compare(self, other):
        playlist_one = self.create_list()
        playlist_two = other.create_list()
        compatibility_index = 0
        duration_difference = abs(playlist_one[0] - playlist_two[0])
        if duration_difference <= 1:
            compatibility_index += 3
        playlist_one_artists = playlist_one[1]
        playlist_two_artists = playlist_two[1]
        if set(playlist_one_artists) & set(playlist_two_artists) != set():
            compatibility_index += 5
        acoust_difference = abs(playlist_one[4] - playlist_two[4])
        if acoust_difference <= .1:
            compatibility_index += 4
        print('Your compatibility percentage is: ', compatibility_index, '%')


spotify_one = Spotify('spotify:playlist:66mDGk6rWDGMAoRBNIT6J5') # sap
spotify_two = Spotify('spotify:playlist:1M5bYJb1gP3F94tlF6ZvJ6') # Beatles
spotify_one.get_track_ids()
spotify_two.get_track_ids()
#print(spotify_one.test_list())
#print(spotify_two.test_list())
spotify_one.playlist_compare(spotify_two)





# df = pandas.DataFrame(tracks, columns=['name', 'duration in ms'])
# df.to_csv("spotify.csv", sep=',')
