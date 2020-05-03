1. dataset 디렉토리에 자신의 데이터셋을 만듭니다. 사진은 8장이어야하고, 형식은 jpg 여야합니다. (다르게 하려면 코드를 수정해야합니다.) 자신의 데이터셋을 만들면 son 폴더는 삭제해도 됩니다.

2. face_encoding.py 파일을 열어 dataset의 path 를 방금 만든 것으로 수정하세요. 백슬래시는 그대로 두고, son 부분만 자신의 데이터셋 파일명으로 바꾸면 됩니다. 파일을 실행하면 encoding.pickle 이라는 파일이 생성됩니다. 만약 여러번 실행할 경우 기존의 파일을 덮어쓰게 됩니다. 

3. encoding.py 파일이 생겼으면 face_recognition_webcam.py 파일을 실행합니다.

face_recognition_video 는 동영상에서의 얼굴인식을 위한 파일입니다.
face_recognition1, face_recognition2 는 사진에서의 얼굴인식을 위한 파일입니다. face_recognition1 은 코드에 에러를 포함하므로 실행하지 마세요.
