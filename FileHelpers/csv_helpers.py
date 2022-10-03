import csv

def write_csv(file_path:str,row_lists:list):
    # open the file in the write mode
    with open(file_path, 'a+', encoding='UTF8',newline="") as f:
        # create the csv writer
        writer = csv.writer(f)
        for row in row_lists:
            # write a row to the csv file
            writer.writerow(row)

def read_csv(file_path:str)->list:
    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f)
        list_new = []
        for line in csv_reader:
            list_new.append([int(line[0]),float(line[1]),line[2],float(line[-1])])
    return list_new

def compare_list_by_index(csv_1:str,csv_2:str)->list:
    my_list_1:list = read_csv(csv_1)
    my_list_2:list = read_csv(csv_2)
    new_list:list = []
    for i in range(0,len(my_list_1)-1):
        if my_list_1[i][-1]>my_list_2[i][-1]:
            new_list.append(my_list_2[i])
        else:
            new_list.append(my_list_1[i])
    return new_list