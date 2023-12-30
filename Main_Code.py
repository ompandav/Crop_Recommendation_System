import pyttsx3  # Importing pyttsx3 library to convert text into speech.
import pandas as pd  # Importing pandas library
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import numpy as np  # Importing numpy to do stuffs related to arrays
import PySimpleGUI as sg  # Importing pysimplegui to make a Graphical User Interface.

excel = pd.read_excel('Crop.xlsx', header=0)  # Importing our excel data from a specific file.
print(excel)
print(excel.shape)  # Checking out the shape of our data.

engine = pyttsx3.init('sapi5')  # Defining the speech rate, type of voice etc.
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)
engine.setProperty('voice', voices[0].id)


def speak(audio):  # Defining a speak function. We can call this function when we want to make our program to speak something.
    engine.say(audio)
    engine.runAndWait()


le = preprocessing.LabelEncoder() #to represent categorical columns in a numerical column.
crop = le.fit_transform(list(excel["CROP"]))

NITROGEN = list(excel["NITROGEN"])  # Importing the values of given.
PHOSPHORUS = list(excel["PHOSPHORUS"])
POTASSIUM = list(excel["POTASSIUM"])
TEMPERATURE = list(excel["TEMPERATURE"])
HUMIDITY = list(excel["HUMIDITY"])
PH = list(excel["PH"])
RAINFALL = list(excel["RAINFALL"])

features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH,RAINFALL])  # Converting all the features into a array form

features = features.transpose()
print(features.shape)
print(crop.shape)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(features,crop)

layout = [[sg.Text('                                                                         ', font=("Times bold", 3),text_color='black', background_color='#34eb95')],
    [sg.Text('                    🌾 Crop Recommendation Assistant 🌾                      ', font=("Times bold", 30), text_color='black',background_color='#34eb95')],
          [sg.Text('                                                                         ', font=("Times bold", 20), text_color='black',background_color='#34eb95')],
          # Defining the layout of the Graphical User Interface. It consist of some text, Buttons, and blanks to take Input.
          [sg.Text('Please enter the following details :-', font=("Times", 20, 'bold', 'italic'),background_color='#34eb95',text_color='#de1414')],
          [sg.Text('                                                                         ', font=("Times bold", 5),text_color='black', background_color='#34eb95')],

          # We have defined the text size, font type, font size, blank size, colour of the text in the GUI.
          [sg.Text('Enter amount of " Nitrogen " in the soil                               :', font=("Times", 20),text_color='black',background_color='#34eb95'),
           sg.Input(font=("bold", 20), size=(20, 1))],
          [sg.Text('Enter amount of "Phosphorous" in the soil                          :', font=("Times", 20),text_color='black',background_color='#34eb95'),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('Enter amount of "Potassium" in the soil                               :', font=("Times", 20),text_color='black',background_color='#34eb95'),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('Enter average "Temperature" value around the field             :', font=("Times", 20),text_color='black',background_color='#34eb95'),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('*C', font=("Times", 20),text_color='black',background_color='#34eb95')],
          [sg.Text('Enter average percentage of "Humidity" around the field      :', font=("Times", 20),text_color='black',background_color='#34eb95'),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('%', font=("Times", 20),text_color='black',background_color='#34eb95')],
          [sg.Text('Enter PH value of the soil                                                     :', font=("Times", 20),text_color='black',background_color='#34eb95'),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('Enter average amount of "Rainfall" around the field             :', font=("Times", 20),text_color='black',background_color='#34eb95'),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('mm', font=("Times", 20),text_color='black',background_color='#34eb95')],
          [sg.Text('                                                                         ', font=("Times bold", 5),text_color='black', background_color='#34eb95')],
          [sg.Text(size=(100, 1), font=("Helvetica", 15, 'italic' , 'bold'), text_color='#de1414', key='-OUTPUT1-',background_color='#d7dbdb')],
          [sg.Button('Submit', font=("Times", 20)), sg.Button('Quit', font=("Times", 20))]]
