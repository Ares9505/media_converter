from  pydub import AudioSegment
from pydub.utils import mediainfo
from pathlib import Path
import os
import logging
from cryptography.fernet import Fernet
import dropbox


def convert_media(base_dir):
	'''
		Convert .mp3 and .flac audios from folder '/audios'
		in oog 96kbs 
	'''
	for paths,_,files in os.walk(base_dir + "/audio/"):
		for file in files:
			storage_dir = base_dir + "/converted/" + str(Path(file).stem) + ".ogg"
			if Path(file).suffix == ".mp3":	
				audio = AudioSegment.from_mp3( os.path.join(paths,file))			
				audio_converted = audio.export(storage_dir, format = "ogg", bitrate="96000")

			if Path(file).suffix == ".flac":
				audio = AudioSegment.from_file(os.path.join(paths,file), "flac")				
				audio_converted = audio.export(storage_dir, format = "ogg", bitrate="96000")
				# print(mediainfo(base_dir + "/converted/" + str(Path(file).stem) + ".ogg")['bit_rate'])




def generate_key():
	'''
		Genarate key and store it in mykey.key
	'''
	key = Fernet.generate_key()
	with open("mykey.key","wb") as key_file:
		key_file.write(key) 




def encrypt_file(file : Path,key : str):
	'''
		Encrypt file using a key 
		the encryted file will be store in out.txt
	'''
	fernet = Fernet(key) # generating key

	with open(file, 'rb') as original_file:
		original_file_data = original_file.read()
	
	encrypted_file_data = fernet.encrypt(original_file_data) # encripting data
	
	with open("out.txt", 'wb') as encrypted_file:
		encrypted_file.write(encrypted_file_data)



def decrypt_file(file : Path, key : str):
	'''
		Decrypt file using a key 
		the decryted file will be store in out.mp3
	'''
	fernet = Fernet(key)

	with open(file, "rb") as encryted_file:
		encrypted_file_data = encryted_file.read()

	decrypted_file_data = fernet.decrypt(encrypted_file_data)

	with open("out.mp3", "wb") as decrypted_file:
		decrypted_file.write(decrypted_file_data)



def upload_file_to_dropbox(files : list, direcction_to_upload, pagination = 1000):
	'''
		Upload a list of files to dropbox
	'''
	file_from = 'some file'
	file_to = 'direction to upload'
	dbx = dropbox.Dropbox('access_token')
	
	for file in files:
		dbx.files_upload(open(file, 'rb').read(), file_to)


def main():
	base_dir = os.getcwd()
	# convert_media(base_dir)

	#getting key
	with open("mykey.key",'rb') as file:
		key = file.read()


	#getting file to encript
	p=Path(base_dir)
	p_mp3 =[p for p in p.glob("*.mp3")]

	#encrypt
	encrypt_file(p_mp3[0], key)


	#getting file to decrypt
	p=Path(base_dir)
	p_txt=[p for p in p.glob("*.txt")]
	print(p_txt)
	#decrypt
	decrypt_file(p_txt[1], key) 
	




if __name__ == "__main__":
	# logging.basicConfig(level=logging.INFO)
	main()
	