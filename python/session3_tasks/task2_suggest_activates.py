# -------------------------------------------------------------------------
# ----------                                              ---------
#      Write a code to suggest automatically activates for you :-
# ----------                                              ---------
# -------------------------------------------------------------------------
import requests

print("Want to do an activity?")
answer = input(("[y/n]\n")).lower()
if answer == "y":
    activity = requests.get(
        "https://www.boredapi.com/api/activity"  #  API that gets a random activity
    )
    print(activity.json()["activity"])
elif answer == "n":
    print("come later, maybe you will change your mind")
