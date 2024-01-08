
import grade_calc as ut

def main():
    file_name = input("Please give the .csv file name: ")
    grade_list = ut.file_to_list(file_name)
    grade_dict = ut.list_to_dict(grade_list) 

    print(grade_dict) 

if __name__ == "__main__":
    main()

