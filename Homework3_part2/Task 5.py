'''
import data

End Gool:
    a dicturnary | key = Year and Value = list of month averges

X0. create object for every day
1. calculate month everige vor all monthe in data set 
2. split data in to years
3.creat dicturnary

2024-06-27;00:00:00;15.3;G
1 3 5 7 9 2 4 6 8 1 3 5 7
 2 4 6 8 1 3 5 7 9 2 4 6 8
'''
def main():
    selected_year = 1999
    projectpath = "/home/vincentl/Documents/LNU/LNU_Python_Corse/Homework3_part2/"
    datafil_name = "smhi-opendata_1_64510_20241007_132504.csv"
    input_string = loud_data_file(projectpath + datafil_name)
    list_of_days = seperate_to_One_day_one_Obj(input_string)
    tabel_of_object = convert_to_tabel(list_of_days)
    lookup_dicturnary = caluculate_monthe(tabel_of_object)
    output(lookup_dicturnary,selected_year)
    #output_to_file(selected_year,projectpath,lookup_dicturnary)


def loud_data_file(lokation):
    data = open(lokation)
    data = data.read()
    return data

def convert_to_tabel(list_obj):
    tabel = []
    for obj in list_obj:
        #remove unused data
        obj = obj.strip(";G") 
        obj = obj.strip(";Y")
        #splitdata up
        colum = (obj.split(";"))
        tabel.append(colum)
    return tabel

def seperate_to_One_day_one_Obj(string_input):
    main_list = (string_input.split("\n"))
    #remove emty enteries
    main_list.remove("")
    return main_list

def caluculate_monthe(list_of_days):
    count = 0
    mounth_averig = 0
    lookup_dicturnarry = {}
    mounth_list = []
    
    year = list_of_days[0][0][0:4]   #select first ellement of array, than the date and than splitt Year
    mounth = list_of_days[0][0][5:7] #select first ellement of array, than the date and than splitt mounth
    #year = "1999"
    #mounth = "11"

    for row in list_of_days: #go thru all rows
        if  year == row[0][0:4]: # check if it is still the same Year
            print(year)
            
            if mounth == row[0][5:7]: #check if its still the same month
                count += 1
                mounth_averig += float(row[2])
            else: 
                mounth_list.append((mounth,mounth_averig/count))
                #reset counting for avergies
                count = 0
                mounth_averig = 0
                #move to next mounth
                mounth = row[0][5:7]
        else:
            #update the list & dicturnary
            mounth_list.append((mounth,mounth_averig/count))
            lookup_dicturnarry.update({int(year):mounth_list})
            #reset value for next mounth
            count = 0
            mounth_averig = 0
            mounth_list = []
            #moving on to next mounth & Year
            mounth = row[0][5:7]
            year = row[0][0:4]
    return lookup_dicturnarry
            
#creat terminal output
def output(lookup, selected):
    print(f"Average Tempertures for {selected}")
    selected_year = lookup[selected]
    for e in selected_year:
        print(f"Mounth {e[0]}: {e[1]:.2f}°C")

#creat output in File
def output_to_file(name,path,lookup):
    file = open(path + str(name) + ".txt","w")
    selected_year = lookup[name]
    cash_for_file = ""
    for e in selected_year:
        cash_for_file += f"Mounth {e[0]}: {e[1]:.2f}°C \n"
    file.write(cash_for_file)
    file.close()
            
main()
