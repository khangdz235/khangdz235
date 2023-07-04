import speech_recognition
import pyttsx3
from datetime import date, datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id)
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you=""
    print("You: " + you)




    if "hello" in you:
        robot_brain = "Hello KhangHandsome"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif you == "how are you":
        robot_brain = "I'm fine. Thank you and you?"
    elif you == "":
        robot_brain = "I can't hear you. Try again" 
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif you == "who is the president of America":
        robot_brain = "President america is Joe Biden"
    elif you == "am I handsome":
        robot_brain = "That right. Khang very handsome"
    elif "handsome" in you:
        robot_brain = "Khang very handsome"
    elif "bye" in you:
        robot_brain = "bye bye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Error! Please try again later"
    print("Robot:" + robot_brain)


    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()