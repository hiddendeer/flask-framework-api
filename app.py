from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy, session
from utils.HttpResponse import HttpResponse
from sqlalchemy import and_
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager
from datetime import datetime


from flask_migrate import Migrate
from flask_redis import FlaskRedis

app = Flask(__name__)

# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask-admin'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

app.config['JWT_SECRET_KEY'] = 'ABCD'
# app.config['REDIS_URL'] = 'redis://:123456@localhost:6379/0'

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)
redis_client = FlaskRedis(app)

migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True, doc='用户ID')
    username = db.Column(db.String(50), doc='用户名')
    name = db.Column(db.String(50), doc='姓名')
    mobile = db.Column(db.String(50), doc='手机号', default="")

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}


class OrderInfo(db.Model):
    __tablename__ = 'order_info'
    id = db.Column('id', db.Integer, primary_key=True, doc='用户ID')
    name = db.Column(db.String(50), doc='订单名称')
    code = db.Column(db.String(50), doc='订单编码')
    user_id = db.Column(db.String(50), doc='关联用户id')

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}


class Dict(db.Model):
    __tablename__ = 'dvadmin_system_dict'
    id = db.Column('id', db.Integer, primary_key=True, doc='id')
    sort = db.Column(db.Integer, doc='id')
    name = db.Column(db.String(50), doc='字典名')
    code = db.Column(db.String(50), doc='字典code')
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)


class Area(db.Model):
    __tablename__ = 'area'
    id = db.Column(db.BigInteger, primary_key=True)
    description = db.Column(db.String(255, 'utf8mb4_general_ci'))
    modifier = db.Column(db.String(255, 'utf8mb4_general_ci'))
    dept_belong_id = db.Column(db.String(255, 'utf8mb4_general_ci'))
    update_datetime = db.Column(db.DateTime)
    create_datetime = db.Column(db.DateTime)
    name = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False)
    code = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, unique=True)
    level = db.Column(db.BigInteger, nullable=False)
    pinyin = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False)
    initials = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False)
    enable = db.Column(db.Integer, nullable=False)
    creator_id = db.Column(db.BigInteger, index=True)
    pcode_id = db.Column(db.String(20, 'utf8mb4_general_ci'), index=True)

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}


# class UsersFir(db.Model):
#     __tablename__ = 'sys_user_friend'
#     id = db.Column('id', db.String, primary_key=True, doc='用户ID')
#     userId = db.Column(db.String, doc='用户名')


class HelloWorld(Resource):

    # def get(self):
    #     req2 = request.args.get('name1')
    #     args = request.args
    #     print(args.to_dict())
    #     print(req2)
    #     rp = RequestParser()
    #     # rp.add_argument('name', required=True, help='name必填')
    #     # rp.add_argument('name1', required=True, help='name1必填', location=['args', 'headers'])
    #     req1 = rp.parse_args()
    #     print(req1)
    #     return {'hello': 'world1'}

    def post(self):
        # 1.创建RequestParser类对象
        rp = RequestParser()
        rp.add_argument('username', required=True, help='用户名必填')
        rp.add_argument('password', required=True, help='密码必填')
        userArgs = rp.parse_args()
        if userArgs['username'] == "" or userArgs['password'] == "":
            return {"code": 500, "msg": "用户名或密码必填"}

        user_info = db.session.query(User).filter(User.username == userArgs['username']).first()

        if user_info is None:
            return {"code": 500, "msg": "找不到用户"}

        # 生成token
        access_token = create_access_token(identity=user_info.id)

        # redis_client.set()

        json_info = {
            'access_token': access_token,
            'username': user_info.username,
            'mobile': user_info.mobile if user_info.mobile else ""
        }

        return json_info

    def delete(self):
        return {'hello': 'world3'}

    def put(self):
        return {'hello': 'world4'}


api.add_resource(HelloWorld, '/login')


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({
        'code': 401,
        'message': '登录令牌无效'
    }), 401


