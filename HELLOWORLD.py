#print('Hello World')
#name= input('what is your name?')
#print('Hello')
#print(name)
# the below print statement will give you an error because it's
#  already contains inside a single quote it will work if you double quote it.
#print("Hello it's a small world")
#first_name = 'Sushree'
#nick_name =' Rinky'
#print ('Hello' +first_name+''+nick_name)
#print(sentence.upper())
#print (sentence.lower())
#print(sentence.capitalize())
#print(sentence.count('a'))
#first_name ='Sushree'
#nick_name = 'Rinky'
#output = 'Hello, ' + first_name + ' ' + nick_name
#output = 'Hello {} {}'.format(first_name, nick_name)
#output = f'Hello {first_name} {nick_name}'
#print(output)
#When displaying a string that contains Numbers in that case we must convert the numbers into strings
#days_in_feb = 28
#print(str(days_in_feb) +'days_in_feb')
#first_num=input('Enter the first_number')
#second_number = input('Enter the second_number')

#print(int(first_num)+int(second_number))
#first_num = 5
#second_num = 10
#print(first_num ** second_num)

from datetime import datetime, timedelta

today = datetime.now()   

print('Today is: ' + str(today))

one_day = timedelta(days=1)
yesterday = today - one_day





