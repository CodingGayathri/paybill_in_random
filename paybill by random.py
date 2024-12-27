#y entering the list i=of names we will get who will pay the bill in random way
# it is like a game between the friends who will pay the bill
import random
name=input("enter everyones name separated by comma: ")
name_list=name.split(",")
print(name_list)
length=len(name_list)
random_choice=random.randint(0,length-1)
print(f"{name_list[random_choice]} will pay the bill")

