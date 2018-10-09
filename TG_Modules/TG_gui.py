from os import listdir

modules = []

modules_list = listdir('./lib/tg_modules/gui_components')
for module in modules_list:
    if module[0:2] != ('._' and '__'):
        modules.append(module.replace('.py',''))
        #print('from tg_modules.gui_components.'+ module.replace('.py','') +' import *')
        exec('from tg_modules.gui_components.'+ module.replace('.py','') +' import *')