window = sg.Window('Crop Recommendation Assistant', layout,background_color='#34eb95')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    print(values[0])
    nitrogen_content = values[0]  # Taking input from the user about nitrogen content in the soil.
    phosphorus_content = values[1]
    potassium_content = values[2]
    temperature_content = values[3]
    humidity_content = values[4]
    ph_content = values[5]
    rainfall = values[6]
    predict1 = np.array([nitrogen_content, phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content,rainfall])
    print(predict1)
    predict1 = predict1.reshape(1,-1)  # Reshaping the input data so that it can be applied in the model for getting accurate results.
    print(predict1)
    predict1 = model.predict(predict1)  # Applying the user input data into the model.
    print(predict1)  # Finally printing out the results.
    crop_name = str()
    if predict1 == 0:
        crop_name = 'Apple(सेब)'
    elif predict1 == 1:
        crop_name = 'Banana(केला)'
    elif predict1 == 2:
        crop_name = 'Blackgram(काला चना)'
    elif predict1 == 3:
        crop_name = 'Chickpea(काबुली चना)'
    elif predict1 == 4:
        crop_name = 'Coconut(नारियल)'
    elif predict1 == 5:
        crop_name = 'Coffee(कॉफ़ी)'
    elif predict1 == 6:
        crop_name = 'Cotton(कपास)'
    elif predict1 == 7:
        crop_name = 'Grapes(अंगूर)'
    elif predict1 == 8:
        crop_name = 'Jute(जूट)'
    elif predict1 == 9:
        crop_name = 'Kidneybeans(राज़में)'
    elif predict1 == 10:
        crop_name = 'Lentil(मसूर की दाल)'
    elif predict1 == 11:
        crop_name = 'Maize(मक्का)'
    elif predict1 == 12:
        crop_name = 'Mango(आम)'
    elif predict1 == 13:
        crop_name = 'Mothbeans(मोठबीन)'
    elif predict1 == 14:
        crop_name = 'Mungbeans(मूंग)'
    elif predict1 == 15:
        crop_name = 'Muskmelon(खरबूजा)'
    elif predict1 == 16:
        crop_name = 'Orange(संतरा)'
    elif predict1 == 17:
        crop_name = 'Papaya(पपीता)'
    elif predict1 == 18:
        crop_name = 'Pigeonpeas(कबूतर के मटर)'
    elif predict1 == 19:
        crop_name = 'Pomegranate(अनार)'
    elif predict1 == 20:
        crop_name = 'Rice(चावल)'
    elif predict1 == 21:
        crop_name = 'Watermelon(तरबूज)'

    if int(humidity_content) >= 1 and int(humidity_content) <= 33:  # Here I have divided the humidity values into three categories i.e low humid, medium humid, high humid.
        humidity_level = 'low humid'
    elif int(humidity_content) >= 34 and int(humidity_content) <= 66:
        humidity_level = 'medium humid'
    else:
        humidity_level = 'high humid'

    if int(temperature_content) >= 0 and int(temperature_content) <= 6:  # Here I have divided the temperature values into three categories i.e cool, warm, hot.
        temperature_level = 'cool'
    elif int(temperature_content) >= 7 and int(temperature_content) <= 25:
        temperature_level = 'warm'
    else:
        temperature_level = 'hot'

    if int(rainfall) >= 1 and int(rainfall) <= 100:  # Here I have divided the humidity values into three categories i.e less, moderate, heavy rain.
        rainfall_level = 'less'
    elif int(rainfall) >= 101 and int(rainfall) <= 200:
        rainfall_level = 'moderate'
    elif int(rainfall) >= 201:
        rainfall_level = 'heavy rain'
    if int(nitrogen_content) >= 1 and int(nitrogen_content) <= 50:
        nitrogen_level = 'less'
    elif int(nitrogen_content) >= 51 and int(nitrogen_content) <= 100:
        nitrogen_level = 'not to less but also not to high'
    elif int(nitrogen_content) >= 101:
        nitrogen_level = 'high'

    if int(phosphorus_content) >= 1 and int(phosphorus_content) <= 50:
        phosphorus_level = 'less'
    elif int(phosphorus_content) >= 51 and int(phosphorus_content) <= 100:
        phosphorus_level = 'not to less but also not to high'
    elif int(phosphorus_content) >= 101:
        phosphorus_level = 'high'

    if int(potassium_content) >= 1 and int(potassium_content) <= 50:
        potassium_level = 'less'
    elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
        potassium_level = 'not to less but also not to high'
    elif int(potassium_content) >= 101:
        potassium_level = 'high'

    if float(ph_content) >= 0 and float(ph_content) <= 5:
        phlevel = 'acidic'
    elif float(ph_content) >= 6 and float(ph_content) <= 8:
        phlevel = 'neutral'
    elif float(ph_content) >= 9 and float(ph_content) <= 14:
        phlevel = 'alkaline'

    print(crop_name)
    print(humidity_level)
    print(temperature_level)
    print(rainfall_level)
    print(nitrogen_level)
    print(phosphorus_level)
    print(potassium_level)
    print(phlevel)

    speak("Sir according to the data that you provided to me. The ratio of nitrogen in the soil is  " + nitrogen_level + ". The ratio of phosphorus in the soil is  " + phosphorus_level + ". The ratio of potassium in the soil is  " + potassium_level + ". The temperature level around the field is  " + temperature_level + ". The humidity level around the field is  " + humidity_level + ". The ph type of the soil is  " + phlevel + ". The amount of rainfall is  " + rainfall_level)
    window['-OUTPUT1-'].update('The+6 best crop that you can grow : ' + crop_name)
    speak("The best crop that you can grow is  " + crop_name)

window.close()
