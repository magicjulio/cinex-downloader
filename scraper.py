from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pyautogui as py
from time import sleep
import PIL

# pyautogui keys
space = "62"
browser = "64"
enter = "66"
backspace = "67"

# urls
url = "https://cinex.me/"
movies_class = "flw-item"

# episods cordinates
big = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28],
       [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],
       [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]

# find elements by
id = "id"
name = "name"
xpath = "xpath"
link_text = "link text"
partial_link_text = "partial link text"
tag_name = "tag name"
class_name = "class name"
css_selector = "css selector"


# static
def test():
    for t in range(3):
        sleep(1)
        print(f"[+] {3-t}s left")
    print(py.position())

def click(x, y, t=0.2):
    if t != 0:
        py.moveTo(x, y, t)
    py.click(x, y)
def close_tab(tab=2):
    if tab == 1:
        click(308, 43, 0.2)
    elif tab == 2:
        click(612, 41, 0.2)
    elif tab == 3:
        click(723, 45, 0.2)
    elif tab == 4:
        click(963, 49, 0.2)
    else:
        print("[-] Tab out of range please recofigure")
def replace_spaces(movie_name):
    new = ""
    for letter in movie_name:
        if letter == " ":
            new += "-"
        else:
            new += letter
    return new

# general
def check_for_element(typ, val):
    try:
        browser.find_element(typ, val)
    except NoSuchElementException:
        return False
    return True
def play():
    # play
    click(662, 770)

    # close redirect
    close_tab(2)

    # play again
    click(662,770, 0.2)
    py.moveRel(100, 100, 1.5)
    click(662, 770, 1.5)

    # remove automatesoftware label
    click(1280, 144, 1)
    py.typewrite("f")
    py.moveTo(0, 0, 1)

# types
def find_type():
    content = browser.find_element(xpath, '//*[@id="main-wrapper"]/div[1]/div/div[1]/nav/ol/li[2]/a').get_attribute("title")
    if "Watch TV Shows" in content:
        return "s"
    if "Watch Movies" in content:
        return "m"
def set_type():
    video_type = input(f"[*] Is {movie} a movie or series? [m/s]: ")
    if video_type != "s":
        video_type = "movie"
    else:
        video_type = "series"
    return video_type

# movie
def downlaod_movies(second=False):
    # play
    click(662, 770, 0.5)

    # close redirect
    if not second:
        close_tab(2)

    # play again
    click(662,770, 0.5)
    py.moveRel(100, 100, 1.1)
    # loads faster when series 2nd
    if second:
        click(662, 770, 1.5)
    else:
        click(662, 770, 1.5)


    # scroll to download b & click
    py.scroll(-10)
    py.moveTo(680, 800, 1)
    try:
        x, y = py.locateCenterOnScreen("down.png")
    except TypeError:
        print("[!] Didnt found download button")
        breakpoint()
    click(x, y, 0.2)

    cordiantes = check_for_streamlare()
    if cordiantes == False:
        print("[-] Streamlare not avaible")
        return False
    else:
        x, y = cordiantes
        click(x=1030, y=y, t=0.5)
        if second:
            streamlare_download(second=True)
        else:
            streamlare_download()
        return True
def check_for_streamlare():
    sleep(1)
    try:
        check = py.locateCenterOnScreen("stream.png")
    except TypeError:
        return False
    if check != None:
        return check
    return False
def streamlare_download(second=False):
    # click streamlab
    close_tab(3)
    global i


    if second and i < 4:
        print("!" * 100)
        print("Round: ", i)
        i += 1
        click(525, 670, 0.9)

    # close possible adds
    if second:
        sleep(1)
        click(1253, 211, 1)
        click(1253, 211, 1)
    else:
        click(1253, 211, 0.5)
        click(1253, 211, 0.4)

    # click download button
    if second:
        click(1048, 364, 0.5)
    else:
        click(1048, 364, 0.2)

    # Finall download button
    for i in range(4):
        click(678, 526, 0.2)
        close_tab(4)
    click(678, 526, 0.2)


