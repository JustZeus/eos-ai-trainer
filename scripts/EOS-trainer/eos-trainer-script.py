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
import cv2 as cv
from threading import Thread

# Set the GUI color theme
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# Open the demonstration training file
with open("training.txt", "r") as file:
    text = file.readlines()
    # print(text)
    indexIntro = text.index('Press the button to start\n')

# retrieve environment variables    
SPEECH_KEY = os.environ[""]
SPEECH_REGION = os.environ[""]
ENDPOINT = os.environ[""]
training_key = os.environ[""]
prediction_key = os.environ[""]
prediction_resource_id = os.environ[""]
project_id = os.environ[""]
iteration_name = os.environ[""]
#Speach SDK Configuration
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

def textToSpeach(text):
    # The neural multilingual voice can speak different languages based on the input text.
    speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    # print("Enter some text that you want to speak >")
    # text = input()

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))

def start(imageLabel):
    global contador
    global step
    print(validationService(imageLabel))
    # if(contador < len(text)):
    #     if contador <= indexIntro:
    #         speechText = ""
    #         for c, t in enumerate(text):
    #             if c < indexIntro:
    #                 speechText += t
    #         print(speechText)
    #         SpeechToText(speechText)     
    #     SpeechToText(text[contador])
    #     print(text[contador])
    # else:
    #     SpeechToText("The training has ended very well.")
    #     print("The training has ended very well.")
    # contador += 1
    # step += 1

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
                print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))
            # First Prediction formating 
            sorted_results = sorted(top_predictions, key=lambda x: x['probability'], reverse=True)
            prediction_statement = f'VALIDATION RESULTS \nPiece is: -->  { sorted_results[0]["tag_name"] } \nWith Score: { round((sorted_results[0]["probability"] * 100), 2) } %' 
            piece_status = sorted_results[0]["tag_name"]
            os.remove(id)
            return [prediction_statement, piece_status]
        else:
            return "There were no elements identified"
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
    thread = Thread(target= lambda:textToSpeach(higher_prediction))
    # start the task in a new thread
    thread.start()
    return  prediction[1]

# Initialize the Window
window = customtkinter.CTk()
window.geometry("600x600")
window.title("Trainer")

# Initialize the counter
contador = indexIntro
step = 0

# Create label for the image placeholder
result_image_label = customtkinter.CTkLabel(window, text="")
result_image_label.pack(pady=10)
# Create the action button 
button = customtkinter.CTkButton(master=window, text="Action", command= lambda: start(result_image_label), font=("Arial", 170))
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# Execute the GUI
window.mainloop()