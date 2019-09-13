import os
    


def create_directory(path):
    if os.path.exists(path):
        return (path,True)
    else:
        return ("No such a file Directory",False)



def create_file(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            raise Exception("File cannot be created within file")
        else:
            return (path,True)
    else:
        return ("No such a file Directory",False)


def list(path):
    list_path = {'Directory':[],'File':[]}
    for item in os.listdir():
        if os.path.isdir(item):
            list_path['Directory'].append(item)
        elif os.path.isfile(item):
            list_path['File'].append(item)

    return list_path


def check_existence(item):
    for (root,dirs,files) in os.walk('/home', topdown=True): 
        if item in dirs or item in files:
            return True


    return False

def search(path,string):
    result = []
    for (root,dirs,files) in os.walk(path, topdown=True): 

        for thing in dirs:
            if string == thing[len(thing)-3:]:
               result.append(thing)
        for thing in files:
            if string == thing[len(thing)-3:]:
               result.append(thing)
            
    return result
