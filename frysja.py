from datetime import date, datetime
import datetime
import urllib.request

# Get date today and time for the filename
date = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M")

# Set start date
start = date(2021, 10, 19)

# Get date today
today= date.today()

# Calculate the diff between start date and date today
diff=today-start
diff = str(diff.days)

# Adds zeros (0) at the beginning of the file name
filnavn = diff.zfill(4)

# Insert image URL
urllib.request.urlretrieve("https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg", 
filnavn+"_frysja_"+str(date)+".jpg")