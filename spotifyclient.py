import json
import requests

from track import Track
from playlist import Playlist


class Spotifyclient:

    def __init__(self, auth_token ):
        self.user_id = ""
        self.auth_token = auth_token

    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"
            }
        )
        return response

    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data,
            headers={
                "Content-type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"
            }

        )
        return response

    def get_uri(self):
        uri="https://api.spotify.com/v1/me"
        response = self._place_get_api_request(uri)
        response_json = response.json()
        self.user_id=response_json["id"]
        print(f"user id {self.user_id}")

    def get_last_played_tracks(self, limit=10):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
                  track in response_json['items']]
        return tracks


    def get_track_recommendation(self, seed_tracks, limit=50):
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for
                  track in response_json["tracks"]]
        return tracks

    def create_playlist(self, name):
        data = json.dumps({
            "name": name,
            "description": "Recommendation Tracks",
            "public": True
        }
        )
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        # create playlist
        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return playlist



    def populate_playlist(self,playlist,tracks):
        track_uris=[track.create_spotify_uri() for track in tracks]
        data=json.dumps(track_uris)
        url=f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response=self._place_post_api_request(url,data)
        response_json=response.json()
        return response_json
