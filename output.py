import os
os.system("conda info --env > environments.txt")
os.system("conda list -n ulab_3.6 > ulab_3.6.txt")
os.system("conda list -n ulab_2.7 > ulab_2.7.txt")
