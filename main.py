from converter import convert_media, file_partial_encode_base64, file_partial_decode_base64
from pathlib import Path
from uploader import upload_files_to_dropbox
import os
from pydub.utils import mediainfo 
import json
import dropbox
import logging 
import multiprocessing

def convert(base_dir):
	while True:
		convert_media(base_dir,pagination = 2)
	

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	base_dir = os.getcwd()
	txt_log_counter = 0 #
	processes = []

	convert_process = multiprocessing.Process(target = convert, args = [base_dir])
	convert_process.start()
	processes.append(convert_process)


	# encoding_pagination = 100
	# for _,to_encode_path in zip(range(encoding_pagination),Path(base_dir + "/converted").glob("*.ogg")):
	# 	file_partial_encode_base64(to_encode_path)

	# # #Fragment of code tu decode files from encoded folder
	# # # ---------------------------------------------------
	# # # for _,to_encode_path in zip(range(encoding_pagination),Path(base_dir + "/encoded").glob("*.ready")):
	# # # 	file_partial_decode_base64(to_encode_path)
	# # #----------------------------------------------------

	# with open("config.json", "r") as json_file:
	# 	config = json.load(json_file)

	# # Conecting with dropbox api
	# dbx = dropbox.Dropbox(config['dropbox_token'])
	
	# #Upload to dropbox
	# upload_pagination = 3
	# file_paths = [j for _,j in zip(range(upload_pagination),Path(base_dir + "/encoded").glob("*.*"))]
	# upload_files_to_dropbox(dbx, file_paths, upload_pagination, txt_log_counter)
	# txt_log_counter += 1

	for p in processes:
		p.join()

	# Tareas:
	#Annadir traspaso de metadata de audio mp3 a ogg(converter) y de ogg a ready(uploader) para leerlo X
	#Aplicar multiprocessing para que se vayan haciendo los procesos en paralelo



	