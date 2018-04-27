import pylast
import os

def init_client():
    network = pylast.LastFMNetwork(
        api_key    = os.environ["PYLAST_API_KEY"],
        api_secret = os.environ["PYLAST_API_SECRET"],
    )

    return network

def now_playing(username):
    user  = client.get_user(username)
    track = user.get_now_playing()

    return track

client = init_client()
