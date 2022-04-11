from logging import error

def get_settings():
    with open('settings.ini') as f:
        options = f.readlines()
        options_dict = {}
        numComments = 0
        for option in options:
            if option == '' or option == '\n' or options == '\r':
                continue
            if not option.startswith('#'):
                options_dict[option.split('=')[0]] = option.split('=')[1].replace('\n', '')
            else:
                options_dict[f'#{numComments} '] = option.split(' ')[1].replace('\n', '')
                numComments += 1
        return options_dict 

def get_setting(setting):
    if setting not in get_settings():
        error(f'Invalid setting \'{setting}\'')
    return get_settings()[setting]

def set_setting(setting, value):
    new_settings = get_settings()
    new_settings[setting] = value
    with open('settings.ini', 'w') as f:
        str = ''
        i = 0
        for setting, value in new_settings.items():
            if i != len(new_settings.items()):
                if type(value) == str:
                    str += f'{setting}=\'{value}\'\n'
                else:
                    str += f'{setting}={value}\n'
            else:
                if type(value) == str:
                    str += f'{setting}=\'{value}\''
                else:
                    str += f'{setting}={value}'
        f.write(str)