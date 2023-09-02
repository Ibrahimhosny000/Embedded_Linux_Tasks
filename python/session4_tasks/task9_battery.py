# -----------------------------------------------------------
# ---------                               -------------
#      display % Battery and make Notification:
# ---------                               -------------
# -----------------------------------------------------------


from pynotifier import notification
import psutil

battary = psutil.sensors_battery()
percent = battary.percent
print(percent)
notification(
    "battary percentage ", str(percent) + "% percent remaining", duration=10
).send()
