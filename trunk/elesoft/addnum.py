import string
from eledef import *
def run():
    print '''ENTER THE INTEGERS
ONE FOR EACH LINE
TYPE ANYTHING ELSE TO EXIT:'''
    sum = 0
    num = eleinput()
    while num not in {'EXIT', 'Q'} and num.isdigit():
        sum = sum + string.atol(num)
        num = eleinput()
    print 'SUM =', sum
