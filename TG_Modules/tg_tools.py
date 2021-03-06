#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

from tg_modules.cp_cpython_add_backs import delattr

def get_direction(val):
    if val < 0:
        return -1
    elif val > 0:
        return 1
    else:
        return 0

class holder():
    def __init__(self):
        self.contents = []
    
    def __iter__(self):
        self._iter_count = 0
        return self 
    
    def __next__(self):
        if self._iter_count == len(self.contents):
            raise StopIteration
        else:
            self._iter_count += 1
            return self.contents[self._iter_count - 1]
            
        
    
    def add(self,name,prog):
        setattr(self,name,prog)
        self.contents.append(getattr(self,name))
        #print(self.contents)
    
    def delete(self,name):
        self.contents.pop(self.contents.index(getattr(self,name)))
        delattr(self,name)
        
    def get(self,target):
        return getattr(self,target)
