# Anonymous Instagram Stories Viewer

_View all Instagram stories anonymously!_
<br />
<br />
Here's how igStoriesGetter looks in action.


```
$ python igStoriesGetter.py igAccountName

    _       _____ __             _           ______     __  __
   (_)___ _/ ___// /_____  _____(_)__  _____/ ____/__  / /_/ /____  _____
  / / __ `/\__ \/ __/ __ \/ ___/ / _ \/ ___/ / __/ _ \/ __/ __/ _ \/ ___/
 / / /_/ /___/ / /_/ /_/ / /  / /  __(__  ) /_/ /  __/ /_/ /_/  __/ /
/_/\__, //____/\__/\____/_/  /_/\___/____/\____/\___/\__/\__/\___/_/
  /____/


[+]  Image Story found:  https://instagram.fdgo1-1.fna.fbcdn.net/v/f22.1234-56/a12/34567890_1234567890012341_12412412141_n.jpg
[+]  Video Story found:  https://instagram.fdgo1-1.fna.fbcdn.net/v/f22.1234-56/a12/34567890_1234567890012341_12412412141_n.mp4
```

## Setup

1. Clone the repository

```
$ git clone https://github.com/EverStarck/anon-ig-stories-viewer
```

2. Install the dependencies

```
$ cd igStoriesGetter
$ pip install -r requirements.txt
```

3. Introduce your instagram cookie

```python
7. COOKIE = '' # <--- HERE
```

To get your instagram cookie just go to ig official page and follow the next steps: <br/>

1. Right click in empty space > inspect element > Network tab
2. Press f5 to realod the page
3. Search for "www.instagram.com", it should be the first
4. Search for Request Headers
5. Copy all the content of "Cookie"

It should look like this:

```py
COOKIE = 'csrftoken=IIIIIIIII44444AAAAAACCCCCCCBBBBB; ig_did=1111111-1111-1111-1111-111111111111; ig_nrcb=1; mid=B_BBBBBBBBBBBBB-BBBBBBBBBBBB; fbm_11111111111111=base_domain=.instagram.com; datr=AAAAAAAAAAAAAAAAAAAAAAAAAAA; ds_user_id=11111111111; csrftoken=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA; sessionid=111111111111111111111111; shbid="11111\1111111111111\11111111111:111111111111111111111111111111111111111111111111111111111111111"; shbts="111111111\1111111111\111111111111:11111111111111111111111111111111111111111111111111111111111111"; rur="AAA\111111111111\11111111111:1111111111111111111111111111111111111111111111111111"' # <--- HERE
```

4. Run the script

```
$ python igStoriesGetter.py igAccountName
```


## Δ


If the script doesn't work as it should because of this, feel free to open an issue or a PR

## Compatibility

Tested on Python 3.9 on Linux and Windows. Feel free to open an issue if you have bug reports or questions. If you want to collaborate, you're welcome.
