import datetime
import random

def fortune_generator(): #creating a function
#keeping all the fortunes in a list
    fortunes = [
        " you will have a great day today",
        " you will meet your better half today",
        " you will be safe today",
        " you will come out of all difficutlies you faced all these while",
        " you will be healthy today",
        " Be careful with decisions today",
        " A Suprise will come to you today",
        " Someone will make you smile today",
        " Take a break a relax a while"
    ]

    #introduction message
    print("welcome to fortune_generator")
    #asking for the name
    name = input("enter your name :")

    #randomely picking forture from fortune list
    fortune = random.choice(fortunes)
    #capturing current date and formatting
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    print(f" Hello  {name}! here is your fortune for {current_time}" )
    print(f" {fortune}")

#calling function
fortune_generator()