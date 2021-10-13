from  pydub import AudioSegment
from pydub.utils import mediainfo
from pathlib import Path
import os
import logging
from cryptography.fernet import Fernet
import base64

import magic

def convert_media(base_dir: Path, pagination: int):
	'''
		Convert .mp3 and .flac audios from folder '/audios'
		in oog 96kbs 
	'''
	counter = 0

	for paths,_,files in os.walk(base_dir + "/audio/"):
		for file in files:
			storage_dir = base_dir + "/converted/" + str(Path(file).stem) + ".ogg"
			if Path(file).suffix == ".mp3":	
				audio = AudioSegment.from_mp3( os.path.join(paths,file))			
				audio_converted = audio.export(storage_dir, format = "ogg", bitrate="96000")

			elif Path(file).suffix == ".flac":
				audio = AudioSegment.from_file(os.path.join(paths,file), "flac")				
				audio_converted = audio.export(storage_dir, format = "ogg", bitrate="96000")
				# print(mediainfo(base_dir + "/converted/" + str(Path(file).stem) + ".ogg")['bit_rate'])

			else:
				logging.warning("The file located at" + paths + "was not converted")
			
			counter+=1
			if counter == pagination:
				break

		logging.info("100 songs processed")




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
	
	with open("out.ini", 'wb') as encrypted_file:
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



def file_partial_encode_base64(file_path): #se codificaran los 100 primeros bits
	'''
		Overwrite first 150 bits information with base64 equivalent, the rest of the 
		strem remain iqual
	'''
	with open(file_path, "rb") as file:
		data = file.read()
	partial_data_encoded = base64.encodebytes(data[:150])
	print(len(partial_data_encoded))
	#concatenando dos byte string
	data_encoded = b''.join([partial_data_encoded,data[150:]])	
	with open("encoded/" + file_path.name + ".ready", "wb") as file_to:
		file_to.write(data_encoded)



def file_partial_decode_base64(file_path):
	with open(file_path, "rb") as file:
		data = file.read()

	partial_data_decoded = base64.decodebytes(data[:203])	
	#concatenando dos byte string
	data_encoded = b''.join([partial_data_decoded,data[203:]])
	
	with open("decoded/" + file_path.stem, "wb") as file_to:
		file_to.write(data_encoded)	



def main():
	base_dir = os.getcwd()
	convert_media(base_dir )

	#getting key
	# with open("mykey.key",'rb') as file:
	# 	key = file.read()


	#getting file to encript from root directory
	p=Path(base_dir)
	p_mp3 =[p for p in p.glob("*.ogg")]

	# #encrypt
	# encrypt_file(p_mp3[0], key)


	# # #getting file to decrypt
	# p=Path(base_dir)
	# p_txt=[p for p in p.glob("*.ini")]
	# print(p_txt)
	# # #decrypt
	# # decrypt_file(p_txt[1], key) 


	


if __name__ == "__main__":
	# logging.basicConfig(level=logging.INFO)
	# main()

	base_dir = os.getcwd()
	paths_files = [p for p in Path(base_dir + '/converted').glob("*.ogg")]
	for path in paths_files:
		file_partial_encode_base64(path)

	
	# print(magic.from_file("encoded"))
	


#Probar codificar en vez de encriptar
#Annadir manejo de errores a conversion de media

#notas:
#para decodificar seran 138bytes
#hacer funcion de decodificacion

