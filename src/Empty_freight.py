import flask_mail
import os
from flask import *
from werkzeug.utils import secure_filename

from src.dbcon import *

app=Flask(__name__)
app.secret_key = "1234567"

import functools

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

mail=flask_mail.Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'peslinto2Qgmail.com'
app.config['MAIL_PASSWORD'] = 'btiewjtyrgbzsku'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('loginindex.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/')
def log():
    return render_template('loginindex.html')




@app.route('/login',methods=['post','get'])
def login():
    username = request.form['textfield']
    password = request.form['textfield2']
    qry="select * from login where uname=%s and pwd=%s"
    val=(username,password)
    res=selectone(qry,val)

    if res is None:
        return'''<script>alert('Invalid..');window.location="/"</script>'''
    elif res['type']=='admin':
        if username == res['uname'] and password== res['pwd']:
          session['lid']=res['lid']
          return redirect('/admin_home')
        else:
            return '''<script>alert('Invalid..');window.location="/"</script>'''

    elif res['type'] == 'Trading_Company':
        if username == res['uname'] and password == res['pwd']:
                session['lid'] = res['lid']
                return redirect('/Trading_Company_home')
        else:
            return '''<script>alert('Invalid..');window.location="/"</script>'''

    else:
        return'''<script>alert('Invalid..');window.location="/"</script>'''






@app.route('/tcreg')
def tcreg():

    return render_template('REG.html')


@app.route('/register',methods=['get','post'])
def register():
    name=request.form['textfield']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    file=request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/photo', filename))
    username=request.form['textfield10']
    password=request.form['textfield11']
    qry="insert into login values(null,%s,%s,'pending')"
    val=(username,password)
    id=iud(qry,val)
    qry="insert into trading_company values(null,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),name,place,post,pin,phone,email,filename)
    iud(qry,val)
    return'''<script>alert("Registered.."); window.location='/'</script>'''
























#============================================ADMIN===============================
@app.route('/admin_home')
def admin_home():
    return render_template('Admin/admin_home.html')
@app.route('/VIEFEEDBACKADMIN')
@login_required
def VIEFEEDBACKADMIN():
    qry="SELECT * FROM  `feedback` JOIN `user`ON `user`.lid=`feedback`.uid where toid=%s"
    res=selectall2(qry,session['lid'])
    return render_template('Admin/view feedback.html',val=res)


@app.route('/approve_localOwner')
@login_required
def approve_localOwner():
    qry="SELECT * FROM  `local_owners` JOIN `login`ON `login`.lid=`local_owners`.lid where login.type='local_owners' or login.type='pending' or login.type='rejected'"
    res=selectall(qry)
    return render_template('Admin/approve_localOwner.html',val=res)





@app.route('/acceptlocal_owners')
@login_required
def acceptlocal_owners():
    id=request.args.get('id')
    qry = "update`login`set type='local_owners' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Accepted...");window.location='approve_localOwner#about'</script>'''


@app.route('/rejectlocal_owners')
@login_required
def rejectlocal_owners():
    id=request.args.get('id')
    qry = "update`login`set type='rejected' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Rejected...");window.location='approve_localOwner#about'</script>'''



@app.route('/approve_userr')
@login_required
def approve_userr():
    qry="SELECT * FROM  `user` JOIN `login`ON `login`.lid=`user`.lid where login.type='user' or login.type='pending' or login.type='rejected'"
    res=selectall(qry)
    return render_template('Admin/VIEWUSER.html',val=res)





@app.route('/acceptuser')
@login_required
def acceptuser():
    id=request.args.get('id')
    qry = "update`login`set type='user' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Accepted...");window.location='approve_userr#about'</script>'''


@app.route('/rejectuser')
@login_required
def rejectuser():
    id=request.args.get('id')
    qry = "update`login`set type='rejected' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Rejected...");window.location='approve_userr#about'</script>'''











@app.route('/approve_TC')
@login_required
def approve_TC():
    qry = "SELECT * FROM  `trading_company` JOIN `login`ON `login`.lid=`trading_company`.lid where login.type='Trading_Company' or login.type='pending' or login.type='rejected'"
    res = selectall(qry)
    return render_template('Admin/approve_TC.html',val=res)





@app.route('/accepttc')
@login_required
def accepttc():
    id=request.args.get('id')
    qry = "update`login`set type='Trading_Company' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Accepted...");window.location='approve_TC#about'</script>'''


@app.route('/rejecttc')
@login_required
def rejecttc():
    id=request.args.get('id')
    qry = "update`login`set type='rejected' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Rejected...");window.location='approve_TC#about'</script>'''













@app.route('/block_unblock_loadOwner')
@login_required
def block_unblock_loadOwner():
    qry = "SELECT * FROM  `local_owners` JOIN `login`ON `login`.lid=`local_owners`.lid where login.type ='local_owners' or login.type ='block'"
    res = selectall(qry)
    return render_template('Admin/block_unblock_loadOwner.html',val=res)



