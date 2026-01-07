m1, m2, m3, m4, m5 = map(int,input("ENter the subject marks: ").split())
marks = [m1, m2, m3, m4, m5]

if any(mark < 35 for mark in marks):
    print("fail")
else:
    avg_sum  = sum(marks)/5
    if avg_sum >=75:
        print("Distinct")
    else:
        print("pass")