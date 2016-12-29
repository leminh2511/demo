from flask import Flask
import json
from flask_restful import Resource,Api,reqparse
from mongoengine import *
import mongoengine

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("name",type=str, location="json")
parser.add_argument("birth",type=str, location="json")
parser.add_argument("desc",type=str, location="json")
parser.add_argument("img",type=str, location="json")

connect(
   'minhle',
   username = 'bibibobo2511',
   password = 'ckiuckiu2511',
   host = "ds133428.mlab.com",
   port = 33428
)

class Jav_idol(Document):
    name = StringField()
    birth = StringField()
    desc = StringField()
    img = StringField()

def jav_item(item):
    return json.loads(item.to_json())
def jav_list(list):
    return [jav_item(item) for item in list]

jav_local=[
    {
        "name":"Mao Kurata",
        "birth":"03/07/1994",
        "desc":"95-58-87",
        "img":"http://i.imgur.com/eALlVKP.jpg"
    },
    {
        "name":"Ren Azumi",
        "birth":"01/07/1991",
        "desc":"85-56-85",
        "img":"http://www.jjgirls.com/japanese/ren-azumi/85/ren-azumi-3.jpg"
    },
    {
        "name":"Miku Ohashi",
        "birth":"12/24/1987",
        "desc":"86-58-85",
        "img":"http://x365.us/images/anh-sex/040015112014/3_miku-ohashi-ngot-ngao-va-quyen-ru.jpg"
    },
    {
        "name":"Eririka Katagiri",
        "birth":"05/03/1991",
        "desc":"86-58-87",
        "img":"http://www.tokyokinky.com/blog/wp-content/uploads/2014/03/eririka-katagiri-porn-star-japanese.jpg"
    }
]

# for item in jav_local:
#     name = item["name"]
#     birth = item["birth"]
#     desc = item["desc"]
#     img = item["img"]
#
#     idol = Jav_idol(name=name, birth=birth, desc=desc, img=img)
#     idol.save()


# In ca list JAV
class Jav_list(Resource):
    def get(self):
        return jav_list(Jav_idol.objects)
    def post(self):
        args = parser.parse_args()
        name = args["name"]
        birth = args["birth"]
        desc = args["desc"]
        img = args["img"]
        print(name,birth,desc,img)

        idol= Jav_idol(name=name,birth=birth,desc=desc,img=img)
        idol.save()

        return json.loads(idol.to_json()), 200

#     ap dung voi tung item theo id : in, xoa, update
class Jav_item(Resource):
    def get(self, idol_id):
        return json.loads(Jav_idol.objects().with_id(idol_id).to_json())
    def delete(self, idol_id):
        idol = Jav_idol.objects().with_id(idol_id)
        idol.delete()
        return {"code": 1,"status":"ok"}
    def put(self, idol_id):
        idol = Jav_idol.objects().with_id(idol_id)
        args = parser.parse_args()
        name = args["name"]
        birth = args["birth"]
        desc = args["desc"]
        img = args["img"]
        idol.update(set__name=name, set__birth = birth, set__desc=desc, set__img=img)
        return json.loads(Jav_idol.objects().with_id(idol_id).to_json())


api.add_resource(Jav_list, "/api/javlist")
api.add_resource(Jav_item, "/api/idol/<idol_id>")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
