#!/usr/bin/env python3

import os,glob
from PIL import Image

for files in glob.glob("/home/student-03-0d194b9becfd/supplier-data/images/*.tiff"):
   im = Image.open(files)
   out_name = os.path.basename(files)[:3]
   #resize image to 600x400 and save it as jpeg format
   im.resize((600,400)).convert("RGB").save("/home/student-03-0d194b9becfd/supplier-data/images/" + out_name + ".jpeg", "JPEG")
