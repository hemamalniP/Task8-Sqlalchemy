from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:user10@localhost:5432/empdb'
app.debug=True
db = SQLAlchemy(app)
class emp(db.Model):
    __tablename__='empdet'
    id = db.Column('emp_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    def __init__(self,id,name,city,addr,pin):
        self.id=id
        self.name=name
        self.city=city
        self.addr=addr
        self.pin=pin
@app.route('/etr',methods=['POST'])
def emrec():
    '''id=request.args.get('id')
    name=request.args.get('name')
    city=request.args.get('city')
    addr=request.args.get('addr')
    pin=request.args.get('pin')'''
    ipt=request.get_json()
    print(ipt)
    det=emp(id=ipt['id'],name=ipt['name'],city=ipt['city'],addr=ipt['addr'],pin=ipt['pin'])
    db.session.add(det)
    db.session.commit()
    return("successfully created")
@app.route('/fet',methods=['GET'])
def fetc():
    det=db.session.query(emp).all()
    res=[]
    for i in det:
        op=i.__dict__
        op.pop('_sa_instance_state')
        res.append(op)
    #print(res)
    return jsonify(res)
@app.route('/up',methods=['PUT'])
def upd():
    value=request.get_json()
    db.session.query(emp).filter(emp.id==value['val']).update({emp.city:value['val2']})
    db.session.commit()
    return ("succesfully updated")
@app.route('/del',methods=['DELETE'])
def dele():
    value=request.get_json()
    db.session.query(emp).filter(emp.id==value['val']).delete()
    db.session.commit()
    return ("Successfully Deleted")
if __name__ == '__main__':
    app.run(debug=True)
