import os

from flask import Flask, request, render_template, send_from_directory,flash
import pandas as pd
import csv
from tensorflow.keras.models import load_model
import numpy as np
import string






app=Flask(__name__)
app.secret_key='random string'

classes=['PREDICTED SIGN IS A','PREDICTED SIGN IS B','PREDICTED SIGN IS C',
         'PREDICTED SIGN IS D','PREDICTED SIGN IS E','PREDICTED SIGN IS F',
         'PREDICTED SIGN IS G','PREDICTED SIGN IS H','PREDICTED SIGN IS I',
         'PREDICTED SIGN IS J','PREDICTED SIGN IS K','PREDICTED SIGN IS L',
         'PREDICTED SIGN IS M','PREDICTED SIGN IS N','PREDICTED SIGN IS O',
         'PREDICTED SIGN IS P','PREDICTED SIGN IS Q','PREDICTED SIGN IS R',
         'PREDICTED SIGN IS S','PREDICTED SIGN IS T']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route('/upload1/<filename>')
def send_image(filename):
    print('kjsifhuissywudhj')
    return send_from_directory("images", filename)

@app.route("/upload1", methods=["POST","GET"])
def upload1():
    print('a')
    if request.method=='POST':
        myfile = request.files['file']
        print("sdgfsdgfdf")
        fn = myfile.filename
        mypath = os.path.join('images/', fn)
        myfile.save(mypath)

        print("{} is the file name", fn)
        print("Accept incoming file:", fn)
        print("Save it to:", mypath)
        # import tensorflow as tf
        import numpy as np
        from tensorflow.keras.preprocessing import image
        from tensorflow.keras.models import load_model
        # img = r"D:\Fathima\Python\medical image\database\train\Eye\006.jpg"
        new_model = load_model("visualizations/mobilenet.h5")
        test_image = image.load_img(mypath, target_size=(224 ,224))
        test_image = image.img_to_array(test_image)
        print(test_image)
        test_image=test_image/255
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)
        prediction = classes[np.argmax(result)]
    return render_template("template.html", image_name=fn,text=prediction)
    return render_template("contact.html")

if __name__=='__main__':
    app.run(debug=True)



