
# Subjects and Marks Example

subjects=["C","CPP","Java","Python","Oracle"]
marks=(80,30,20,10,20)

if all(marks):
    print("This Student Has no 0 marks in Any Subject...")
else:
    if marks.count(0)==1:
        print("This Student Has 0 Marks in - ",subjects[marks.index(0)])
    else:
        i=0
        while i<len(marks):
            if marks[i]==0:
                print("This Student Has 0 Marks in - ",subjects[marks.index(0,i)])
            i+=1
