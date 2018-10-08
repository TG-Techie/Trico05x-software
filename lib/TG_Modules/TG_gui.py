from os import listdir
modules_list = listdir('./lib/tg_modules/gui_components')
for module in modules_list:
    if module[0:2] != '._':
        exec('from tg_modules.gui_components.'+ module.replace('.py','') +' import *')