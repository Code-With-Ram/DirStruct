

class Node(object):
    
    start = None            #Reference to root 

    def __init__(self, data,Type,path=None):
        self.name = data        #Name of Directory or file
        self.children = []      #Contents if node is directory
        self.type = Type        #Type :- Directory / File 
        self.path = path        #path to Directory / File

    def is_leaf(self):              #to check if node is external or not
        return (self.children==[])

        
    def create_directory(self, path):

        if path[0] !='/':       #if path not starting  with '/'
            return ("No such a file or Directory",False)

        #Get the reference to last directory of path 
        pathob,ispath = self.traverse(path.split('/')[:-1]) 

        #if path is valid create directory and add it 
        if ispath:

            #check if directory already exists
            for d in pathob.children:
                if d.name[0] == path.split('/')[-1:][0]:
                    return ("Directory already exists ",False)
            o = Node(path.split('/')[-1:],'Directory')
            o.path = path
            pathob.children.append(o)
            return (path,True)
        else:
            return ("No such a file or Directory",False)


    def create_file(self, path):
        pathob,ispath = self.traverse(path.split('/')[:-1])
        if ispath:
            
            #check if File already exists
            for d in pathob.children:
                if d.name[0] == path.split('/')[-1:][0]:
                    return ("File already exists ",False)

            o = Node(path.split('/')[-1:],'File')
            o.path = path
            pathob.children.append(o)
            return (path,True)
        else:
            return ("No such a file or Directory",False)
            

    #Traverse tree from root till the end of path and returns path object (Node),path exists or not (bool)
    def traverse(self,path):  

        if not path:    #if path is empty
            return None,False

        path[0] = '/'   #set of starting of path as root '/'
        p = Node.start  
        masterpath = path[:] #hold a copy of path

        #removing null values
        for k in path:
            if k=='':
                path.remove(k)
                
        while not p.is_leaf():  
            o = p
            if path==['/']:  
                break
            
            #for every child reference in directory p
            for d in p.children:
                
                #if path consists of file
                if d.type =="File" and d.name[0] in path:  
                    raise Exception("File cannot be created within file")
                    return None,False

                #if child exists in path assign d to p
                #remove name of directory from path
                if d.name[0] in path:
                    p = d
                    path.remove(d.name[0])

            #In case none of children matching directories in path
            #invalid directory name in path        
            if o == p:
                break

        #if name of directory at the end of path and p.name is matching ==>success traversal    
        if p.name[0] == masterpath[len(masterpath)-1]:


            return p,True
        else:
            return None,False

                
    #List all directories and files in path
    def list(self,path):
        if path[len(path)-1]!='/':
            path+='/'
        #Get the reference to last directory of path 
        pathob,ispath = self.traverse(path.split('/')[:-1])

        #To hold the result
        list_path = {'Directory':[],'File':[]}

        #if path is valid
        if ispath:
            for o in pathob.children:
                if o.type=='File':
                    list_path['File'].append(o.name)
                    
                elif o.type=='Directory':
                    list_path['Directory'].append(o.name)

        return list_path
    

    def check_existence(self,item):

        #start from '/'
        p = Node.start

        #flag for existence
        flag = [False]

        #checks for existence of item recursively        
        def check(o,item):

            if o.name[0] == item:
                flag[0] = True

            #if o is directory traverse it
            if o.type =='Directory':
                for s in o.children:
                    check(s,item)
                    
        check(p,item)            
        return flag[0]


    #searches for string in file  and returns path for file    
    def search(self,path,string):

        if path[len(path)-1]!='/':
            path+='/'
        result = []
        #Get the reference to last directory of path 
        pathob,ispath = self.traverse(path.split('/')[:-1])

        def check(o,item):

            #if Directory/file is ending with string 
            if o.name[0][len(o.name)-len(string)-1:] == string:
                result.append(o.path)

            #if its directory traverse it    
            if o.type =='Directory':
                for s in o.children:
                    check(s,string)
            
        check(pathob,string)


        #Display the result 
        for r in result:
            print(r)
        
