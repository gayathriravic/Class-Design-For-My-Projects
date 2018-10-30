class Image:
    def __init__(self):
        self.image = "Image"
        self.isSkewed = False
        self.isBlur = False
        self.noisy = False
    def properties(self):
        print("Getting the properties of the image!")
        if self.skewed(self.image):
            self.isSkewed = True
        if self.blur(self.image):
            self.isBlur = True
        if self.noise(self.image):
            self.noisy = True
    def skewed(self,image):
        return True
    def blur(self,image):
        return True
    def noise(self,image):
        return False

class User:
    def __init__(self,number):
        self.number = number
        print("User created!")
    def capture_image(self):
        print("User is capturing an image!")
        self.image = Image()
        self.image.properties()

class OCR(User):
    def __init__(self):
        print("Instantiated the OCR model")
        self.workingModel = []

    def imageProcessing(self,image):
        if image.isBlur:
            # do some processing here
            print("blurry image")
        if image.isSkewed:
            # do processing for skewed images
            print("skewed image")
        if image.noisy:
            print("noisy image")
            # then do some processing here.
        print("done processing the image!")
        return image

    def tesseract(self,image):
        # convert the image to text
        print("Tesseract engine called.")
        text_file = "text file with image contents"
        return text_file

    def speech(self,text):
        # convert the text to speech.
        print("speech conversion")
        speech_output = "this is the speech output"
        return speech_output



if __name__ == '__main__':
    user = User(2)   # create the user.
    user.capture_image() # capture an image
    model = OCR() # instantiate the OCR
    image = model.imageProcessing(user.image) # processed image
    text_file_ocr = model.tesseract(image)  # processed image is fed into the OCR Engine.
    print(text_file_ocr)
    speech_output = model.speech(text_file_ocr)  # speech output
    print(speech_output)