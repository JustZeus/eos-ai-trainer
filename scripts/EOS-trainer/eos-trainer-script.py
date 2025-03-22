"""File: eos-trainer-script.py
Author: Nancy Vazquez, Ricardo Zamudio
Date: 03/18/2025
Description: Demonstration script of the EOS trainer concept
"""
import azure.cognitiveservices.speech as speechsdk
import azure.cognitiveservices.vision.customvision.prediction as visionClient
import msrest.authentication as msRestAuth
import os, uuid
import customtkinter
from PIL import Image
from openai import AzureOpenAI
import cv2 as cv
from threading import Thread

# Set the GUI color theme
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green



SPEECH_KEY = os.environ[""]

SPEECH_REGION = os.environ[""]

ENDPOINT = os.environ[""]

training_key = os.environ[""]

prediction_key = os.environ[""]

prediction_resource_id = os.environ[""]

project_id = os.environ[""]

iteration_name = os.environ[""]

# Azure credentials
client = AzureOpenAI(
  azure_endpoint = "", 
  api_key="", 
  api_version=""
)

#Speach SDK Configuration
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)


# Open the demonstration training file
with open("training.txt", "r") as file:
    text = file.readlines()
    # print(text)
    indexIntro = text.index('Press the button to start.\n')
    indexSteps = text.index("Okay, now that you know the parts, let's start with the assembly. Press the button to begin the instructions.\n") 
    indexSteps = indexSteps + 1
    # print("index")
    # print(len(text))

def textToSpeech(text):
    # The neural multilingual voice can speak different languages based on the input text.
    speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))

def openAIFunction(question, responseBefore):
    nowQuestion = {"role": "user", "content": question}
    message = []
    if responseBefore == "":
        message = [nowQuestion]
    else:
        message = [responseBefore, nowQuestion]

    assistenMessage = {
        "role": "system",
        "content": "Your name is EOS you are an AI assistant that helps individuals to find information regarding the manufacturing industry"
    }

    message.append(assistenMessage)

    print(message)
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages= message,
        max_tokens=80
    )
    
    result = response.choices[0].message.content


    print(result)
    textToSpeech(result)
    if result[len(result) - 1] == "?":
        speech = recognize_from_microphone()
        openAIFunction(speech, {"role": "assistant", "content": result})


def recognize_from_microphone():
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        textToSpeech("I don't understand you, repeat the question please.")
        speech = recognize_from_microphone()
        openAIFunction(speech, "")
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return ""


## empty, half, dissasembly, complete
validationAnsware = "Correct."
errorAnsware = "Not correct, try again"
def start(imageLabel):
    global contador
    global step

    if(contador < len(text)):
        if contador <= indexIntro:
            speechText = ""
            for c, t in enumerate(text):
                if c < indexIntro:
                    speechText += t
            # print(speechText)
            textToSpeech(speechText)
        if  contador <= indexSteps and contador > indexIntro:
            # print(text[contador])
            textToSpeech(text[contador])
        if indexSteps <= contador:
            if contador == (indexSteps + 1):
                validation = validationService(imageLabel)
                # print(validation)
                if validation == "dissasembly":
                    # print(validationAnsware )
                    textToSpeech(validationAnsware)
                    # print(text[contador])
                    textToSpeech(text[contador])
                elif validation == "empty":
                    # print("The assembly does not appear in the work area, please place the part in the assigned area for validation.")
                    textToSpeech("The assembly does not appear in the work area, please place the part in the assigned area for validation. And try again")
                    contador = contador - 1
                    textToSpeech(text[contador])
                else:
                    # print(errorAnsware)
                    textToSpeech(errorAnsware)
                    contador = contador - 1
                    # print(text[contador])
                    textToSpeech(text[contador])
            elif contador == (indexSteps + 2):
                validation = validationService(imageLabel)
                print(validation)
                if validation == "half":
                    # print(validationAnsware)
                    textToSpeech(validationAnsware)
                    # print(text[contador])
                    textToSpeech(text[contador])  
                elif validation == "empty":
                    # print("The assembly does not appear in the work area, please place the part in the assigned area for validation.")
                    textToSpeech("The assembly does not appear in the work area, please place the part in the assigned area for validation. And try again")
                    contador = contador - 1
                    textToSpeech(text[contador])
                else:
                    # print(errorAnsware)
                    textToSpeech(errorAnsware)
                    contador = contador - 1
                    textToSpeech(text[contador])
                    # print(text[contador])
            elif  contador == (indexSteps + 3):
                validation = validationService(imageLabel)
                print(validation)
                if validation == "complete":
                    # print(validationAnsware )
                    textToSpeech(validationAnsware)
                    # print(text[contador] + "If you have any questions, you can ask me anything. Just press the button and ask your question.")
                    textToSpeech(text[contador] + "If you have any questions, you can ask me anything. Just press the button and ask your question.")
                elif validation == "empty":
                    # print("The assembly does not appear in the work area, please place the part in the assigned area for validation.")
                    textToSpeech("The assembly does not appear in the work area, please place the part in the assigned area for validation. And try again")
                    contador = contador - 1
                    textToSpeech(text[contador])
                else:
                    # print(errorAnsware)
                    textToSpeech(errorAnsware)
                    contador = contador - 1
                    textToSpeech(text[contador])
                    # print(text[contador])
    else:
        speech = recognize_from_microphone()
        if speech != "":
            openAIFunction(speech, "")
    contador += 1
    # print(contador)

