#coding=utf-8
f = open("out.csv","w")
f.write('num' + ',' + 'start time' + ',' + 'end time' + '\n')  #write title

def find_match(line, string):
    match = ''
    pos = line.index(string) + len(string)
    for i in range(pos, len(line)):
        if line[i] == ',':
            break;
        match += line[i]
    return match

def get_time(file_name):
    num = 0
    for line in open(file_name + ".log","r"):
        num += 1
        try:
            start_time = find_match(line, "start time")
            print("start time = %s" % start_time)
            end_time = find_match(line, "end time")
            print("end time = %s" % end_time)
        except ValueError:
            num -= 1
            continue
        f.write(str(num) + ',' + start_time + ',' + end_time + ',' + '\n')
    f.close()

if __name__ == "__main__":
    get_time("test")
