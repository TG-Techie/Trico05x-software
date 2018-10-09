from os import listdir

modules = []

modules_list = listdir('./lib/tg_modules/gui_modules')
for module in modules_list:
    if module[0:2] != ('._' and '__'):
        try:
            modules.append(module.replace('.py',''))
            #print('from tg_modules.gui_modules.'+ module.replace('.py','') +' import *')
            exec('from tg_modules.gui_modules.'+ module.replace('.py','') +' import *')
        except ImportError:
            raise ImportError('TG: from tg_modules.gui_modules.'+ module.replace('.py','') +' import *')