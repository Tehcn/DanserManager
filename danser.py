from genericpath import exists
from logging import error
import os
from settings import get_setting

def open_danser(beatmap: str, diff: str, mods: list | None = None):
    danser_exe = get_setting('danser_exe')
    os.system(f'{danser_exe} -t="{beatmap}" -d="{diff}"')

