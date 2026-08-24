import requests
import time

BASE_URL = "https://musicbrainz.org/ws/2"
METALLICA_ID = "65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab"

HEADERS = {
    "User-Agent": "MetallicaPythonApp/1.0"
}

LYRICS_URL = "https://lrclib.net/api/search"
LYRICS_HEADERS = { "User-Agent": "MetallicaCLI/1.0"}

def get_lyrics(song_name):
    params = {
        "track_name": song_name,
        "artist_name": "Metallica"
    }

    try:
        response = requests.get(
            LYRICS_URL,
            headers=LYRICS_HEADERS,
            params=params,
            timeout=10
        )

        response.raise_for_status()

    except requests.Timeout:
        print("Lyrics service took too long to respond.")
        return None
    except requests.RequestsException as error:
        print(f"Lyrics API error: {error}")
        return None

    results = response.json()

    if not results:
        return None

    return results

def search_songs(song_name):
    url = f"{BASE_URL}/recording"

    params = {
        "query": f'artist:"Metallica" AND recording:"{song_name}"',
        "limit": 500,
        "fmt": "json"
    }

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            params=params,
            timeout=30
        )

        response.raise_for_status()

    except requests.Timeout:
        print("MusicBrainz took too long to respond.")
        return []

    except requests.RequestException as error:
        print(f"MusicBrainz API error: {error}")
        return []

    data = response.json()

    return data.get("recordings", [])

def get_albums():
    url = f"{BASE_URL}/release-group"

    params = {
        "artist": METALLICA_ID,
        "type": "album",
        "limit": 100,
        "fmt": "json",
        "inc": "artist-credits"
    }

    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=30)
        response.raise_for_status()
    except Exception as error:
        print(f"Error getting albums: {error}")
        return []
    else:
        data = response.json()

    return data["release-groups"]

def show_menu():
    print("\n🤘 METALLICA DATABASE 🤘")
    print("1. Albums")
    print("2. Search songs")
    print("3. Lyrics")
    print("4. Concert setlists")
    print("5. Latest news")
    print("6. Random song")
    print("7. Quit")


def main():
    while True:
        show_menu()

        choice = input("\nChoose: ")

        if choice == "1":
            albums = get_albums()

            studio_albums = []

            for album in albums:
                secondary_types = album.get('secondary-types', [])
                artist_credit = album.get("artist-credit", [])

                metallica_only = (
                    len(artist_credit) == 1
                    and artist_credit[0]['artist']['id'] == METALLICA_ID
                )

                if not secondary_types and metallica_only:
                    studio_albums.append(album)

            studio_albums.sort(
                key=lambda album: album.get('first-release-date', '9999')
            )

            for album in studio_albums:
                date = album.get('first-release-date', 'Unknown')
                print(f"{date}: {album['title']}")

        elif choice == "2":
            song_name = input("Enter song name: ")
            print("\nSearching...please wait up to 30 seconds...\n")
            songs = search_songs(song_name)

            titles=[]
            seen_titles = set()
            if not songs:
                print("No songs found.")
            else:
                for song in songs:
                    title = song["title"]

                    normalized_title = title.lower()
                    if normalized_title not in seen_titles:
                        seen_titles.add(normalized_title)
                        titles.append(title)
                for title in titles:
                    print(title)
        elif choice == "3":
            song_name = input("Enter song name: ")

            results = get_lyrics(song_name)

            if not results:
                print("Lyrics not found.")
                continue

            # Keep exact title matches when possible
            exact_matches = []

            for result in results:
                if result['trackName'].lower() == song_name.lower():
                    exact_matches.append(result)

            if exact_matches:
                results = exact_matches

            print("\nMatches: ")

            for index, result in enumerate(results[:5], start=1):
                print(
                    f"{index}. {result['trackName']} "
                    f"- {result['albumName']}"
                )

            selection = input('\nChoose recording: ')

            try:
                index = int(selection) - 1
                result = results[index]
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue


            print(f"\n{result['trackName']}")
            print(f"Album: {result['albumName']}")
            print("-" * 40)

            lyrics = result.get("plainLyrics")

            if lyrics:
                print(lyrics)
            else:
                print("No 'plain' lyrics available.")
        elif choice == "4":
            print("Setlists!")
        elif choice == "5":
            print("News!")
        elif choice == "6":
            print("Random song!")
        elif choice == "7":
            print("Later! 🤘")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()





