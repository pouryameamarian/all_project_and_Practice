print('How much do you get paid per hour?:')
hour = input(int)

def salary (hour, money_of_timework):
    if hour < 7 :
        print ("You are very lazy")
    else:
     salary  = hour * money_of_timework
print (salary(5, 9))
