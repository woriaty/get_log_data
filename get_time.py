#coding=utf-8

import os

def find_match(line, string):
    match = ''
    pos = line.index(string) + len(string)
    for i in range(pos, len(line)):
        if line[i] == ',':
            break;
        match += line[i]
    return match

def get_time(file):
    num = 0
    value = ''
    for line in open(file,"r"):
        num += 1
        try:
            start_time = find_match(line, "start time")
            #print("start time = %s" % start_time)
            end_time = find_match(line, "end time")
            #print("end time = %s" % end_time)
        except ValueError:
            num -= 1
            continue
        value += (str(num) + ',' + start_time + ',' + end_time + ',' + '\n')
    return value

def find_exist(file, files):
    pos = file.find('.log')
    for i in range(len(files)):
        if files[i] == file[:pos]+ ".csv":
            return -1
    return 0

if __name__ == "__main__":
    files = os.listdir()
    for i in range(len(files)):
        pos = files[i].find('.log')
        if pos != -1:
            print("match file: %s" % files[i])
            if find_exist(files[i], files) == -1:
                print("file %s.csv exist, ignored..." % files[i][:pos])
                continue
            f = open(files[i][:pos]+ ".csv","w")
            f.write('num' + ',' + 'start time' + ',' + 'end time' + '\n')  #write title
            f.write(get_time(files[i]))
            f.close()
