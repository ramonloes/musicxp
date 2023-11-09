"""Main API module."""
from musicxp.handlers.mixin.music_mixin import MusicMix
from musicxp.src.primary_objects import MAIN_API_INTERFACE


@MAIN_API_INTERFACE.get("/")
async def root():
    """Main page of the API."""
    return {"message": "Hello! API in progress!"}


@MAIN_API_INTERFACE.get("/recommendation/byartist/{artist}")
async def recommend_track_by_artist(artist: str, play_it: bool = True):
    """Recommend a track by artist."""
    music_handler = MusicMix()
    recommendation = music_handler.random_track_by_artist(artist)
    music_handler.play_uri_track(recommendation["spotify_uri"])
    return recommendation
