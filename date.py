#!/bin/python3


from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    r1 = datetime.strptime(t1,fmt)
    r2 = datetime.strptime(t2,fmt)
    answ = int(abs((r1-r2).total_seconds()))
    return(answ)
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        print(time_delta(t1, t2))
