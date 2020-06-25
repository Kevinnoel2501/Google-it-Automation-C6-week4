#! /usr/bin/env python3
import requests
import glob

url = "http://localhost/upload/"
for files in glob.glob("/home/student-03-0d194b9becfd/supplier-data/images/*.jpeg"):
   with open(files, 'rb') as f:
      r = requests.post(url, files={'file': f}) #add images to ip_address/media/images
