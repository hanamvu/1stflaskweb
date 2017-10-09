from flask import Flask, render_template, redirect, request
import mlab
from mongoengine import Document, StringField
mlab.connect()

class Weapon(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    meta = {'collection': 'weaponz'}

# girl_type.save()
app = Flask(__name__)
app.config["DEBUG"] = True #app.config là dictionary

@app.route('/') #Nếu người dùng vào trang chủ, hàm index sẽ được gọi
def index():
    return render_template("index.html",weapons=Weapon.objects())
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/school")
def school():
    return redirect ("http://techkids.vn")
# @app.route("/bmi/<height>/<weight>")

if __name__ == '__main__':
  app.run(port=8000, debug=True)
# app.run(port=8000)
# app.run
#debug =true: để server tự reset lại khi thay đổi nội dung#
