# assumption: possibles times are between 0 and 23.

def load_agenda(file_name):
    result = []
    with open(file_name) as f:
        for line in f:
            fields = line.split()
            result.append((int(fields[0]),int(fields[1]),fields[2]))
    return result

def tabulate_agenda(agenda):
    # result = [[]] * 24 # WRONG because of sharing. We must use a loop here.
    result = []
    for i in range(0,24):
        result.append([])
    print (result)
    # here result is a list of empty lists of size 24.
    for (start,stop,task) in agenda:
        for t in range(start,stop+1):
            result[t].append(task)
    return result

# print(load_agenda("agenda.txt"))
print(tabulate_agenda(load_agenda("agenda.txt")))
