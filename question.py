
import random
from guizero import App, Text, PushButton, TextBox

questions = []
r1 = []
r2  = []
r3 = []
with open("greetings.csv") as f:
	for line in f:
		senc = line.split(",")
		questions.append(senc[0])
		r1.append(senc[1])
		r2.append(senc[2])
		r3.append(senc[3])
		print(line[:10])


def question():
	a = random.randint(0, len(questions)-1)
	return a



b = question()	

   
	
def message():
    global b
    b = random.randint(0, len(questions)-1)
    ran = questions[b]
    messages.value = ran
    print(messages.get())
    test.value = 'enter another response'
    
app = App("How to make friends")

def answer():
    messages.value +=  "\n\n here are some other responeses: \n\n\n" + r1[b] + '\n\n' + r2[b] + '\n\n' + r3[b]

button = PushButton(app, message, text="new question")
test = TextBox(app, text="enter your response...", width="60")
messages = Text(app, text=questions[b], color="black")
b3 = PushButton(app, answer, text="answer")
app.display()

	
	