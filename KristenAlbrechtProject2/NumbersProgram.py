
#calculate average
def getAverage(num):
    num  = [ int(x) for x in num ]
    a = sum(num)/len(num)
    return a

#calculate highest
def getLargest(num):
    highest = max(num)
    return highest

#calculate smallest
def getSmallest(num):
    smallest = min(num)
    return smallest

#check order
def isOrdered(num):
    for i in range(0, len(num)-1):
        if num[1] < num[i+1]:
            order = 'in ascending'    
        elif num[1] > num[i+1]:
            order = 'in descending'    
        else:
            order = 'out of'
                   
    return order

def main():        
    numInputs = input('Enter 5 numbers seperated by commas: ')
    
    #create numbres list  
    numbersList = list()
    for numInput in numInputs:
        num = numInputs.split(',')  
    
    #get average
    averageNum = getAverage(num)
    
    #get highest number
    highestNum = getLargest(num)
    
    #get smallest number
    smallestNum = getSmallest(num)
    
    #check order
    order = isOrdered(num)
            
    print("The average of the numbers is:"  ,averageNum, "\nThe highest number is:" ,highestNum, "\nThe smallest number is:" ,smallestNum, "\nThe numbers are" ,order, "order" )

#start program
main()

   
