import os
from icecream import ic

def main():
    path1 = os.path.abspath("./")
    path2 = os.path.abspath("../")
    path3 = os.path.abspath("./Startup/")
    ic(path1)
    ic(path2)
    ic(path3)

try: 
    main()
except KeyboardInterrupt:
    print("Error")