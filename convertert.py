from  pydub import AudioSegment
from pydub.utils import mediainfo
from pathlib import Path
import os
import logging



def main():
	base_dir = os.getcwd()
	for paths,folders ,files in os.walk(base_dir):
		for file in files:
			storage_dir = base_dir + "/converted/" + str(Path(file).stem) + ".ogg"
			if Path(file).suffix == ".mp3":	
				audio = AudioSegment.from_mp3( os.path.join(paths,file))			
				audio_converted = audio.export(storage_dir, format = "ogg", bitrate="96000")

			if Path(file).suffix == ".flac":
				audio = AudioSegment.from_file(os.path.join(paths,file), "flac")				
				audio_converted = audio.export(storage_dir, format = "ogg", bitrate="128000")
				# print(mediainfo(base_dir + "/converted/" + str(Path(file).stem) + ".ogg")['bit_rate'])



if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	main()
	
