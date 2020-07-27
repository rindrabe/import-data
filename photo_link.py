import os
import netrc
import requests
import glob
from datetime import datetime
import xml.etree.ElementTree as ET
import re
import sys
import time

start_time = time.time() # for the purpose of recording the time for the system to run the script

#define the name of the column that has the photos
photo_col_name = ['column name photo #1','column name photo #2','column name photo #...'] # name of the columns containing photos

#define the following by info of the parent form where we re copying the data from
parent_username = 'parent username'
parent_kc_id = 'kc id specific of the form'


photo_path = parent_username+'/attachments/'+parent_kc_id+'/'


filelist = glob.glob("tempfiles/*.xml")
for file in filelist:
	# print('### *** FILE: '+file)
	et = ET.parse(file)
	tree = et.find('meta')
	uuid = tree.find('instanceID').text
	uuid = uuid.replace('uuid:','')
	
	for col in photo_col_name:
		# print('---',col)
		for photo in et.iter(col):
			if photo is None:
				break
				# print('NONE')
			elif photo.text is None:
				break
				# print('NONE Text')
			else:
				photo_name = photo.text
				photo_link = photo_path+uuid+'/'+photo_name
				# print('---> photo link:'+photo_link)
				photo.text = photo_link
	et.write(file)
	# print('--> SUCCESS in file:'+file)

print("--- Running time: %s seconds ---" % (time.time() - start_time))

print('***** ************ *****')
print('*****     PHOTO    *****')
print(' ****     LINKS    **** ')
print('  ***      ARE     ***  ')
print('   ** SUCCESSFULLY **   ')
print('    *     ADDED    *    ')
print('    * ************ *     ')
