''' this is a module designed to handle keeping programs in ram '''
import sys
from tg_Modules.tg_tools import holder

#ordered list
buffer = []

#current program
cur_prog = None
#curent container in prog
cur_cont = None

#two places to hold programs
system = holder()
programs = holder()

def _import(prog_name, path = 'programs', to_system = 0):
    try:
        #import the module
        exec('from '+path+' import '+prog_name)
        
        programs.add(prog_name,eval(prog_name))
        if to_system:
            system.add(prog_name,eval(prog_name))
        else:
            global buffer
            buffer.append(prog_name)
        
    except MemoryError:
        unload(-1)
        _import(prog_name, path, target)
        
def load(*args):
    for prog_name in args:
        #try:

            if not hasattr(programs,prog_name):
                _import(prog_name)
            
            global buffer
            try:
                buffer.insert(0,buffer.pop(buffer.index(prog_name)))
            except:
                pass
                
            
            global cur_prog
            global cur_cont
            if cur_prog != programs.get(prog_name):
                try:
                    cur_cont.clear()
                except:
                    pass
            
            cur_prog = programs.get(prog_name)
            cur_cont = cur_prog.container
            
            cur_cont.place()
            
        #except:
            #print('TG:HandlerError: unable to load: '+prog_name)
        
def unload(*args):
    for prog_id in args:
        for target in (programs,system):
            try:
                try:
                    _unimport(prog_id,target)
                    buffer.pop(buffer.index(prog_id))
                except AttributeError:
                    _unimport(buffer[prog_id],target)
                    buffer.pop(buffer[prog_id])
                break
            except:
                continue
            

def _unimport(prog_name, target = programs):
    target.delete(prog_name)
    exec('del '+prog_name)
    #print(dir())

def load_system_prog(*args):
    for prog_name in args:
        _import(prog_name, path = 'system.programs', to_system = 1)
        load(prog_name)
            

'''# the real load function that fetches from the programs directory
def _load(prog_name, to_system = 0):
    #try:
        try:
            global prog_order
            
            # if system is true then it will auto switch to ssytem.programs else programs
            import_cmd = 'from '+'system.'*to_system+'programs import '+prog_name
            #print(prog_name, to_system,(import_cmd))
            exec(import_cmd) 
            #print(eval(prog_name))
            #print('evaling: ','from '+'system.'*system+'programs.'+prog_name+' import container as '+prog_name)
            
            #prog_dict[prog_name] = eval(prog_name)
            #programs.add(prog_name, eval(prog_name))
            
            if to_system:
                system.add(prog_name,eval(prog_name))
                #print('added to system')#, programs.contents)
                
            else:
                programs.add(prog_name,eval(prog_name))
                #print('added to programs')#, system.contents)
                
        except MemoryError:
            unload(-1)
            _load(prog_name, to_system = to_system)
        #load(prog_name)
    #except:
        #output = 'TG:HandlerError: unable to load  "'+prog_name
        #output += '", not in lib/'+'system/'*to_system+'programs'
        #raise ImportError(output)
    

# a resume function that will load if teh program is not already in ram
def load(*args):
    for prog_name in args:
        try:
            global prog_order
            global cur_prog
            global cur_cont
            
            #clear the old program
            try:
                cur_prog.clear()
            except:
                pass
            
            #resume the desired prog
            try:
                prog_order.insert(0, prog_order.pop(prog_order.index(prog_name)))
            except:
                pass
            
            try:
                cur_prog = programs.get(prog_name)
            except:
                cur_prog = system.get(prog_name)
            
            #print(cur_prog)
                
            cur_cont = cur_prog.container
            cur_cont.place()
            
        except:
            _load(prog_name)
            load(prog_name)
        cur_cont.place()

def unload(*args):
    for prog_name in args:
        
        if prog_dict[prog_name] == cur_prog:
            cur_prog.clear()
        
        error = 0
        
        try:
            programs.delete(prog_name)
        except:
            try:
                programs.delete(prog_name)
            except:
                error = 1 

        if error:
            raise RuntimeError('TG:HandlerError: unable to unload  "'+prog_name+'", not loaded?')

def load_system_prog(*args):
    for prog_name in args:
        _load(prog_name, to_system = True)
        #load(prog_name) '''