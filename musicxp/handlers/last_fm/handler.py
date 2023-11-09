"""Singleton to import the LastFM Handler."""
import os
import requests


class LastFMHandler:
    """Class with all possible LastFM Calls to be used."""

    LASTFM_ID = os.environ["LAST_FM_USER_ID"]
    LASTFM_TOKEN = os.environ["LAST_FM_TOKEN"]
    LASTFM_API_URL = "http://ws.audioscrobbler.com/2.0/"

    def __init__(self) -> None:
        self.url_get_similar_artist = f"{self.LASTFM_API_URL}?" \
                                      f"method=artist.getsimilar&" \
                                      f"artist={{input_artist}}&" \
                                      f"limit={{num_artists}}&" \
                                      f"api_key={self.LASTFM_TOKEN}&" \
                                      f"format=json"

    def get_similar_artists(self, artist: str, num_artists: int = 10) -> list:
        """Select top similar artist from input."""
        response = requests.get(
            self.url_get_similar_artist.format(
                input_artist=artist,
                num_artists=num_artists
            ), timeout=5
        ).json()
        return [artist['name'] for artist in response['similarartists']['artist']]
