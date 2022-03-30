import views
#import face_recognition
from flask import Flask, Response, send_file
from flask import render_template, request
from PIL import Image, ImageDraw
from flask import Flask, request
import os
import numpy as np
import cv2
from mtcnn.mtcnn import MTCNN
import time
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
#from face import facenett
from face import facevideo
from face import detect
import pandas as pd


app = Flask(__name__)


app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\2-2563\\project\\2\\projectII\\database.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


app.add_url_rule('/base', 'base', views.base)
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/faceapp', 'faceapp', views.faceapp)
# app.add_url_rule('/showlist', 'showlist', views.showlist)
app.add_url_rule('/faces', 'faces', views.faces, methods=['GET', 'POST'])


@app.route('/download_file')
def download_file():
    p = "book.xlsx"
    return send_file(p, as_attachment=True)


@app.route('/showlist')
def showlist():
    return render_template('showlist.html')


@app.route('/dataset')
def dataset():
    return render_template('dataset.html')
def dataset():
    cap = cv2.VideoCapture(0)
    detector = MTCNN()
    img_id = 0
    count = 0
    while(True):
        
        ret, frame = cap.read()
        if not ret:
            frame = cv2.VideoCapture(0)
            continue
        
        if ret:
            frame = np.asarray(frame)
            count = count + 1
            if count == 5 :
                print(count)
                try:
                    results = detector.detect_faces(frame)
                    count = 0
                    for i in range(len(results)):
                        x1, y1, width, height = results[i]['box']
                        x1, y1 = abs(x1), abs(y1)
                        x2, y2 = x1 + width, y1 + height
                        # frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                        pixels = np.asarray(frame)
                        face = pixels[y1:y2, x1:x2]
                        image = Image.fromarray(face)
                        image = image.resize((160,160))
                        face_array = np.asarray(image)
                        cv2.imwrite('./datas/train/Warinthon/img_{}.jpg'.format(img_id),frame)  
                        img_id +=1
               
                
                except:
                    print("Something else went wrong")
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        # time.sleep(0.1)
        
