# spoti-lyric-with-os
Shows lyric of the current playing song on Spotify Desktop App. Currently only works on Linux.

![example](https://i.imgur.com/KQPfTED.png)

# Usage

* run on terminal ```python spoti_lyric.py```


# How work?
* The program gets song name that is currently playing on Spotify Desktop App. with the aid of 'subprocess' and 'xprop'.

  ```The xprop utility is for displaying window and font properties in an X server. ```
  
* Searches the song name on Google.
* If the song lyric found, - after some web scraping - the lyric displays on GUI.


# Adds 
 * Only searches within the sites given below. (New sites will be added to increase the probability of finding)
```
  - Metrolyrics.com
  - Genius.com
  - Azlyrics.com
```


# Requirements (tested versions)
**pip install -r requirements.txt**
  ```
Python 3.6.5
Requests 2.11.1
Beautifulsoup4 4.6.0
  ```
