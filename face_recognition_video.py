import cv2
import face_recognition
import pickle

video_file='./sonny.gif';
encoding_file='encodings.pickle'

def detectAndDisplay(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="HOG")
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data['encodings'], encoding)
        name = 'unknown'

        if True in matches:
            matchedIndxs=[]
            for(i,b) in enumerate(matches):
                if(b == True):
                    matchedIndxs.append(i)
            counts={}
            for i in matchedIndxs:
                name = data['names'][i]
                counts[name] = 0
                counts[name] = counts.get(name) + 1
            name=max(counts, key=counts.get)
        names.append(name)

    for ((top, right, bottom, left), name) in zip(boxes, names):
        y = top-15
        color=(255,255,0)
        line = 1
        if(name == 'unknown'):
            color=(255,255,255)
            line = 1
            name = ''
        cv2.rectangle(image, (left,top), (right,bottom), color,line)
        cv2.putText(image, name, (left,y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, line)

    cv2.imshow('Recognition', image)


data = pickle.loads(open(encoding_file, 'rb').read())
image = cv2.imread(video_file)

'''
put all the video stuffs here, run detectAndDisplay function!

'''
cap = cv2.VideoCapture(video_file)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('No more captured frames!')
        break
    detectAndDisplay(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