@app.route('/unblocklo')
@login_required
def unblocklo0():
    id=request.args.get('id')
    qry = "update`login`set type='local_owners' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Unblocked...");window.location='block_unblock_loadOwner#about'</script>'''


@app.route('/blocklo')
@login_required
def blocklo():
    id=request.args.get('id')
    qry = "update`login`set type='block' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Blocked...");window.location='block_unblock_loadOwner#about'</script>'''





@app.route('/block_unblock_TC')
@login_required
def block_unblock_TC():
    qry = "SELECT * FROM  `trading_company` JOIN `login`ON `login`.lid=`trading_company`.lid where login.type='Trading_Company' or  login.type='block'"
    res = selectall(qry)
    return render_template('Admin/block_unblock_TC.html',val=res)


@app.route('/unblocktc')
@login_required
def unblocktc():
    id=request.args.get('id')
    qry = "update`login`set type='Trading_Company' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Unblocked...");window.location='block_unblock_TC#about'</script>'''


@app.route('/blocktc')
@login_required
def blocktc():
    id=request.args.get('id')
    qry = "update`login`set type='block' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Blocked...");window.location='block_unblock_TC#about'</script>'''






@app.route('/view_complaint_reply')
@login_required
def view_complaint_reply():

    return render_template('Admin/view_complaint_reply.html')



@app.route('/view_complaint_reply1',methods=['post'])
@login_required
def view_complaint_reply1():
    TYPE=request.form["select"]
    if TYPE=="driver":
       qry="SELECT `driver`.`fname`AS `name`,complaint.* ,`user`.`fname`,`user`.`lname` FROM `driver` JOIN `complaint` ON `complaint`.`toid`=`driver`.`lid`JOIN `user`ON `user`.`lid`=`complaint`.`uid`"
       res=selectall(qry)
       return render_template('Admin/view_complaint_reply.html',val=res)

    elif TYPE=="Trading_Company":
       qry="SELECT * FROM `trading_company` JOIN `complaint` ON `complaint`.`toid`=`trading_company`.`lid`JOIN `user`ON `user`.`lid`=`complaint`.`uid`"
       res=selectall(qry)
       return render_template('Admin/view_complaint_reply.html',val=res)
    else:
       qry = "SELECT * FROM `local_owners` JOIN `complaint` ON `complaint`.`toid`=`local_owners`.`lid`JOIN `user`ON `user`.`lid`=`complaint`.`uid`"
       res = selectall(qry)
       return render_template('Admin/view_complaint_reply.html',val=res)





@app.route('/view_rating')
@login_required
def view_rating():
    qry="SELECT * FROM `rating` JOIN `user` ON `user`.lid=`rating`.uid"
    res=selectall(qry)
    return render_template('Admin/view_rating.html',val=res)






#===============================TRADING COMPANY=========================================================

@app.route('/Add_new')
@login_required
def Add_new():
    qry="SELECT * FROM driver  JOIN `login`ON `login`.`lid`=`driver`.`lid` WHERE `login`.`type`='driver'"
    res=selectall(qry)
    return render_template('Trading_Company/Add_new.html',val=res)






@app.route('/Assign')
@login_required
def Assign():
    id=request.args.get('id')
    session['lrid']=id

    qry="SELECT * FROM driver  JOIN `login`ON `login`.`lid`=`driver`.`lid` WHERE `login`.`type`='driver'"
    r=selectall(qry)
    return render_template('Trading_Company/Assign.html',v=r)



@app.route('/assigndr',methods=['post'])
@login_required
def assigndr():

    driver=request.form['select']
    qry="insert into assign values(null,%s,%s,curdate(),'pending')"
    val=(session['lrid'],driver)
    iud(qry,val)
    qry="update request_for_load set status='assigned' where id=%s"
    iud(qry,session['lrid'])
    return '''<script>alert("Assigned the driver.");window.location='view_request_assign_driver#about'</script>'''
















@app.route('/block_unblock_driver')
@login_required
def block_unblock_driver():
    qry = "SELECT * FROM  `driver` JOIN `login`ON `login`.lid=`driver`.lid"
    res = selectall(qry)
    return render_template('Trading_Company/block_unblock_driver.html',val=res)