# series
def watch_series():
    py.hotkey("alt", "tab")
    single_season = input("[*] Enter a season: ")
    folge = input("[*] Enter a episod to watch: ")
    py.hotkey("alt", "tab")
    season_check_click(single_season)
    for liste in big:
        if int(folge) in liste:
            x = 390 + (300 * big.index(liste))
            for ele in liste:  # F2 [0]
                if int(folge) == ele:
                    y = 300 + (60 * liste.index(ele))
                    break
            break
    print("[+] x,y: ", x, y)
    py.moveTo(660, 560, 0.1)
    py.scroll(500)
    py.scroll(-235)
    click(x, y, 1)
    py.scroll(236)

    # play
    click(662, 770, 0.1)

    # close redirect
    close_tab(2)

    # play again
    click(662, 770, 0.2)
    py.moveRel(100, 100, 1)
    click(662, 770, 0.5)

    # full mod
    click(1280, 144, 1)
    py.typewrite("f")
    py.moveTo(0, 0, 1)
def download_series():
    abool = False
    # create seasons as key from dict
    py.hotkey("alt", "tab")
    dict_of_series = seasons_calc()

    # asign list of episods as values to keys
    for season_key in dict_of_series.keys():
        print(f"----season {season_key}-----")
        list_of_episods = []

        episods = input(f"[*] Enter episods for season {season_key}: (f.e: 1 | 1,2,5,6 | 1-4)(MAX 4!):\n>")
        py.hotkey("alt", "tab")
        if "," in episods:
            list_of_episods = episods.split(",")

        elif "-" in episods:
            a, b = episods.split("-")
            for i in range(int(a), int(b) + 1):
                list_of_episods.append(str(i))

        else:
            list_of_episods = [episods]
        dict_of_series.update({season_key:list_of_episods})

    # select season S6 F10
    for season_key in dict_of_series.keys():
        if season_check_click(season_key):
            liste_von_folgen = dict_of_series.get(season_key)
            for folge in liste_von_folgen:
                for liste in big:
                    if int(folge) in liste:
                        x = 390 + (300 * big.index(liste))
                        for ele in liste:   # F2 [0]
                            if int(folge) == ele:
                                y = 300 + (60 * liste.index(ele))
                                break
                        break
                print("[+] x,y: ", x, y)
                py.moveTo(660, 560, 0.2)
                py.scroll(500)
                py.scroll(-235)
                click(x, y, 1)
                py.scroll(236)
                sleep(0.3)

                if downlaod_movies(second=abool):
                    abool = True
                    print(f"[+] Downloading S{season_key} F{folge} ...")
                    close_tab(2)
                    close_tab(2)
                    click(1293, 1023, 0.1)
                    py.scroll(100)
                else:
                    print(f"[-] S{season_key} F{folge} is not avaible for download")
                    close_tab(2)
def seasons_calc():
    season = input("[*] Enter a season:\n")
    seasons_dict = {}

    if "," in season:
        ls = season.split(",")
        for ele in ls:
            seasons_dict.update({ele:None})

    elif "-" in season:
        a, b = season.split("-")
        for i in range(int(a), int(b) + 1):
            seasons_dict.update({str(i):None})

    elif len(season) <= 2:
        seasons_dict.update({season: None})
    else:
        print("[!] Input invalid")

    return seasons_dict
def season_check_click(season_num):
    if check_for_element(xpath, f'//*[@id="main-wrapper"]/div[2]/div/div/div[2]/div/div[1]/ul/li[{season_num}]/a'):
        print(f"[+] Season {season_num} found")
        browser.find_element(xpath, f'//*[@id="main-wrapper"]/div[2]/div/div/div[2]/div/div[1]/ul/li[{season_num}]/a').click()
        return True
    else:
        print(f"[-] Season {season_num} not found")
        return False

print("[+] System on")
print("==============main==================")

while True:

    # Enter movie
    movie = input("[*] Enter movie/series name: ")
    if movie == "q":    # only way out
        break
    elif " " in movie:
        movie = replace_spaces(movie)


    # download or watch
    dowload_or_watch = input("[*] Download or watch? [d/w]: ")

    # search for movies
    browser = webdriver.Chrome()
    search_url = url + "search/" + movie
    print("[+] Results: ", search_url)
    browser.get(search_url)

    # Check for exsistenz click first if yes
    if check_for_element(class_name, movies_class) == True:
        print(f"[+] Found {movie}!")
        browser.find_element(class_name, movies_class).click()
        video_type = find_type()
        if video_type == "m":
            if dowload_or_watch == "d":
                downlaod_movies()
            else:
                play()
        elif video_type == "s":
            if dowload_or_watch == "d":
                download_series()

            elif dowload_or_watch == "w":
                watch_series()

    elif check_for_element(class_name, movies_class) == False:
        print(f"[-] Sorry {movie} was not found!\n[?] Why? 1:Check spelling 2: Movie to unpopular")
    print("[*] Done")


print("====================================")
browser.quit()
print("[-] System off")
