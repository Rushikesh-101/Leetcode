class Solution:
    def simplifyPath(self, path: str) -> str:
        List1 = []
        listpath = path.split("/")
        listpath = path.split("/")
        
        
        


        # Input - /home/user/Documents/../Pictures
        # Expected output : /home/user/Pictures


        for index, item in enumerate(listpath) :

            if item == ".." and len(List1):
                List1.pop()
                print("\n",List1)

            elif item == ".." and len(List1) == 0 :
                continue
                print("\n", List1)

           

            elif item == "." :
                # print("Not appending this item :")
                continue
                print("\n",List1)

            elif item == "/" :

                continue
                print("\n",List1)

            elif item == "" and len(List1) != 0  :

                continue 
                print("\n",List1)

            else : 
                List1.append(item)
                print("\n",List1)
   

        print("\n List1 before / pop : ", List1)


        
        #  if item == ".." and not len(List1):
        #         continue
                
        
        listpath = '/'.join(List1)
        

        if len(listpath) and listpath[-1] == "/"  :

            print("\n List1 before / pop : ", listpath)

            listpath = listpath[:-1]
            
            print("\n List1 after / pop : ", listpath)

        print("this is it: " , listpath , " this is that : ", listpath[-2:])   

        if listpath[-2:] == '..' and listpath[-3] == '/':
            
            
           

            if len(listpath) >= 3 and listpath[-3:] == '...' :
                pass

            else:
                listpath = listpath[:-2]
                print("After indicing : ", listpath)
            # return listpath

        if listpath == '' :
            return "/"
        
        elif  listpath[0] != '/' :
            return '/' + listpath

        else :
            return listpath