@app.route('/', methods=['GET', 'POST'])
@jwt_required()
def hello_world():  # put application's code here
    # token = redis_client.get('token')
    # if not token:
    #     return {"msg": "token过期"}
    #
    # access_token = token.decode()
    # print(access_token)
    req = request.get_json()
    # print(request.files.get('file'), 111)

    # user_id = get_jwt_identity()
    area_info = db.session.query(Area).all()
    json_data = []
    print(area_info)
    for item in area_info:
        json_data.append(item.to_dict())

    # return current_user
    # users = db.session.query(User.name, UsersFir.id).outerjoin(UsersFir, Users.id == UsersFir.userId).all()
    # print(users)
    # for item in users:
    #     print(item)
    #
    # try:
    #     token = jwt.encode({'some': 'payload'}, key="", algorithm='HS512')
    # finally:
    #     pass

    # tokenStr = "eyJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOjEzMzk1NTA0Njc5Mzk2MzkyOTksImFjY291bnQiOiJhZG1pbiIsInV1aWQiOiI1OTQ5YjBkMi1jZjFlLTQ5NzUtOWY2My1mYmNjM2EwNTYyYTQiLCJyZW1lbWJlck1lIjpmYWxzZSwiZXhwaXJhdGlvbkRhdGUiOjE3MDMxMTg3MzQ2NTUsImNhVG9rZW4iOm51bGwsIm90aGVycyI6bnVsbCwic3ViIjoiMTMzOTU1MDQ2NzkzOTYzOTI5OSIsImlhdCI6MTcwMjUxMzkzNCwiZXhwIjoxNzAzMTE4NzM0fQ.WdD7UnKHwfKBLJIWSoHNhoIWJr3hbX8B6BfdSemMnx3E7INN8XvopAn5JJBrfWkpTKXWaKJ1dxyYHJADMvf0HQ"
    # header, payload, signature = tokenStr.split('.')
    # decode_payload = base64.urlsafe_b64decode(payload + "==").decode('utf-8')
    # print(type(decode_payload))
    # print(type(json.loads(decode_payload)))
    # return decode_payload
    #
    # print(decpded_payload)

    # jwtObj = jwt.decode(tokenStr, "",
    #                     algorithms=['HS512'])
    #
    #
    # print(jwtObj, 111)

    # page = db.session.query(OrderInfo).filter(User.id == 2).join(User, User.id == OrderInfo.user_id).all()
    # print(page, 1111)

    # paginate = db.session.query(User).paginate(page=1, per_page=10)
    # userAll = db.session.query(User).filter(and_(User.name.like('%猫%'), User.id.in_([1, 2, 3]))).all()

    # 单条插入
    # useradd = User(id=3, name=req['name'])
    # db.session.add(useradd)
    # db.session.commit()

    # 多条插入
    # listModel = [
    #     User(id=4, name=req['name']),
    #     User(id=5, name=req['name']),
    #     User(id=6, name=req['name']),
    # ]
    # db.session.add_all(listModel)
    # db.session.commit()

    # 删除
    # delId = db.session.query(User).filter(User.id == 6).delete()
    # db.session.commit()
    # print(delId)

    # 更新
    # db.session.query(User).filter(User.id == 5).update({"name": "我不是陈大猫啊"})
    # db.session.commit()

    # print(userAll, '模糊查询')
    listInfo = [{"user_id": 1}]
    # for item in paginate.items:
    #     listInfo.append(item.to_dict())
    # print(listInfo)
    # listInfo = []
    # for item in user:
    #     jsonDict = {
    #         "id": item.id,
    #         "name": item.name,
    #     }
    #     listInfo.append(jsonDict)
    # handle(data={"a": 2})
    # print(listInfo)
    return jsonify({"data": json_data})


def handle(data=None) -> str:
    HttpResponse()
    return 111


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
    # app.run()
