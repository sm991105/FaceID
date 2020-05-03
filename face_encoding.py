import cv2
import face_recognition
import pickle
import time

dataset_paths = ['dataset/son/']
names = ['son']
number_images = 8

knownEncodings = []
knownNames =[]

start_time = time.time()
for(i, dataset_path) in enumerate(dataset_paths):
    name = names[i]
    
    for i in range(number_images):
        file_name = dataset_path + str(i)+ '.jpg'

        image = cv2.imread(file_name)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb, model='HOG')

        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            print(file_name, name, encoding)
            knownEncodings.append(encoding)
            knownNames.append(name)
            print(knownNames)
            
data = {"encodings" : knownEncodings,"names":knownNames}

end_time = time.time()
process_time = end_time - start_time
print("{:.3f} seconds".format(process_time))
f = open('encodings.pickle', 'wb')
f.write(pickle.dumps(data))


