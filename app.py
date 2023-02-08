import sys
import time
import random
from datetime import datetime, timedelta

from lib.FlexUnlimited import FlexUnlimited

timed = False


if __name__ == "__main__":
  print("***Amazon Flex Unlimited v2*** \n")
  flexUnlimited = FlexUnlimited()
  if (len(sys.argv) > 1):
    arg1 = sys.argv[1]
    if (arg1 == "getAllServiceAreas" or arg1 == "--w"):
      print("\n Your service area options:")
      print(flexUnlimited.getAllServiceAreas())
    else:
      print("Invalid argument provided.")
  else:
    while(timed):
      nw = datetime.now()
      hrs = nw.hour
      mins = nw.minute
      secs = nw.second
      zero = timedelta(seconds=secs + mins * 60 + hrs * 3600)
      st = nw - zero  # this take me to 0 hours.
      time1 = st + timedelta(seconds=2 * 3600 + 0 * 60)  # this gives 10:30 AM
      time2 = st + timedelta(seconds=3 * 3600 + 0 * 60)  # this gives 4:30 PM
      if nw >= time1 and nw <= time2:
        flexUnlimited.run()
      time.sleep(300)
      print("Waiting")
    while(not timed):
        flexUnlimited.run()
        time.sleep(540 + random.randint(0, 120))
