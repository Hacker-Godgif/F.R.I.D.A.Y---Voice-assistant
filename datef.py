import datefinder
import winsound
import datetime

def alarm(text):
    dTimeA = datefinder.find_dates(text)
    for mat in dTimeA:
        print(mat)
    stringA = str(mat)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA = timeA[3:-3]
    minA = int(minA)
    


    while True:
        print("Your alarm is started now")
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('D:\\F.R.I.D.A.Y\\audio.wav',winsound.SND_LOOP)
            elif minA<datetime.datetime.now().minute:
                break    

#alarm("set alarm at 6:03 pm")        