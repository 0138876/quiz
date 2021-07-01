# roept mijn class genaamd Question van de file Question
from Question import Question

#string voor vraag 9 
str2 =  "In Python, 'Hello', is the same as"

# Vragen van de quiz  met opties gesorteerd (list start bij [0])
question_prompts = [
    '1.What is a correct syntax to output Hello World in Python? \n(a) print("Hello World") \n(b) echo "Hello World" \n(c) echo("Hello World"); \n(d) p("Hello World")\n\n',
    "2.How do you insert COMMENTS in Python code?\n(a) /*This is a comment*/ \n(b) #This is a comment \n(c) //This is a comment \n\n",
    "3.Which one is NOT a legal variable name?\n(a) Myvar \n(b) _myvar \n(c) my_var \n(d) my-var \n\n",
    "4.How do you create a variable with the numeric value 5?\n(a) Both the other answers are correct \n(b) x = int(5) \n(c) x = 5 \n\n",
    "5.What is the correct file extension for Python files?\n(a) .pt \n(b) .pyth  \n(c) .py \n(d) .pyt \n\n",
    "6.How do you create a variable with the floating number 2.8?\n(a) x = float(2.8) \n(b) x = 2.8 \n(c) Both the other answers are correct \n\n",
    "6.What is the correct syntax to output the type of a variable or object in Python? \n(a) print(typeof x) \n(b) print(typeof(x)) \n(c) print(typeOf(x)) \n(d) print(type(x)) \n\n",
    "8.What is the correct way to create a function in Python?\n(a) create myFunction(): \n(b) def myFunction(): \n(c) function myfunction(): \n\n",
    "9."+ str2 + '"hello"\n(a) True \n(b) False \n\n',
    '10.What is a correct syntax to return the first character in a string?\n(a) x = sub("Hello", 0, 1) \n(b) x = "Hello".sub(0, 1) \n(c) x = "Hello"[0] \n\n',
    "11.Which method can be used to remove any whitespace from both the beginning and the end of a string?\n(a) len() \n(b) ptrim() \n(c) trim() \n(d) strip()\n\n",
    "12.Which method can be used to return a string in upper case letters?\n(a) toUpperCase() \n(b) upperCase() \n(c) upper() \n(d) uppercase()\n\n",
    "13.Which method can be used to replace parts of a string?\n(a) replace()  \n(b) switch() \n(c) repl() \n(d) replaceString()\n\n",
    "14.Which operator is used to multiply numbers?\n(a) X \n(b) # \n(c) *  \n(d) %\n\n",
    "15.Which operator can be used to compare two values?\n(a) <> \n(b) = \n(c) >< \n(d) == \n\n",
    '16.Which of these collections defines a LIST? \n(a) {"name": "apple", "color": "green"} \n(b) ["apple", "banana", "cherry"] \n(c) {"apple", "banana", "cherry"} \n(d) ("apple", "banana", "cherry")\n\n',
    '17.Which of these collections defines a TUPLE?\n(a) ("apple", "banana", "cherry") \n(b) {"name": "apple", "color": "green"} \n(c) {"apple", "banana", "cherry"} \n(d) ["apple", "banana", "cherry"]\n\n',
    '18.Which of these collections defines a SET?\n(a) ("apple", "banana", "cherry") \n(b) ["apple", "banana", "cherry"] \n(c) {"apple", "banana", "cherry"} \n(d) {"name": "apple", "color": "green"}\n\n',
    '19.Which of these collections defines a DICTIONARY?\n(a) ("apple", "banana", "cherry") \n(b) ["apple", "banana", "cherry"] \n(c) {"apple", "banana", "cherry"} \n(d) {"name": "apple", "color": "green"}\n\n',
    "20.Which collection is ordered, changeable, and allows duplicate members?\n(a) LIST \n(b) TUPLE \n(c) DICTIONARY \n(d) SET \n\n",
    "21.Which collection does not allow duplicate members?\n(a) SET \n(b) TUPLE \n(c) LIST \n\n",
    "22.How do you start writing an if statement in Python?\n(a) if (x > y) \n(b) if x > y then: \n(c) if x > y: \n\n",
    "23.How do you start writing a while loop in Python?\n(a) while (x > y) \n(b) while x > y: \n(c) while x > y { \n(d) x > y while { \n\n",
    "24.How do you start writing a for loop in Python?\n(a) for x > y: \n(b) for each x in y: \n(c) for x in y: \n\n",
    "25.Which statement is used to stop a loop?\n(a) exit \n(b) break \n(c) stop \n(d) return \n\n",

]

