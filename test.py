def is_subset(test_list,sub_list):
    flag = 0
    if(all(x in test_list for x in sub_list)): 
        flag = 1

    return flag


class Node(object):
    start = None
    def __init__(self, data,Type,path=None):
        self.name = data
        self.children = []
        self.type = Type
        self.path = path
    def is_leaf(self):
        return (self.children==[])

        
    def create_directory(self, path):
        if path[0] !='/':
            return ("No such a file or Directory",False)

        pathob,ispath = self.traverse(path.split('/')[:-1])
        if ispath:
            o = Node(path.split('/')[-1:],'Directory')
            o.path = path
            pathob.children.append(o)
            return (path,True)
        else:
            return ("No such a file or Directory",False)

    def create_file(self, path):
        pathob,ispath = self.traverse(path.split('/')[:-1])
        if ispath:
            o = Node(path.split('/')[-1:],'File')
            o.path = path
            pathob.children.append(o)
            return (path,True)
        else:
            return ("No such a file or Directory",False)
            

    def traverse(self,path):
        if not path:
            return False

        path[0] = '/'
        p = Node.start
        masterpath = path[:]
        while not p.is_leaf():
            o = p
            if path==['/']:
                break
            for d in p.children:
                if d.type =="File" and d.name[0] in path:
                    raise Exception("File cannot be created within file")
                    return False
                   
                if is_subset(path,d.name):
                    p = d
                    path.remove(d.name[0])
            if o == p:
                break
        if p.name[0] == masterpath[len(masterpath)-1]:
            return p,True
        else:
            return None,False
                

    def list(self,path):
        pathob,ispath = self.traverse(path.split('/')[:-1])
        list_path = {'Directory':[],'File':[]}
        if ispath:
            for o in pathob.children:
                if o.type=='File':
                    list_path['File'].append(o.name)
                    
                elif o.type=='Directory':
                    list_path['Directory'].append(o.name)

        return list_path
    
    def check_existence(self,item):
        p = Node.start
        def check(o,item):
            if o.name == item:
                return True

            if o.type =='Directory':
                for s in o.children:
                    check(s,item)
                    
        check(p,item)
        return False

    def search(self,path,string):
        result = []
        pathob,ispath = self.traverse(path.split('/')[:-1])
        def check(o,item):
            
            if o.name[0][len(o.name)-len(string)-1:] == string:
                result.append(o.path)
            if o.type =='Directory':
                for s in o.children:
                    check(s,string)
            
        check(pathob,string)


        for r in result:
            print(r)
        

