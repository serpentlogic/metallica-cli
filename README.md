
<img width="1672" height="941" alt="image" src="https://github.com/user-attachments/assets/49fcc018-b502-41b8-ae73-ee05618d27e5" />



# Metallica CLI 🤘

A Python command-line Metallica app that uses several public APIs to explore albums, songs, lyrics, concert setlists, news, and more.

It also includes a small terminal game called **Creeping Death Mode**.

## Features

* View Metallica studio albums in chronological order
* Search for Metallica songs
* Look up song lyrics and select between available recordings
* Search Metallica concert setlists by city
* View recent Metallica news
* Get a random Metallica song
* Play **Creeping Death Mode**, a simple terminal game

## APIs and Data Sources

### MusicBrainz

Used for:

* Albums
* Song search
* Random song selection

MusicBrainz API:

https://musicbrainz.org/doc/MusicBrainz_API

Metallica MusicBrainz Artist ID:

```text
65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab
```

MusicBrainz does not require an API key, but clients should provide a descriptive `User-Agent`.

### LRCLIB

Used for song lyrics.

https://lrclib.net/

The LRCLIB API does not require an API key.

### setlist.fm

Used for Metallica concert and setlist information.

https://api.setlist.fm/

The setlist.fm API requires a free API key.

### Google News RSS

Used to retrieve recent news stories related to Metallica.

https://news.google.com/

The news feature reads Google's RSS news search feed and does not require an API key.

<img width="1402" height="1122" alt="image" src="https://github.com/user-attachments/assets/5fc0d6b6-efe8-4646-bca8-34361c78c713" />


## Requirements

* Python 3
* Internet connection
* `requests`
* A setlist.fm API key for the concert setlist feature

The other modules currently used by the application are part of Python's standard library:

```text
os
random
time
xml.etree.ElementTree
```

## Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd metallica
```

Optional but recommended: create a virtual environment.

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Install the required external Python package:

```bash
pip install requests
```

## setlist.fm API Key

To use the concert setlist feature, create an account at setlist.fm and obtain an API key.

Set the key as an environment variable before running the program.

### macOS / Linux

```bash
export SETLISTFM_API_KEY="your-api-key-here"
```

### Windows PowerShell

```powershell
$env:SETLISTFM_API_KEY="your-api-key-here"
```

Do **not** commit your API key to GitHub.

If using a `.env` file in the future, make sure `.env` is included in `.gitignore`.

## Running the Program

Run:

```bash
python3 metallica.py
```

or, depending on your system:

```bash
python metallica.py
```

The main menu looks similar to:

```text
🤘 METALLICA DATABASE 🤘

1. Albums
2. Search songs
3. Lyrics
4. Concert setlists
5. Latest news
6. Random song
7. Creeping Death Mode
8. Quit
```

Enter the number corresponding to the feature you want to use.

## Creeping Death Mode

Creeping Death Mode is a small terminal game included with the application.

You control Creeping Death:

```text
D = Creeping Death
@ = Soul
X = Enemy
```

Use:

```text
W = Up
A = Left
S = Down
D = Right
Q = Quit
```

Collect all souls while avoiding the enemy.

## API Reliability

This project depends on external services.

Occasionally an API may:

* respond slowly
* time out
* temporarily return an HTTP error such as `503 Service Temporarily Unavailable`
* return unusual or duplicate music metadata

The application includes basic error handling so that temporary API problems generally do not terminate the entire program.

## Project Status

The main application features are implemented.

Future improvements may include:

* Improved filtering of demos, B-roll recordings, and live versions
* Additional Creeping Death levels
* Improved retry handling
* Refactoring the program into multiple Python modules
* Better command-line presentation
* Dependency management with `requirements.txt`

## Disclaimer

This is an unofficial fan project and is not affiliated with or endorsed by Metallica.

Metallica and related names are trademarks of their respective owners.

Music and lyrics data remain the property of their respective rights holders.

<img width="1672" height="941" alt="image" src="https://github.com/user-attachments/assets/4049746d-b318-42ff-a6ce-a3a6f813eaac" />