@app.route('/unblockdriver')
@login_required
def unblockdriver():
    id=request.args.get('id')
    qry = "update`login`set type='driver' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Unblocked...");window.location='block_unblock_TC#about'</script>'''


@app.route('/blockdriver')
@login_required
def blockdriver():
    id=request.args.get('id')
    qry = "update`login`set type='block' where lid=%s"
    iud(qry,id)
    return '''<script>alert("Blocked...");window.location='block_unblock_TC#about'</script>'''







@app.route('/form')
@login_required
def form():
    return render_template('Trading_Company/form.html')
@app.route('/adddr',methods=['post'])
def adddr():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    vtype=request.form['textfield8']
    vnumber=request.form['textfield9']
    inumber=request.form['number']
    uname=request.form['textfield10']
    password=request.form['textfield11']
    qry="insert into login values(null,%s,%s,'driver')"
    val=(uname,password)
    id=iud(qry,val)
    qry="insert into driver values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),fname,lname,place,post,pin,phone,email,vtype,vnumber,inumber)
    iud(qry,val)
    return'''<script>alert("Added the new driver...."); window.location='/Add_new#about'</script>'''




@app.route('/editdr')
@login_required
def editdr():
    id=request.args.get('id')
    session['drid']=id
    qry="select * from driver where lid=%s"
    res=selectone(qry,id)
    return render_template('Trading_Company/edit dr.html',val=res)


@app.route('/editdr1',methods=['post'])
@login_required
def editdr1():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    vtype=request.form['textfield8']
    vnumber=request.form['textfield9']
    inumber=request.form['number']
    qry="UPDATE `driver` SET `fname`=%s,`lname`=%s,`place`=%s,`post`=%s,`pin`=%s,`phone`=%s,`email`=%s,`vtype`=%s,`vnumber`=%s,`i number`=%s WHERE `lid`=%s"
    val=(fname,lname,place,post,pin,phone,email,vtype,vnumber,inumber,session['drid'])
    iud(qry,val)
    return'''<script>alert("Edited.."); window.location='/Add_new#about'</script>'''



@app.route('/deletedr')
@login_required
def deletedr():
    id=request.args.get('id')
    qry="delete from driver where lid=%s"
    iud(qry,id)
    qry = "delete from login where lid=%s"
    iud(qry, id)
    return '''<script>alert("Deleted...."); window.location='/Add_new#about'</script>'''






@app.route('/reply_box')
@login_required
def reply_box():
    id=request.args.get('id')
    session['cmid']=id
    return render_template('Trading_Company/reply_box.html')

@app.route('/sendreply1',methods=['post'])
@login_required
def sendreply1():
    reply=request.form['textfield']
    qry="UPDATE `complaint` SET `reply`=%s WHERE `id`=%s"
    val=(reply,session['cmid'])
    iud(qry,val)
    return '''<script>alert("Sended...");window.location='view_complaint_send_reply#about'</script>'''

@app.route('/tcviewfeedback')
@login_required
def tcviewfeedback():
    qry = "SELECT * FROM `feedback` JOIN `user`ON `user`.`lid`=`feedback`.`uid` WHERE `feedback`.`toid`=%s"
    val = selectall2(qry,session['lid'])
    return render_template('Trading_Company/view tcfeedback.html',val=val)

@app.route('/viewrating')
@login_required
def viewrating():
    qry = "SELECT * FROM `rating` JOIN `user`ON `user`.`lid`=`rating`.`uid` WHERE `rating`.`toid`=%s"
    val = selectall2(qry,session['lid'])
    return render_template('Trading_Company/view RATING.html',val=val)


@app.route('/request_for_trip')
@login_required
def request_for_trip():
    return render_template('Trading_Company/request_for_trip.html')

# @app.route('/request_for_trip1',methods=['post'])
# def request_for_trip1():
#


@app.route('/Trading_Company_home')
@login_required
def Trading_Company_home():
    return render_template('Trading_Company/Trading_Company_home.html')


@app.route('/view_complaint_send_reply')
def view_complaint_send_reply():
    qry="SELECT `complaint`.*,`user`.`fname`,`lname` FROM `complaint`JOIN `user` ON `user`.lid=`complaint`.uid  WHERE `complaint`.`toid`=%s"
    res=selectall2(qry,session['lid'])
    return render_template('Trading_Company/view_complaint_send_reply.html',val=res)

@app.route('/view_request_assign_driver')
@login_required
def view_request_assign_driver():
    qry="SELECT * FROM `request_for_load` JOIN `user`ON `user`.lid=`request_for_load`.uid WHERE tid=%s"
    res=selectall2(qry,session['lid'])
    return render_template('Trading_Company/view_request_assign_driver.html',val=res)





@app.route('/rejectlocal_loadreq')
@login_required
def rejectlocal_loadreq():
    id=request.args.get('id')
    qry = "update`request_for_load`set status='rejected' where id=%s"
    iud(qry,id)
    return '''<script>alert("Rejected the load request.");window.location='view_request_assign_driver#about'</script>'''



@app.route('/forgotpassword',methods=['post','get'])
def forgotpassword():
    return render_template("forgetindex.html")



@app.route('/forgotpassword1',methods=['post','get'])
def forgotpassword1():
    email=request.form['textfield']
    qry ="SELECT `pwd` FROM `login` JOIN `trading_company` ON `login`.`lid`=`trading_company`.`lid` WHERE `trading_company`.`email`=%s"
    val=(email)
    res=selectone(qry,val)
    if res is not None:

            # date = qry[1]
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('peslinto2@gmail.com', 'btiewjtyrgubzsku')
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText("Your current password: " + res['pwd'])
            print(msg)
            msg['Subject'] = 'password'
            msg['To'] = email
            msg['From'] = 'peslinto2@gmail.com'
            try:
                gmail.send_message(msg)
            except Exception as e:
                print("COULDN'T SEND EMAIL", str(e))
                # con.commit()

            return  '''<script>alert("Sented to the email..");window.location='/'</script>'''
    else:
        return '''<script>alert(" Successfully Sented....");window.location='/'</script>'''













app.run(debug=True)