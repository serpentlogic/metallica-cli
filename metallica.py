import requests

BASE_URL = "https://musicbrainz.org/ws/2"
METALLICA_ID = "65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab"

HEADERS = {
    "User-Agent": "MetallicaPythonApp/1.0"
}

def get_albums():
    url = f"{BASE_URL}/release-group"

    params = {
        "artist": METALLICA_ID,
        "type": "album",
        "limit": 100,
        "fmt": "json",
        "inc": "artist-credits"
    }

    response = requests.get(url, headers=HEADERS, params=params, timeout=10)
    response.raise_for_status()
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
            print("Song search!")
        elif choice == "3":
            print("Lyrics!")
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