# Juiste antwoord gekoppeld aan vragen van de quiz (gesorteerde list vraag 1 is [0]) en de mogelijke opties beschickbaar
questions = [
     Question(question_prompts[0], "a", "a" "b" "c" "d"),  
     Question(question_prompts[1], "b", "a" "b" "c"),
     Question(question_prompts[2], "d", "a" "b" "c" "d"),
     Question(question_prompts[3], "a", "a" "b" "c"),
     Question(question_prompts[4], "c", "a" "b" "c" "d"),
     Question(question_prompts[5], "c", "a" "b" "c"),
     Question(question_prompts[6], "d", "a" "b" "c" "d"),
     Question(question_prompts[7], "b", "a" "b" "c"),
     Question(question_prompts[8], "a", "a" "b"),
     Question(question_prompts[9], "c", "a" "b" "c"),
     Question(question_prompts[10], "d", "a" "b" "c" "d"),  
     Question(question_prompts[11], "c", "a" "b" "c" "d"),
     Question(question_prompts[12], "a", "a" "b" "c" "d"),
     Question(question_prompts[13], "c", "a" "b" "c" "d"),
     Question(question_prompts[14], "d", "a" "b" "c" "d"),
     Question(question_prompts[15], "b", "a" "b" "c" "d"),
     Question(question_prompts[16], "a", "a" "b" "c" "d"),
     Question(question_prompts[17], "c", "a" "b" "c" "d"),
     Question(question_prompts[18], "d", "a" "b" "c" "d"),
     Question(question_prompts[19], "a", "a" "b" "c" "d"),
     Question(question_prompts[20], "a", "a" "b" "c"),
     Question(question_prompts[21], "c", "a" "b" "c"),
     Question(question_prompts[22], "b", "a" "b" "c" "d"),
     Question(question_prompts[23], "c", "a" "b" "c"),
     Question(question_prompts[24], "b", "a" "b" "c" "d"),

]

# Mijn input antwoorden komen hierin
myanswers = [

]


# Gaat de lijst af van vragen en vraagt mij om input antwoorden. voegt een punt toe aan score bij correct antwoord
# bij incorrect antwoord geeft hij fout aan en faat hij verder.
# Bij een antwoord die niet in mogelijke opties zitten herhaalt hij de vraag met de vraag kies een van de mogelijke optie
# slaat mijn antwoorden in myanswers=[] op

score = 0

def check_answer(current_question, user_answer):
    global score
    if user_answer == current_question.answer:
        score += 1
        myanswers.append(user_answer)
        print("Goede antwoord\n\n")
    elif user_answer in current_question.possible:
        myanswers.append(user_answer)
        print("Foute antwoord\n\n")
    else:
        print("\nKies een van de mogelijke optie")
        user_answer = input(current_question.prompt)
        check_answer(current_question, user_answer)

# zorgt ervoor dat de funtie check_answer geinitialiseerd wordt en dat de vragen gesteld worden
# zorgt global myanswers ervoor dat myanswers rewritable wordt en mijn antwoorden in opslaat                 
def run_quiz(questions):
    global myanswers
    for question in questions:
        answer = input(question.prompt)
        check_answer(question, answer)
    

# geeft mijn een beoordeling gebasseerd op mijn score
# geeft weer hoeveel vragen ik goed heb van het aantal vragen
    if score <= 13:
        print("Resultaat: \n","Onvoldoende \n je hebt", score , "van de" , len(questions) , "vragen goed\n\n")
    elif score in range(14,20):
        print("Resultaat: \n","Voldoende \n je hebt", score , "van de" , len(questions) , "vragen goed\n\n")
    else:
        print("Resultaat: \n","Goed \n je hebt", score , "van de" , len(questions) , "vragen goed\n\n")

#runs the quiz
run_quiz(questions)


# prints de vragen de goede antwoord en mijn antwoorden zodat ik kan controleren
print("Controleer jou antwoorden:\n")
def print_questions(questions):
    for i in range(len(questions)):
        print(questions[i].prompt , "Goede antwoord: " , questions[i].answer , " \n Jou antwoord: " , myanswers[i] , "\n")

# runs de print_question(questions) om de vragen de goede antwoord en mijn antwoorden in beeld te krijgen
print_questions(questions)

# loops back to the def run_quiz part en zorgt ervoor dat mijn gesavede antwoorden verwijderd worden
# 
def rerun_quiz(questions):
    restart = input("Do you wanna redo Quiz type yes or no\n").lower()
    if restart == "yes":
        print("\n")
        global score
        score = 0
        myanswers.clear()
        run_quiz(questions)
        print_questions(questions)
        rerun_quiz(questions)
    else:
        print("\n")
        exit()
        
# reruns the quiz
rerun_quiz(questions)

