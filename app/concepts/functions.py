#given an array of grades calculate the gpa
#they all have the same weight

# A-> 4.0
# B-> 3.0
# C-> 2.0
# D-> 1.0
# F-> 0.0

def translate_letter_to_num(letter):
    if letter=="A":
        return 4.0
    if letter=="B":
        return 3.0
    if letter=="C":
        return 2.0
    if letter=="D":
        return 1.0
    return 0.0

def translate_letter_array_to_num_array(letter_arr):
    num_arr = []
    for letter in letter_arr:
        num = translate_letter_to_num(letter)
        num_arr.append(num)
    return num_arr


def arr_sum(num_arr): 
    solution =0
    for num in num_arr:
        solution+=num
    return solution

def gpa(arr):
    numeric_grade_values= translate_letter_array_to_num_array(arr)
    grade_sum = arr_sum(numeric_grade_values)
    number_of_classes = len(numeric_grade_values)
    return grade_sum/number_of_classes


grades = ["A","B","B","C","A"]
print(gpa(grades))
    