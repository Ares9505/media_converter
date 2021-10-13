import dropbox
import json
import os
from pathlib import Path
from tinytag import TinyTag


def upload_file_to_dropbox(): #
	'''
		upload a single file to dropbox
	'''
	dbx = dropbox.Dropbox('acces_token')
	
	# for file in files:
	dbx.files_upload(open('requirements.txt', 'rb').read(), '/Descargas/requirements1.txt')



def upload_files_to_dropbox(
	dbx : dropbox.Dropbox,
	 file_paths: list
	 ):
	'''
		Upload files to folder /Descargas i dropbox
		Save a json with upload files
	'''

	for file in file_paths:
		audio = TinyTag.get(file)
		audio.artist
		audio.title
		print(audio.title)
		
		# current_file = open(file, 'rb').read()
		# dbx.files_upload(current_file, '/Descargas/' + str(file.name))



def main():
	with open("config.json", "r") as json_file:
		config = json.load(json_file)

	#Base directory to upload
	base_dir = os.getcwd() + '/audio'

	#Creating test files
	# for i in range(10):
	# 	file=open('converted/{}.txt'.format(i),'wb')
	# 	file.close()

	#list of files to upload ineficiently without list of the files in the dir
	pagination = 6
	file_paths = [j for _,j in zip(range(pagination),Path(base_dir).glob("*.*"))]
	
	# Conecting with dropbox api
	dbx = dropbox.Dropbox(config['dropbox_token'])

	upload_files_to_dropbox(dbx, file_paths)


if __name__ == "__main__":
	main()
		

	# Direccion de la api:
	# https://www.dropbox.com/developers/apps/info/qogj8z5rrgn1hgn#permissions

