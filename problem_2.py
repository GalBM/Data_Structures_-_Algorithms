import  os
def find_files(suffix=None, path=None):
    #if input is null
    if suffix==None or path==None:
        return "please insert appropriate input"
    list_path=[] ## define global variable
    #test case- if the path is exists
    if os.path.isdir(path)==False:
        return "Path isn't exist"
    def recurse(suffix, path):
        ## break case- if the path is file-> return and if the suffix fit it appent to the global list
        if os.path.isfile(path):
            if path.endswith(suffix):
                return list_path.append(path)
            else:
                pass
        ## the reucrsive part-> call the function every time the path isnt file
        if os.path.isdir(path):
            for dir in os.listdir(path):
                recurse(suffix,os.path.join(path,dir))
        return
    recurse(suffix, path)
    return list_path

#test1- right path
print(find_files('.c', "D:\\python\\Atestdir"))
# expect to get:
# ['D:\\python\\Atestdir\\subdir1\\a.c','D:\\python\\Atestdir\\subdir3\\subsubdir1\\b.c',
#  'D:\\python\\Atestdir\\subdir5\\a.c','D:\\python\\Atestdir\\t1.c']

#test 2- righ path with non-exist suffix
print(find_files('.dc', "D:\\python\\Atestdir"))
# expect to get: []

#test3- wrong path
print(find_files('.c', "D:\\python\\Atestdirwrong"))
# expect to get: "Path isn't exist"

#test4- Null path
print(find_files())
# expect to get: "please insert appropriate input"
