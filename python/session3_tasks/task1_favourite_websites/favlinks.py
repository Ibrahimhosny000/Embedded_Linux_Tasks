# ------------------------------------------------
# ------                     ---------
#   module for favourite wbsites:-
# ------                     ---------
# ------------------------------------------------
import webbrowser

links = {
    "facebook": "https://www.facebook.com/",
    "youtube": "https://www.youtube.com/",
    "google": "https://www.google.com/",
    "instagram": "https://www.instagram.com/",
    "github": "https://github.com/",
    "haker rank": "https://www.hackerrank.com/",
}
names = links.keys()
urls = links.values()
print(f"avilable websites are:{list(names)}")
choosen = input("choose your favourite one ===> ").lower().strip()
choosenlink = links.get(choosen)


def firefox(choosenlink):
    webbrowser.open_new_tab(choosenlink)
