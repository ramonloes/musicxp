"""Class mixin: All handlers in one!"""
from random import sample
from musicxp.handlers.last_fm.handler import LastFMHandler
from musicxp.handlers.spotify.handler import SpotifyHandler


class MusicMix(LastFMHandler, SpotifyHandler):
    """Mixin class to handle all music APIs."""
    def __init__(self) -> None:
        super().__init__()
        super(LastFMHandler, self).__init__()

    def random_track_by_artist(self, artist: str, spotify_search: bool = False,
                               num_artists: int = 10) -> str:
        """Select a random track from a certain artist."""
        if not artist:
            raise ValueError("No artist was specified")

        id_spotify_artists = []
        similar_artists = self.get_similar_artists(artist, num_artists) \
            if not spotify_search else [artist]

        for sim_artist in similar_artists:
            id_artist = self.search_artist_id(sim_artist)
            if id_artist:
                id_spotify_artists.append(id_artist)

        if not id_spotify_artists:
            raise AssertionError("No IDs were found on Spotify DB!")

        id_spotify_artists = sample(id_spotify_artists, 5) if \
            len(id_spotify_artists) >= 5 else id_spotify_artists

        spotify_search = self.spotify_api.recommendations(
            seed_artists=id_spotify_artists,
            limit=1
        )

        return {
            "recommended_artist": spotify_search['tracks'][0]['artists'][0]['name'], 
            "recommended_track": spotify_search['tracks'][0]['name'],
            "spotify_uri": spotify_search['tracks'][0]['uri']
        }
