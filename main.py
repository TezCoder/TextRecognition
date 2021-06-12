## importing Libraries
import cv2
import pytesseract

#Calling Pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

#Reading image
image = cv2.imread("sample.jpg")

#Now the thing is, Pytesseract can only read RGB values, where cv2 is in BGR. So, we have to convert it.
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

## just printing out the detected text
print(pytesseract.image_to_string(image))

## Now, if we want to see what the pytesseract detected, then there is a method called image to boxes
## which returns the dimension information of each and every character from the image. We are storing it in a a list.
imageBoxInfo = pytesseract.image_to_boxes(image)

## Storing shape of our image as height and width
hImage, wImage, _ = image.shape

for box in imageBoxInfo.splitlines():
    box = box.split(' ')
    ## so, box will be a list with first object as character and then box dimension information
    # --> ['D', '274', '899', '311', '946', '0']
    # --> [letter[0], x_start[1], x_end[2], y_start[3], y_end[4]]

    x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])

    ## now, next step is to put rectangle to detected characters.
    cv2.rectangle(image, (x, hImage-y), (w, hImage-h), (200,255,80), 2)
    cv2.putText(image, box[0], (x,hImage-y-85), cv2.FONT_HERSHEY_PLAIN, 2, (50,245,50), 1)


cv2.imshow('Result', image)
cv2.waitKey(0)






