import cv2

trained_car_data = cv2.CascadeClassifier("CarTracking/vehicle_haarcascades.xml")

stop_sign_data = cv2.CascadeClassifier("CarTracking/stop_sign_haarcascade.xml")

vid = cv2.VideoCapture("test\DMV+Driving+Test+Dash+Cam+-+STAY+CALM+-+Includes+Tips_Trim.mp4")

while True:
    sucessFrameRead, frame = vid.read()

    grayvid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Car
    carCoordinates = trained_car_data.detectMultiScale(grayvid)
    #print(carCoordinates)
    # Draw rectangle around car
    for (x, y, w, h) in carCoordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (111, 213, 255), 1)
        cv2.putText(frame, 'Car', (x, y-10), cv2.FONT_ITALIC, 0.75, (111, 213, 255), 2)

    # Stop sign
    stopSignCoordinates = stop_sign_data.detectMultiScale(grayvid)
    #print(stopSignCoordinates)
    # Draw rectangle around car
    for (x, y, w, h) in stopSignCoordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.putText(frame, 'Stop Sign', (x, y-10), cv2.FONT_ITALIC, 0.5, (0, 255, 0), 2)

    # show image (window name, and what you want to show)
    cv2.imshow('Face Detector app', frame)
    
    # wait and close by pressing any key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
vid.destroyAllWindows()
