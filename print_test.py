
import os
import time
import string


#test git
def create_file(text):

    t = time.localtime()
    y, m, d, h, m, s = t[0], t[1], t[2], t[3], t[4], t[5]

    file_name = y, m, d, h, m, s
    file_name = ''.join(str(file_name)).replace(' ', '')

    for i in range(len(string.punctuation)):

        file_name = file_name.replace(string.punctuation[i], '')

    file_name = file_name + '.txt'

    file = open(file_name, 'w')
    file.write(text)
    os.system("rm %s" % file_name)

text = input()
create_file(text)
