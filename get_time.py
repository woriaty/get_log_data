#coding=utf-8
f = open("out.csv","w")
f.write('start time' + ',' + 'end time' + '\n')  #write title
data = ""
time = {'start':'','end':''}
num = 0
start = 0
end = 0
for line in open("test.txt","r"):
    for i in range(len(line)):
        if line[i:i+10] == "start time":
            start = i+11
            i = start
        if line[i:i+8] == "end time":
            start = i+9
            i = start
        if line[i] == ',' and start != 0:
            end = i
            data = line[start:end]
            if num == 0:
                time['start'] = data
                f.write(time['start'] + ',')
                print("start_time = %s" % time['start'])
                num += 1
            else:
                time['end'] = data
                f.write(time['end'] + ',' + '\n')
                print("end_time = %s" % time['end'])
                num = 0
            start = 0
f.close()
