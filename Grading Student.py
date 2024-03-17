def gradingStudents(grades):
    res=[]
    for i in grades:
        if i>=38:
            a=i%5
            if a>=3:
                i+=(5-a)
        res.append(i)
    return res
    
