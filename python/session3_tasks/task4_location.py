# ------------------------------
# ------           -------
#    Get your location:-
# ------           -------
# ------------------------------
import requests

print("Want to get your location?")
answer = input("y/n\n").lower()
if answer == "y":
    puplicip = requests.get("https://api.ipify.org/?format=json")
    ip = puplicip.json()["ip"]
    puplicip = str("https://ipinfo.io/" + ip + "/geo")
    locals = requests.get(puplicip)
    print(locals.json())
elif answer == "n":
    print("come back if you change your mind")
