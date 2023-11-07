#CTI-110
#P4HW1 - Score List
#William Snipes
#11/2/2023
#

#How many Scores do you want to enter? 5

#Enter Score #1: 67
#Enter score #2: 75
#Enter Score #3: -1

#INVALID Score entered!!!!
#Score should be between 0 and 100
#Enter Score #3 again: 86
#Enter Score #4: 45
#Enter Score #5: 90

#--------------Results--------------
#Lowest Score   : 45.0
#Modified List  : [67.0, 75.0, 86.0,90.0]
#Scores Averange: 79.50
#Grade          : C

num_of_scores = int(input("How many scores do you want to enter? "))
score_list = []

for i in range(1, num_of_scores + 1):
    while True:
        score = float(input(f"Enter Score #{i}: "))        
        if 0 <= score <= 100:
            score_list.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
    
print("\n--------------Results--------------")
print(f"Lowest Score   : {min(score_list)}")
print(f"Modified List  : {score_list}")
print(f"Scores Average : {sum(score_list) / len(score_list):.2f}")
average_grade = ""
average_score = sum(score_list) / len(score_list)
if average_score >= 90:
    average_grade = 'A'
elif 80 <= average_score < 90:
    average_grade = 'B'
elif 70 <= average_score < 80:
    average_grade = 'C'
elif 60 <= average_score < 70:
    average_grade = 'D'
else:
    average_grade = 'F'
print(f"Grade          : {average_grade}")
print("------------------------------------")
