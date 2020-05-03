import cv2
import face_recognition
import pickle

encoding_file='encodings.pickle'

def detectAndDisplay(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="HOG")
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data['encodings'], encoding, tolerance = 0.4)
        name = 'unknown'

        if True in matches:
            matchedIndxs=[]
            for (i,b) in enumerate(matches):
                if(b == True):
                    matchedIndxs.append(i)
            print(matchedIndxs) 

            counts={}
            for items in matchedIndxs:
                name = data['names'][items]
                counts[name]= 0
            for items in matchedIndxs:
                counts[data['names'][items]] = counts.get(data['names'][items]) + 1
                print(data['names'][items])
            name = max(counts, key=counts.get)
            print(counts)
            print()
        names.append(name)

    for ((top, right, bottom, left), name) in zip(boxes, names):
        y = top-15
        color=(255,255,0)
        line = 1
        if(name == 'unknown'):
            color=(255,255,255)
            line = 1
            name = ''
        cv2.rectangle(frame, (left,top), (right,bottom), color,line)
        cv2.putText(frame, name, (left,y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, line)

    cv2.imshow('Recognition', frame)


data = pickle.loads(open(encoding_file, 'rb').read())


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('No more captured frames!')
        break
    flipped = cv2.flip(frame, 1)
    detectAndDisplay(flipped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
