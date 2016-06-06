import urllib
import requests


roomnumber = 000
origin = 'http://www.srmuniv.ac.in/downloads/cdc/batch3/room_no_'

for i in range (000,1000):
	print("searching room number "+ str(i))
	url = origin +str(i)+'.pdf'
	r= requests.get(url)
	print(r.status_code)
	if(r.status_code == 200):
		print(" found room number " + str(i))
		urllib.urlretrieve(url , "UB_room_number_"+str(i)+".pdf")







