# ---------------------------------
# ------             --------
#    Get your public IP:-
# ------             --------
# ---------------------------------
import requests

puplicip = requests.get("https://api.ipify.org/?format=json")
print("Your puplic IP is:" + str(puplicip.json()["ip"]))
