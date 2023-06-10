from flask import Flask, request, redirect, url_for
from flask import render_template
import os
from imageai.Classification.Custom import CustomImageClassification


app = Flask(__name__)
UPLOAD_FOLDER = "./upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if "file1" not in request.files:
            return "There is no file1 in form!"
        file1 = request.files["file1"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
        file1.save(path)

        
        prediction = CustomImageClassification()
        prediction.setModelTypeAsDenseNet121()
        prediction.setModelPath("model.pt")
        prediction.setJsonPath("archive_model_classes.json")
        prediction.loadModel()

        predictions, probabilities = prediction.classifyImage((os.getcwd()+"/upload/"+str(file1.filename)), result_count=1)

        for i, j in zip(predictions, probabilities):
            x = i
            y = j   
            print(x,y)         
    else:
        i = 0
        j = 1
    return render_template('index.html',i=i,j=j)

app.run(debug=True)