#Implementing a function that takes list of student scores
#display sum of scores which are above average 

student_scores = [80,60,50,65,75,55]
def sum_of_scores_above_average(p_student_scores):
    sum_scores = 0
    num_of_students = 0
    for score in p_student_scores:
        sum_scores += score
        num_of_students += 1
    average_score = sum_scores/num_of_students
    print(average_score)
    sum_above_average = 0
    for score in p_student_scores:
        if score > average_score:
            sum_above_average += score
    return sum_above_average

print(sum_of_scores_above_average(student_scores))
    














#num = [11,'sri',5.5,'true',2,234,6.7]
#for n in num:
#    if isinstance(n,int):
 #       print(n)

#create a list consists of names & implement  the for loop which prints hello before each name
