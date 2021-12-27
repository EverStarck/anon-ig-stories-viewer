import requests
import sys, colorama
from colorama import Fore, Style

COOKIE = ''  # <--- HERE


USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)"
headers = {"user-agent": USER_AGENT, "cookie": COOKIE}


profile = sys.argv[1]
getInfoUrl = f"https://www.instagram.com/{profile}/?__a=1"


# initialize colorama
colorama.init()
bad = Fore.RED + "[-]" + Style.RESET_ALL
good = Fore.GREEN + "[+]" + Style.RESET_ALL
alert = Fore.YELLOW + "[Δ]" + Style.RESET_ALL


# Get user ID with profile name
def getID():
    try:
        req = requests.session()
        req.headers.update(headers)
        res = req.get(getInfoUrl)
        userInfo = res.json()
        return {
            "id": userInfo["graphql"]["user"]["id"],
            "followersNumber": userInfo["graphql"]["user"]["edge_follow"]["count"],
            "isPrivate": userInfo["graphql"]["user"]["is_private"],
            "followed_by_viewer": userInfo["graphql"]["user"]["followed_by_viewer"],
        }
    except:
        print(
            f"There was an error getting the user {profile}\nIf the user is ok then it is a cookie error"
        )
        sys.exit()


# Get links of instagram stories
def getStories():
    userID = getID()
    if userID["isPrivate"] and userID["followed_by_viewer"] == False:
        print("The account is private, you cannot get followers info.")
        return
    try:
        req = requests.session()
        req.headers.update(headers)
        res = req.get(
            f"https://i.instagram.com/api/v1/feed/user/{userID['id']}/reel_media/"
        )
        if res.status_code == 200:
            stories = res.json()["items"]
            if len(stories) == 0:
                print(f"{alert} There are no stories for {profile}")
                return

            for story in stories:
                media_type = story["media_type"]  # 1 = image, 2 = video
                if media_type == 1:
                    print(
                        f"{good} \033[1m Image Story found: \033[0m {story['image_versions2']['candidates'][0]['url']}"
                    )
                elif media_type == 2:
                    print(
                        f"{good} \033[1m Video Story found: \033[0m {story['video_versions'][0]['url']}"
                    )
            return
        else:
            print("There was an error getting the stories")
            return False
    except:
        print("There was an error getting the stories\nMaybe it's a cookie error")
        sys.exit()


print(
    """
    _       _____ __             _           ______     __  __
   (_)___ _/ ___// /_____  _____(_)__  _____/ ____/__  / /_/ /____  _____
  / / __ `/\__ \/ __/ __ \/ ___/ / _ \/ ___/ / __/ _ \/ __/ __/ _ \/ ___/
 / / /_/ /___/ / /_/ /_/ / /  / /  __(__  ) /_/ /  __/ /_/ /_/  __/ /
/_/\__, //____/\__/\____/_/  /_/\___/____/\____/\___/\__/\__/\___/_/
  /____/
 \n"""
)

getStories()
