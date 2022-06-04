from datetime import date, datetime
import urllib.request

# Get date today and time for the filename
dato = datetime.utcnow().strftime("%Y-%m-%d_%H-%M")

# Set start date
start = date(2022, 6, 4)

# Get date today
today= date.today()

# Calculate the diff between start date and date today
diff=today-start
diff = str(diff.days)

# Adds zeros (0) at the beginning of the file name
filnavn = diff.zfill(4)

# Insert image URL
urllib.request.urlretrieve("https://kunde.byggekamera.no/?p=133&c=684&width=fullsize", 
filnavn+"_frysja_"+str(dato)+".jpg")
