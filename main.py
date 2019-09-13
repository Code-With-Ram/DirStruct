import test


while True:

  choice = int(input("Enter your Choice \n 1.Create Directory\n2.Create File\n3.List \n 4.Check Existence \n 5.Search\n6.Exit"))
  if choice == 1:
        path = input("Please Enter path for Creating directory")
        print(test.create_directory(path))
  elif choice == 2:
        path = input("Please Enter path for creating File")
        print(test.create_file(path))
  elif choice == 3:
        path = input("Please Enter path for Listing directories and files")
        print(test.list(path))
  elif choice == 4:
        item = input("Please Enter Directory/File")
        print(test.check_existence(item))
  
  elif choice == 5:
        path = input("Please Enter path for searching File")
        item = input("Please Enter string to search")
        print(test.search(path,item))
  elif choice == 6:
        print("Bye Bye")
        sys.exit()      

  print()
    
