import cv2
import face_recognition
import pickle

image_file='../black.jpg'
encoding_file='encodings.pickle'

def detectAndDisplay(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="HOG")
    encodings = face_recognition.face_encodings(rgb, boxes)
    names=[]# for recognized faces

    for encoding in encodings: # 인풋 사진의 얼굴 하나에 대해
        matches = face_recognition.compare_faces(data['encodings'], encoding, tolerance=0.5)
        print(matches)
        print(encoding)
        name = 'unknown'
        
        if True in matches: # matches 에 true 가 있다면, true 의 인덱스를 뽑아
            matchedIndxs=[]
            for (i,b) in enumerate(matches):
                if(b == True):
                    matchedIndxs.append(i)
            print(matchedIndxs) # [0,1,2,3,4,5,6,7,14]

            counts={}
            for items in matchedIndxs:
                name = data['names'][items]
                counts[name]= 0
            # print(counts) # {'jihun':0, 'hyesoo':0}
            for items in matchedIndxs:
                counts[data['names'][items]] = counts.get(data['names'][items]) + 1
                print(data['names'][items])
            name = max(counts, key=counts.get)
            print(counts)
        names.append(name)

    for ((top, right, bottom, left), name) in zip(boxes, names):
        y = top - 15
        
        color = (255,255,0)
        line = 1
        if(name == 'unknown'):
            color = (255,255,255)
            line = 1
            name =''

        cv2.rectangle(image, (left,top),(right,bottom),color,line)
        cv2.putText(image, name, (left,y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, line)

    cv2.imshow('Recognition', image)
                

data = pickle.loads(open(encoding_file, 'rb').read())
image = cv2.imread(image_file)
detectAndDisplay(image)

cv2.waitKey(0)
cv2.destroyAllWindows()
