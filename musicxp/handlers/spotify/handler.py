"""Singleton to import the SpotifyHandler."""
import os
import spotipy


class SpotifyHandler:
    """Class with all possible Spotify Calls to be used."""

    SPOTIFY_ID = os.environ["SPOTIFY_USER_ID"]
    SPOTIFY_TOKEN = os.environ["SPOTIFY_TOKEN"]

    def __init__(self) -> None:
        self.spotify_api = self.__init_spotify_client()

    def __init_spotify_client(self):
        client_cred_mgr = spotipy.oauth2.SpotifyOAuth(
            client_id=self.SPOTIFY_ID,
            client_secret=self.SPOTIFY_TOKEN,
            redirect_uri="https://example.com/callback",
            scope=["user-modify-playback-state"]
        )
        return spotipy.Spotify(auth_manager=client_cred_mgr)

    def search_artist_id(self, artist: str):
        """Get Spotify ID of an artist."""
        spotify_search = self.spotify_api.search(
            q=f"artist:{artist}",
            type="artist",
            limit=1
        )
        return spotify_search['artists']['items'][0]['id'] \
            if spotify_search['artists']['items'] else ''

    def play_uri_track(self, uri: str):
        """Play a track by URI."""
        self.spotify_api.start_playback(
            device_id="88ce6ce1a801547a78b470e34a1a90148fbfef70",
            uris=[uri]
        )
