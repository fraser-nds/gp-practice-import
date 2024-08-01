import csv
import urllib.request

practices = []
input_file = open("input/gpprac", "r")
NumberOfLines = len(input_file.readlines())
input_file = open("input/gpprac", "r")

for line_number in range(NumberOfLines):
    line = input_file.readline()
    practice = {}
    practice['code'] = line[1:6]
    practice['address1'] = line[6:41]
    practice['address2'] = line[41:76]
    practice["address3"] = line[76:111]
    practice["address4"] = line[111:146]
    practice["postcode"] = line[146:154]
    practice["is_active"] = True if len(line[183:191].strip()) == 0 else False
    practice['telephone'] = line[154:169].replace('NOT KNOWN', '11111 111111').replace('UNKNOWN', '11111 111111').replace("MISSING", '11111 111111').replace(" ", '')
    practices.append(practice)

keys = practices[0].keys() 
with open(f'output/gpprac.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(practices)


gps = []
input_file = open("input/gpref", "r")
number_of_lines = len(input_file.readlines())
input_file = open("input/gpref", "r")

for line_number in range(number_of_lines):
    line = input_file.readline()
    practice_code_of_gp = line[55:60]
    phoneNumberOfGp = ""

    with open("input/gpprac", 'r') as practice_file:
        while phoneNumberOfGp == "":
            practice_line = practice_file.readline()
            if practice_line == "":
                break
            practice_code = practice_line[1:6]
            telephone = practice_line[154:169].replace('NOT KNOWN', '11111 111111').replace('UNKNOWN', '11111 111111').replace("MISSING", '11111 111111').replace(" ", '')
            if practice_code == practice_code_of_gp:
                phoneNumberOfGp = telephone;

    gp = {}
    gp['first_name'] = line[32:52]
    gp['last_name'] = line[12:32]
    gp['telephone'] = phoneNumberOfGp
    gps.append(gp)

keys = gps[0].keys() 
with open(f'output/gpref.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(gps)
