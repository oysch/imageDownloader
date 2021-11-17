from datetime import date, datetime
import datetime
import urllib.request

dato = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M")

start = date(2021, 10, 19)
print(start)
today= date.today()
diff=today-start

diff = str(diff.days)

filnavn = diff.zfill(4)

urllib.request.urlretrieve("https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg", 
filnavn+"_frysja_"+str(dato)+".jpg")