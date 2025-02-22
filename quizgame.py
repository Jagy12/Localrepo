print("Welcome to the quiz game!!")
name=input("please enter your name: ")
status=input("do you want to continue? ")
if status.lower()=="yes":
    open("quizgame.html")
    score=0
else:
    quit()
    
# 0
Ques=input("Who's the President of India? ")
if Ques.lower()=="mr. narendra modi":
    print("Correct :)")
    score+=5
else:
    print("Incorrect Answer!")
# 1
Ques=input("Who is known as the Father of the Nation in India? ")
if Ques.lower()=="mahatma gandhi":
    print("Correct :)")
    score+=5
else:
    print("Incorrect Answer!")
#2
Ques=input("Which festival celebrates the victory of light over darkness and good over evil? ")
if Ques.lower()=="diwali":
    print("Correct :)")
    score+=5
else:
    print("Incorrect Answer!")
# 3
Ques=input("Which animal is considered the national animal of India? ")
if Ques.lower()=="tiger":
    print("Correct :)")
    score+=5
else:
    print("Incorrect Answer!")
# 4
Ques=input("Name the currency used in India.  ")
if Ques.lower()=="indian Rupee":
    print("Correct :)")
    score+=5
else:
    print("Incorrect Answer!")
# 6
Ques=input("Name the largest state in India by area. ")
if Ques.lower()=="rajasthan":
    print("Correct :)")
    score+=5
else:
    print("Incorrect Answer!")



print("Hey +name+ , You scored " + str(score))
print("Your pecentage is "+str(score/30 *100))

if score>=15:
   b = input("Congratulations! You have cleared round 1 🎉🎉🎉\nWould you like to continue? ")
if b.lower()=="yes":
    print("Ok let's continue!!")
else:
    exit()

# 1
Ques=input("Which famous monument in India is considered one of the Seven Wonders of the World? ")
if Ques.lower()=="the taj mahal":
    print("Correct :)")
    score+=10
else:
    print("Incorrect Answer!")

# 2
Ques=input("Who is known as the \"Missile Man of India\"?")
if Ques.lower()=="APJ Abdul Kalam":
    print("Correct :)")
    score+=10
else:
    print("Incorrect Answer!")
# 3
Ques=input("Which city is known as the \"Pink City\" of India?")
if Ques.lower()=="Jaipur":
    print("Correct :)")
    score+=10
else:
    print("Incorrect Answer!")
# 4
Ques=input("Who is the author of the famous book \"Harry Potter\" series? ")
if Ques.lower()=="J.K. Rowling":
    print("Correct :)")
    score+=10
else:
    print("Incorrect Answer!")
# 5
Ques=input("Which is the largest coffee-producing state in India? ")
if Ques.lower()=="Karnataka":
    print("Correct :)")
    score+=10
else:
    print("Incorrect Answer!")
# 6
Ques=input("Which Indian cricketer has scored the highest number of international centuries?")
if Ques.lower()=="Sachin Tendulkar":
    print("Correct :)")
    score+=10
else:
    print("Incorrect Answer!")
# 7
Ques=input("What is the national flower of India? ")
if Ques.lower()=="Lotus":
    print("Correct :)")
    score+=10
else:
    print("Incorrect Answer!")


print("Hey +name+ , You scored " + str(score))
print("Your pecentage is "+str(score/100 *100))



# way 2
print("Welcome to the quiz game!!")
name,status=input("please enter your name: "),input("do you want to continue?,yes or no: ")
if status.lower()=="yes":
    print("ok let's play")
    score=0
else:
    quit()
q=[("Who's the PM of India? ","Who is known as the Father of the Nation in India? ","Which festival celebrates the victory of light over darkness and good over evil? ","Which animal is considered the national animal of India? ","Name the currency used in India. ","Name the largest state in India by area. "),("Which famous monument in India is considered one of the Seven Wonders of the World? ","Who is known as the \"Missile Man of India\"?","Which city is known as the \"Pink City\" of India?","Who is the author of the famous book \"Harry Potter\" series? ","Which is the largest coffee-producing state in India?","Which Indian cricketer has scored the highest number of international centuries?","What is the national flower of India? ")]  
a=[("mr. narendra modi","mahatma gandhi","diwali","tiger","indian rupee","rajasthan"),("the taj mahal","apj abdul kalam","jaipur","j.k. rowling","karnataka","sachin Tendulkar","lotus")]
def myfn(x,y):
    global score
    for i in x:
        Ques=input(i[0])
        if Ques.lower()==i[1]:
            print("Correct :)")
            score+=y
        else:print("Incorrect Answer!")
myfn(list(zip(q[0],a[0])),5)
print(f"Hey {name} , You scored {str(score)}\nYour pecentage is "+str(score/30 *100) )
if score>=15:myfn(list(zip(q[1],a[1])),10)
print(f"Hey {name} , You scored {str(score)}\nYour pecentage is "+str(score/100 *100) )













    






