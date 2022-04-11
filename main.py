from genericpath import exists
from logging import basicConfig
import time
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import InMemoryHistory
from danser import open_danser
from settings import get_setting, set_setting
# from window import Window
from utils import flush, format_beatmap_name, get_beatmaps, get_diffs

# Globals
window = None
frames = 0

def main():
	flush()
	global frames
	global window
	basicConfig()
	# Have to uncomment the next line once I've finished the gui
	# gui_mode = input(' Would you like to use the GUI [Y/n] ') 
	gui_mode = 'n'
	if gui_mode.lower() == 'y' or gui_mode.lower() == 'yes' or gui_mode == '':
		pass
		# window = Window()
		# window.open()
		# if window.isOpen():
		# 	window.loop()
		# print(' Quitting application')
	else:
		if not exists('settings.ini'):
			with open('settings.ini', 'w') as f:
				f.writelines(['# settings for the application\n','has_changed_settings=false\n','osu_song_dir=none\n','danser_exe=none'])
		if get_setting('has_changed_settings') == 'false':
			settings_session = PromptSession(enable_history_search=True)
			correct_osu_songs_path = False
			correct_danser_exe_path = False
			while not correct_osu_songs_path:
				flush()
				while True:
					try:
						osu_songs_path = settings_session.prompt(' Enter the path to your osu! Songs (ex: C:/Program Files/osu!/Songs) ')
					except KeyboardInterrupt:
						pass
					else: 
						break
				osu_songs_path_confirm = input(f' You entered {osu_songs_path}. Is this correct [Y/n]')
				if osu_songs_path_confirm.lower() == 'y' or osu_songs_path_confirm.lower() == 'yes' or osu_songs_path_confirm.lower() == '':
					correct_osu_songs_path = True
					set_setting('osu_song_dir', osu_songs_path)
				# else:
				# 	print(f'If you checked this as correct, you are wrong. The path {osu_songs_path} does not exist')
				# 	time.sleep(2)

			flush()

			while not correct_danser_exe_path:
				flush()
				while True:
					try:
						danser_exe_path = settings_session.prompt(' Enter the path to your danser.exe (ex: C:/Users/you/danser-x.y.z-platform/danser.exe) ')
					except KeyboardInterrupt:
						pass
					else: 
						break
				danser_exe_path_confirm = input(f' You entered {danser_exe_path}. Is this correct [Y/n] ')
				if danser_exe_path_confirm.lower() == 'y' or danser_exe_path_confirm.lower() == 'yes' or danser_exe_path_confirm.lower() == '':
					correct_danser_exe_path = True
					set_setting('danser_exe', danser_exe_path)

			set_setting('has_changed_settings', 'true')

			flush()

		flush()
		beatmaps = get_beatmaps()
		map_history = InMemoryHistory()

		short_to_long_map_dict = {}
		
		for beatmap in beatmaps:
			try:
				map_history.append_string(format_beatmap_name(beatmap))
				short_to_long_map_dict[format_beatmap_name(beatmap)] = beatmap
			except:
				pass

		map_session = PromptSession(
			history=map_history,
			auto_suggest=AutoSuggestFromHistory(),
			enable_history_search=True
		)

		correct_map = False

		print(' This section has autocomplete!\n To use, simply start typing the map / difficulty name, and a suggestion will appear.\n To accept the suggestion, press the arrow right key on your keyboard.\n (Continuing in 7s)')
		time.sleep(7)

		while not correct_map:
			flush()
			while True:
				try:
					map = map_session.prompt(' Beatmap: ')
				except KeyboardInterrupt:
					pass
				else:
					break
			
			flush()

			map_confirm = input(f' You chose {map}. Is this correct [Y/n] ')
			if map_confirm.lower() == 'y' or map_confirm.lower() == 'yes' or map_confirm.lower() == '':
				correct_map = True

			flush()

		if map in short_to_long_map_dict.keys():
			diffs = get_diffs(short_to_long_map_dict[map])
			diff_history = InMemoryHistory()
			for diff in diffs:
				diff_history.append_string(diff)
			
		diff_session = PromptSession(
			history=diff_history,
			auto_suggest=AutoSuggestFromHistory(),
			enable_history_search=True
		)

		correct_diff = False

		while not correct_diff:
			flush()
			while True:
				try:
					diff = diff_session.prompt(' Difficulty: ')
				except KeyboardInterrupt:
					pass
				else:
					break
			
			flush()

			diff_confirm = input(f' You chose difficulty {diff}. Is this correct [Y/n]')
			if diff_confirm.lower() == 'y' or diff_confirm.lower() == 'yes' or diff_confirm.lower() == '':
				correct_diff = True


		print(f'Running Danser for {map} {diff}')

		danser_friendly_name = map.split(' - ')[0]
		open_danser(danser_friendly_name, diff)
		

if __name__ == '__main__':
	main()
