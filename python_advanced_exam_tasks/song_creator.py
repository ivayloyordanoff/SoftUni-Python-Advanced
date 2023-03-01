def add_songs(*songs):
    songs_dict = {}

    for song in songs:
        title, lyrics = song
        if title in songs_dict:
            songs_dict[title] += lyrics
        else:
            songs_dict[title] = lyrics

    result = ""

    for title, lyrics in songs_dict.items():
        result += f"- {title}\n"
        if lyrics:
            result += "\n".join(lyrics) + "\n"

    return result