# The predictionHandler is the function to query the Azure Custom Vision prediction endpoint, 
# this will validate the tag name with the highest score from the predictions received from the cloud.
def predictionHandler(id):
    prediction_credentials = msRestAuth.ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = visionClient.CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
    base_image_location = os.path.join (os.path.dirname(__file__), "")
    top_predictions = list()
    top_predictions.append({'tag_name': "empty", 'probability': .7})
    with open(os.path.join (base_image_location, id), "rb") as image_contents:
        results = predictor.detect_image(project_id , iteration_name, image_contents.read())
        if(results.predictions[0]):
            for prediction in results.predictions:
                if(prediction.probability > 0.75):
                    top_predictions.append({'tag_name': prediction.tag_name, 'probability': prediction.probability})
                # print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))
            # First Prediction formating 
            sorted_results = sorted(top_predictions, key=lambda x: x['probability'], reverse=True)
            prediction_statement = f'VALIDATION RESULTS \nPiece is: -->  { sorted_results[0]["tag_name"] } \nWith Score: { round((sorted_results[0]["probability"] * 100), 2) } %' 
            piece_status = sorted_results[0]["tag_name"]
            os.remove(id)
            return [prediction_statement, piece_status]
   
# ImageHandler is the function in charge of obtaining a camera capture, write it into memory and updating the display tag in the GUI.
def imageHandler(imageLabel, id):
    cam_port = 0
    cam = cv.VideoCapture(cam_port)
    result, image = cam.read()
    if result: 
        cv.imwrite(id, image)
        my_image = customtkinter.CTkImage(light_image=Image.open(id),
	    dark_image=Image.open(id),
	    size=(512,384)) # WidthxHeight
        imageLabel.configure(image=my_image, text = "")
        imageLabel.image= my_image
        cam.release()
    else: 
        print("No camera on current device")    
# ValidationService is the function to orchestrate the different pieces to obtain a image query to the Custom Vision.
# This function provides users with Speach feedback executed in a different thred to avoid blocking the GUI update.
# Returns the tag name of the identified object
def validationService(imageLabel):
    id = f'{uuid.uuid4()}.png'
    imageHandler(imageLabel, id)
    prediction = predictionHandler(id)
    higher_prediction = prediction[0]
    label = customtkinter.CTkLabel(master=window, text=higher_prediction)
    label.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)
    # create and configure a new thread to run a function
    # thread = Thread(target= lambda:textToSpeach(higher_prediction))
    # start the task in a new thread
    # thread.start()
    return  prediction[1]

# Initialize the Window
window = customtkinter.CTk()
window.geometry("600x600")
window.title("Trainer")

# Initialize the counter
contador = indexIntro

# Create label for the image placeholder
result_image_label = customtkinter.CTkLabel(window, text="")
result_image_label.pack(pady=10)
# Create the action button 
button = customtkinter.CTkButton(master=window, text="Action", command= lambda: start(result_image_label), font=("Arial", 170))
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# Execute the GUI
window.mainloop()
