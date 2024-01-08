"""
Grade Distribution Calculator

Create 2 functions: file_to_list(file_name) and list_to_dict(grade_list) that converts the grade .csv file into a list and then that list into a dictionary respectively.
•	File_to_list
o	Takes file_name as an argument
o	Opens the file in read mode
o	Creates a blank list (grades_list)
o	Loops through line by line
o	Uses .split to split based on the comma and int(data[1].rstrip()) where data is the list you get after you split the line.
o	Appends just the score to the created list (grades_list)
o	Return the list to the main module
•	List_to_dict
o	Takes the grades_list as an argument
o	Creates a blank dictionary
o	Loops through each grade in the grade list
o	Uses if/elif/else logic to count the values up by 1 if that grade is above 90 (A), 80 (B), 70 (C), 60 (D), else (F) for each key (letter grade) in the dictionary.
o	Use .get to add to the count.   dict1[‘A’] = dict1.get(xx, x) + 1
o	Return the dictionary back to the main module
•	Main function
o	Get filename input from user, call both functions from imported utilities module, and print out the dictionary, which gives us the grade distribution

"""
def file_to_list(file_name):
    fh = open(file_name,'r')
    list1 = []
    for line in fh:
        data = line.split(",")
        list1.append(int(data[1].rstrip()))
        
    return list1

def list_to_dict(grade_list):
    dict1 = {}
    for grade in grade_list:
        if grade >= 90:
            dict1['A'] = dict1.get("A",0) + 1
            
        elif grade >= 80:
            dict1['B'] = dict1.get("B",0) + 1
            
        elif grade >= 70:
            dict1['C'] = dict1.get("C",0) + 1
            
        elif grade >= 60:
            dict1['D'] = dict1.get("D",0) + 1
        
        else:
            dict1['F'] = dict1.get("F",0) + 1
    
    
    return dict1