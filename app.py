from flask import Flask, render_template, redirect, request
import mlab
from mongoengine import Document, StringField
mlab.connect()

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()

girl_type = GirlType(name= "Gái tiểu thư",image= "https://via.placeholder.com/400x200",
    description= "Thường đến các nơi sang chảnh, trà sữa 50K trở lên ở tại Royal City")
# girl_type.save()
app = Flask(__name__)
app.config["DEBUG"] = True #app.config là dictionary

gg = [
        {
            "name": "Gái tiểu thư",
            "image":"https://via.placeholder.com/400x200",
            "description":"Thường đến các nơi sang chảnh, trà sữa 50K trở lên ở tại Royal City"
        },
        {
            "name": "Gái ngoan",
            "image":"https://via.placeholder.com/400x200",
            "description":"Tính bình dân, trẻ như học sinh, già như công sở. Hay xuất hiện ở thư viện"
        },
        {
            "name": "Gái hâm",
            "image":"https://via.placeholder.com/400x200",
            "description":"Hâm dở, dẩm dít"
        }
    ]
@app.route('/') #Nếu người dùng vào trang chủ, hàm index sẽ được gọi
def index():
    return render_template("index.html",girl_types=GirlType.objects())
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/school")
def school():
    return redirect ("http://techkids.vn")
# @app.route("/bmi/<height>/<weight>")
@app.route("/bmi")
def bmi():
    print (request.args)
    args = request.args
    height = int(args["height"]) /100
    weight = int(args["weight"])
    bmi = weight/ (height ** 2)
    return "BMI của m là: "+str(bmi)
@app.route('/bmi_calc')
def bmi_calc():
    return render_template("bmi_calc.html")
if __name__ == '__main__':
  app.run(port=8000, debug=True)
# app.run(port=8000)
# app.run
#debug =true: để server tự reset lại khi thay đổi nội dung#
