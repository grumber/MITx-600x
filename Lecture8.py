# Problem 2

# Exceptions
##def FancyDivide(numbers,index):
##    try:
##        denom = numbers[index]
##        for i in range(len(numbers)):
##            numbers[i] /= denom
##    except IndexError, e:
##        print "-1"
##    else:
##        print "1"
##    finally:
##        print "0"

        
##def FancyDivide(numbers, index):
##    try:
##        try:
##            denom = numbers[index]
##            for i in range(len(numbers)):
##                numbers[i] /= denom
##        except IndexError, e:
##            FancyDivide(numbers, len(numbers) - 1)
##        else:
##            print "1"
##        finally:
##            print "0"
##    except ZeroDivisionError, e:
##        print "-2"

##def FancyDivide(list_of_numbers, index):
##    try:
##        try:
##            raise Exception("0")
##        finally:
##            denom = list_of_numbers[index]
##            for i in range(len(list_of_numbers)):
##                list_of_numbers[i] /= denom
##    except Exception, e:
##        print e


# Problem 3

def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):
    try:
        item / denom        
    except ZeroDivisionError, e:
        return 0        
    return item / denom
      

I need to re-study these functions
