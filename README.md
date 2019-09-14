# DirStruct
Implementation of a directory structure for a Linux Based operaing System and Performing some tasks

Assignment (string_list_dict):
Name : Implement a directory structure for a Linux Based opera ng System. You are not suppose to create actual files or directories. You should only give
the implementa on of the Directory Structure like how would a directory Structure look if I create a Directory. I will give you the output in detail. You can
assume that there exist no Directory Structure in the beginning.
Tasks :

  1. Create a Directory
    a. Input – Absolute Path String – Example create_directory(“/home/prathiba/mydirectory/”)
    b. Output – Tuple or Pair (string,bool) indica ng (path,True) or (“No such file or Directory”, False)
  
  2. Create a File within a Directory
    a. Input – Absolute Path String – Example create_file(“/home/prathiba/mydirectory/”)
    b. Output – Tuple or Pair (string,bool) indica ng (path,True) or (“No such file or Directory”, False)
    c. Note that if you are trying to create a file within a file, it should throw an excep on

  3. List at a par cular path
    a. Input – Absolute Path String – Example list(“/home/prathiba/mydirectory/”)
    b. Output – Key value pair (Type:list(string)) indica ng the files and directories in that path

  4. Check if a file/directory exists in the directory structure.
    a. Input – String – Example check_existence(“mydirectory”)
    b. Output – True/False

  5. Search a file or a directory in the en re structure star ng from that path.
    a. Input - String - Example search("path", "searchstring"). search("/", "ssh")
    b. Output - Print all the paths which ends with the searchstring
    /run/user/1000/keyring/ssh
    /snap/core18/1098/etc/default/ssh
    /snap/core18/1098/etc/init.d/ssh
    /snap/core18/1098/etc/ssh
    /snap/core18/1098/usr/bin/ssh
    /snap/core18/1074/etc/default/ssh

# Requirements

## Langauge
Python is an interpreted, high-level, general-purpose programming language.Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. 

## Installination

```bash
sudo apt install python3
```
## Data structures
Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
List

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
Example

Create a List:

```python
thislist = ["apple", "banana", "cherry"]
```

# How to Use
1.Run main.py  
2.Select the operation by inputing number between 1-6  
3.Give necessary input for operation  
4.Observe the output  


# How It works

## 1.Creating Directory

---
if path is not starting with '/' then return false
traverse tree till path  
  if any directory in path does not exits then return false  
  
  if path contains file in between then return false  
  
  if path exists create directory and return true  
  
---

## 2.Creating File  

---
Same as creating directory   

---

## 3.list  

---
traverse down the tree till path  
for children in path    
  append path to child according to type  
  
---

## 4.Checking existence
---
start from root node  
for children in root  
  if child is directory  
      repeat step 2  
  if child is matching with input return true  
return false  

---


## 5.searching
---
traverse down the tree till path
for children in path    

  if child is directory  
      repeat step 2  
  if child is matching with input return true  
return false  

---

## test.py
  It contains all classes,functions required for the operations.It is imported in main.py file  


# Time complexcity for each functions

# traverse

n - no of directory to traverse  
d - no of children in each directory while traversing  

O(nd)  


# create_directory

n - no of directory to traverse  
d - no of children in each directory while traversing  
k - no of children in last directory after traversing  
O(nd) + o(k)  


# create_file

n - no of directory to traverse  
d - no of children in each directory while traversing  
k - no of children in last directory after traversing  
O(nd) + o(k)  


# List

n - no of directory to traverse  
d - no of children in each directory while traversing  
k - no of children in last directory in path after traversing  

O(nd) + o(k)


# check_existence 

let T(n) be no of elementary operations performed by check()  
if d is no of children in each directory while traversing ,  
check() is called d no of times for each directory  

O(d)  


# Search

#For traversing till path  
n - no of directory to traverse  
d - no of children in each directory while traversing  

O(nd)  


#for searching
let T(n) be no of elementary operations performed by check()  
if k is no of children in each directory while traversing ,  
check() is called k no of times for each directory  

O(k)


total = O(nd) + O(k)  






















  
# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
