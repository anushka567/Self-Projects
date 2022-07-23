# python automation to get recommendations from last played tracks and add to a playlist in spotify
from secrets import oauth_token
from spotifyclient import Spotifyclient


# remember to hide the id and oauth token
def main():
    spotifyclient = Spotifyclient(oauth_token)
    spotifyclient.get_uri()

    num_tracks_visual = int(input("How many tracks you want to visualise?"))
    last_played_tracks = spotifyclient.get_last_played_tracks(num_tracks_visual)

    print(f"here are the {num_tracks_visual} you played last on your Spotify account")
    for index, track in enumerate(last_played_tracks):
        print(f"{index + 1}. {track}")

    seeds = input("Enter the tracks you want to use as seeds upto 5?")
    seeds = seeds.split()
    print(seeds)
    seed_tracks = [last_played_tracks[int(index) - 1] for index in seeds]
    size=seed_tracks.__len__()
    for i in range(size):
        track=seed_tracks[i]
        print(track.name)
    recommmend_tracks = spotifyclient.get_track_recommendation(seed_tracks)
    print("These tracks have been recommended based on the seed tracks")
    for track in recommmend_tracks:
        print(f"{track.name} by {track.artist}")

    playlist_name = input("enter playlist name?")
    playlist = spotifyclient.create_playlist(playlist_name)
    print(f"Playlist named {playlist_name} created succesfully")
    spotifyclient.populate_playlist(playlist, recommmend_tracks)
    print(f"Tracks added to {playlist_name}")


main()
