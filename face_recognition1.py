import cv2
import face_recognition
import pickle
import time

image_file = '../gilmoregirls_1.jpg'
encoding_file = 'encodings.pickle'
unknown_name = 'Unknown'

def detectAndDisplay(image):
    start_time = time.time()
    # change bgr value to rgb
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # detect faces
    boxes = face_recognition.face_locations(rgb, model='hog')
    # encode faces
    encodings = face_recognition.face_encodings(rgb, boxes)

    names=[]
    
    for encoding in encodings:
        matches = face_recognition.compare_faces(data['encodings'], encoding)
        name = unknown_name # 모든 name 에 대해 unknown 인 상태에서 시작. 

        if True in matches: # True 값을 반환한 얼굴들의 인덱스를 찾음
            for (i,b) in enumerate (matches):
                if (b == True):
                    matchedIndxs = [i]
            #matchedIndxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIndxs:
                name = data['names'][i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)
            print(counts)
        names.append(name)
        
    for ((top, right, bottom, left), name) in zip(boxes, names):
        y = top - 15 if top -15 > 15 else top + 15
        color = (255,255,0)
        line = 1
        if(name == unknown_name):
            color = (255,255,255)
            line = 1
            name = ''
        cv2.rectangle(image, (left,top), (right,bottom), color, line)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(image, name, (left,y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.75, color, line)

    end_time = time.time()
    process_time = end_time - start_time
    print("{:.3f} seconds".format(process_time))

    cv2.imshow('Recognition', image)
    
    
data = pickle.loads(open(encoding_file, 'rb').read())

image = cv2.imread(image_file)
detectAndDisplay(image)

cv2.waitKey(0)
cv2.destroyAllWindows()
