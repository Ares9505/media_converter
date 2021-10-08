from  pydub import AudioSegment
from pydub.utils import mediainfo
from pathlib import Path
import os
import logging
from cryptography.fernet import Fernet



def convert_media():
	base_dir = os.getcwd()
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
	key = Fernet.generate_key()
	with open("mykey.key","wb") as key_file:
		key_file.write(key) 


def main():
	convert_media()


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	generate_key()
	
'''Tareas:

*Comprobar que el formato sea ogg VORBIS
*Encriptar un archivo
*Subir archivos a dropbox
'''