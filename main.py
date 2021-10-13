from converter import convert_media, file_partial_encode_base64, file_partial_decode_base64
from pathlib import Path
from uploader import upload_files_to_dropbox
# from uploader
import os
from pydub.utils import mediainfo 

if __name__ == "__main__":
	base_dir = os.getcwd()
	# convert_media(base_dir,pagination = 100)
	
	# encoding_pagination = 100
	# for _,to_encode_path in zip(range(encoding_pagination),Path(base_dir + "/converted").glob("*.ogg")):
	# 	file_partial_encode_base64(to_encode_path)

	# #Fragment of code tu decode files from encoded folder
	# # ---------------------------------------------------
	# # for _,to_encode_path in zip(range(encoding_pagination),Path(base_dir + "/encoded").glob("*.ready")):
	# # 	file_partial_decode_base64(to_encode_path)
	# #----------------------------------------------------

	# with open("config.json", "r") as json_file:
	# 	config = json.load(json_file)


	# # Conecting with dropbox api
	# dbx = dropbox.Dropbox(config['dropbox_token'])
	dbx = 0
	upload_pagination = 100
	file_paths = [j for _,j in zip(range(upload_pagination),Path(base_dir + "/audio").glob("*.*"))]
	upload_files_to_dropbox(dbx, file_paths)




	