@app.route('/dataset_feed')
def dataset_feed():
    global video
    return Response(dataset(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


##########################################################

@app.route('/dataset1')
def dataset1():
    return render_template('dataset1.html')
def dataset1():
    cap = cv2.VideoCapture(0)
    detector = MTCNN()
    img_id = 0
    count = 0
    while(True):
        
        ret, frame = cap.read()
        if not ret:
            frame = cv2.VideoCapture(0)
            continue
        
        if ret:
            frame = np.asarray(frame)
            count = count + 1
            if count == 5 :
                print(count)
                try:
                    results = detector.detect_faces(frame)
                    count = 0
                    for i in range(len(results)):
                        x1, y1, width, height = results[i]['box']
                        x1, y1 = abs(x1), abs(y1)
                        x2, y2 = x1 + width, y1 + height
                        # frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                        pixels = np.asarray(frame)
                        face = pixels[y1:y2, x1:x2]
                        image = Image.fromarray(face)
                        image = image.resize((160,160))
                        face_array = np.asarray(image)
                        cv2.imwrite('./datas/train/Alameen/img_{}.jpg'.format(img_id),frame)  
                        img_id +=1
                        print("test")
               
                
                except:
                    print("Something else went wrong")
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        # time.sleep(0.1)
        
@app.route('/dataset_feed1')
def dataset_feed1():
    global video
    return Response(dataset1(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
##########################################################

##########################################################

@app.route('/dataset2')
def dataset2():
    return render_template('dataset2.html')
def dataset2():
    cap = cv2.VideoCapture(0)
    detector = MTCNN()
    img_id = 0
    count = 0
    while(True):
        
        ret, frame = cap.read()
        if not ret:
            frame = cv2.VideoCapture(0)
            continue
        
        if ret:
            frame = np.asarray(frame)
            count = count + 1
            if count == 5 :
                print(count)
                try:
                    results = detector.detect_faces(frame)
                    count = 0
                    for i in range(len(results)):
                        x1, y1, width, height = results[i]['box']
                        x1, y1 = abs(x1), abs(y1)
                        x2, y2 = x1 + width, y1 + height
                        # frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                        pixels = np.asarray(frame)
                        face = pixels[y1:y2, x1:x2]
                        image = Image.fromarray(face)
                        image = image.resize((160,160))
                        face_array = np.asarray(image)
                        cv2.imwrite('./datas/train/Alameen/img_{}.jpg'.format(img_id),frame)  
                        img_id +=1
                        print("test_dataset2")
               
                
                except:
                    print("Something else went wrong")
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        # time.sleep(0.1)
        
@app.route('/dataset_feed2')
def dataset_feed2():
    global video
    return Response(dataset2(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
##########################################################

@app.route('/detect')
def detect():
    return render_template('detect.html')
def detect():
    cap = cv2.VideoCapture(0)
    detector = MTCNN()
    count = 0
    img_id = 0
    while(True):
        ret, frame = cap.read()
        if not ret:
            frame = cv2.VideoCapture(0)
            continue
        
        if ret:
            frame = np.asarray(frame)
            count = count+1
            if count == 10 :

                try:
                    results = detector.detect_faces(frame)
                    print(len(results))
                    count = 0
                    img_id = 0
                    for i in range(len(results)):
                        x1, y1, width, height = results[i]['box']
                        x1, y1 = abs(x1), abs(y1)
                        x2, y2 = x1 + width, y1 + height
                        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                        pixels = np.asarray(frame)
                        face = pixels[y1:y2, x1:x2]
                        image = Image.fromarray(face)
                        image = image.resize((160,160))
                        face_array = np.asarray(image)
                       
                        cv2.imwrite('./data/img_{}.jpg'.format(i),face_array)
                    facevideo()
                   
                    folder_path = (r'D:\2-2563\project\2\projectII\data')
                    test = os.listdir(folder_path)
                    for images in test:
                        if images.endswith(".jpg"):
                            os.remove(os.path.join(folder_path, images))
                        
                                
                except:
                    print("Something else went wrong")
        

        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        time.sleep(0.1)
        
        
@app.route('/detect_feed')
def detect_feed():
    global video
    return Response(detect(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

############################### test ####

# def detect(): 
#     cap = cv2.VideoCapture(0)
#     database_image = face_recognition.load_image_file("image/Warinthon1.jpg")
#     data_base_encoding = face_recognition.face_encodings(database_image)[0]

#     person_face_encodings = [data_base_encoding]
#     person_face_names = ["Warinthon"]

#     data_locations = []
#     data_encodings = []
#     data_names = []
#     frameProcess = True

#     while True:
#         ret, frame = cap.read()
#         rgb_frame = frame[:, :, ::-1]
#         data_locations = face_recognition.face_locations(rgb_frame)
#         for top, right, bottom, left in data_locations:
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 4)
#             data_encodings = face_recognition.face_encodings(rgb_frame, data_locations)
#             data_names = []
#             for dc in data_encodings:
#                 matches = face_recognition.compare_faces(person_face_encodings, dc)
#                 name = "UNKNOWN"
#                 if True in matches:
#                     first_match_index = matches.index(True)
#                     name = person_face_names[first_match_index]

#                 data_names.append(name)
#                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (26, 174, 10), cv2.FILLED)
#                 font = cv2.FONT_HERSHEY_DUPLEX
#                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#         frame = cv2.resize(frame, (600, 340))
#         cv2.imshow('Video', frame)
#         facevideo()

#         if cv2.waitKey(25) == 13:
#             break

##################################
# from mtcnn import MTCNN
# import cv2
# detector = MTCNN()
# #Load a videopip TensorFlow
# video_capture = cv2.VideoCapture(0)
 
# while (True):
#     ret, frame = video_capture.read()
#     frame = cv2.resize(frame, (600, 400))
#     boxes = detector.detect_faces(frame)
#     if boxes:
 
#         box = boxes[0]['box']
#         conf = boxes[0]['confidence']
#         x, y, w, h = box[0], box[1], box[2], box[3]
 
#         if conf > 0.5:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
 
#     cv2.imshow("Frame", frame)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
 
# video_capture.release()
# cv2.destroyAllWindows()


#####################################





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(
        message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data, method='sha256')
        new_user = User(username=form.username.data,
                        email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return '<h1>New user has been created!</h1>'

    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
