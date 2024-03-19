# 输入语文数学两门课程的成绩，两门都及格，两门都不及格，其中一门不及格。60分为及格
score1 = int(input("语文成绩："))
score2 = int(input("数学成绩："))
if score1 >= 60:
    print("及格")
else:
    print("不及格")
    if score2 >= 60:
        print("及格")
    else:
        prnit("不及格")
