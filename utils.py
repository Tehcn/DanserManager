import os
import re
from settings import get_setting

def get_beatmaps():
    return os.listdir(get_setting('osu_song_dir'))

def get_diffs(beatmap: str):
    diffs = []
    for file in os.listdir(get_setting('osu_song_dir') + f'/{beatmap}'):
        if file.endswith('.osu'):
            diffs.append(re.search('\[(.*)\]\.osu', file).group(1))
    return diffs

def format_beatmap_name(name: str):
    return name.split(' ', 1)[1].split(' - ')[1] + ' - ' + name.split(' ', 1)[1].split(' - ')[0]

def flush():
    pass