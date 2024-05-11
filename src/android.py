import flask_mail
import os
from flask import*
from werkzeug.utils import secure_filename
from src.dbcon import*


app=Flask(__name__)

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



@app.route('/vactime',methods=['get','post'])
def vactime():
    email=request.form['email']
    type=request.form['type']
    print(request.form)
    if type=='user':
            qry=selectone("SELECT * FROM `user` WHERE `email`=%s",email)
            print(qry)
    elif type=='local_owners':
        qry = selectone("SELECT * FROM `local_owners` WHERE `email`=%s", email)
        print(qry)
    else:
        qry = selectone("SELECT * FROM `driver` WHERE `email`=%s", email)
        print(qry)
    if qry is not None:
        print("hereeee")
        lid=qry['lid']
        qry1=selectone("select * from login where lid=%s",lid)
        print(qry1)
        pswd=qry1['pwd']

        print(qry)

    # date = qry[1]
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('peslinto2@gmail.com','btiewjtyrgubzsku')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Your current password: " + pswd)
        print(msg)
        msg['Subject'] = 'forgot password'
        msg['To'] = email
        msg['From'] = 'peslinto2@gmail.com'
        try:
            gmail.send_message(msg)
        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        # con.commit()

        return jsonify({"task": "sucess"})
    else:
        return jsonify({"task":"failed"})

@app.route('/login',methods=['post'])
def login():

    username=request.form['uname']
    password=request.form['pwrd']

    qry="select * from `login` where uname =%s and `pwd`=%s "
    val=(username,password)
    s=selectone(qry,val)

    if s is None:
        return jsonify({'task':'invalid'})
    else:
        type=s['type']
        id=s['lid']
        return jsonify({'task':'valid',"lid" : id ,"type":type})




@app.route('/register', methods=['post'])
def register():
    try:
        fname = request.form['Fname']
        lname = request.form['Lname']
        phone = request.form['phno']
        email = request.form['email']
        place=request.form['plc']
        post=request.form['post']
        pin=request.form['pin']
        uname=request.form['uname']
        Pwrd=request.form['pword']
        qry = "INSERT INTO `login` VALUES(NULL,%s,%s,'user')"
        val = (uname,Pwrd)
        s = iud(qry, val)
        qry="INSERT INTO `user` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(str(s),fname,lname,place,post,pin,phone,email)
        iud(qry,val)
        return jsonify({'task': 'success'})
    except:
        return jsonify({'task': 'already exist'})




@app.route('/registerlo', methods=['post'])
def reglo():

        fname = request.form['Fname']

        phone = request.form['phno']
        email = request.form['email']
        place=request.form['plc']
        post=request.form['post']
        pin=request.form['pin']
        file=request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/photo', filename))
        uname=request.form['uname']
        Pwrd=request.form['pword']
        qry = "INSERT INTO `login` VALUES(NULL,%s,%s,'pending')"
        val = (uname,Pwrd)
        s = iud(qry, val)
        qry="INSERT INTO `local_owners` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(str(s),fname,place,post,pin,email,phone,filename)
        iud(qry,val)
        return jsonify({'task': 'success'})















@app.route('/send_rating', methods=['post'])
def send_rating():

    lid = request.form['lid']
    tid = request.form['toid']
    review = request.form['review']
    rating = request.form['rating']
    qry = "insert into rating values(null,%s,%s,%s,%s,curdate())"
    val = (lid,tid,rating,review)
    iud(qry, val)
    return jsonify({'task': 'valid'})




@app.route('/send_feedback',methods=['post'])
def send_feedback():
    type=request.form['type']
    if (type == "Admin"):
        tid="1"
    else:
        tid = request.form['toid']

    lid=request.form['lid']

    feed=request.form['feed']
    qry="insert into feedback values(null,%s,%s,%s,curdate())"
    val=(lid,tid,feed)
    iud(qry,val)




    return jsonify({'task': 'valid'})




@app.route('/view_reply',methods=['post'])
def view_reply():
    lid=request.form['lid']
    type=request.form['type']
    if type=='driver':
        qry="SELECT `complaint`.*,`login`.*,`driver`.`fname`AS `name` FROM `complaint` JOIN `driver` ON `driver`.`lid`=`complaint`.`toid` JOIN `login` ON `login`.`lid`=`driver`.`lid` WHERE `login`.`type`='driver' AND `complaint`.uid=%s"
        res=selectall2(qry,lid)
        print(res)
        return jsonify(res)

    elif type == 'Trading_Company':
        qry = " SELECT * FROM `complaint` JOIN `trading_company` ON `trading_company`.`lid`=`complaint`.`toid` JOIN `login` ON `login`.`lid`=`trading_company`.`lid` WHERE `login`.`type`='Trading_Company' AND `complaint`.uid=%s"
        res = selectall2(qry, lid)
        print(res)
        return jsonify(res)
    else:
        qry = " SELECT * FROM `complaint` JOIN `local_owners` ON `local_owners`.`lid`=`complaint`.`toid` JOIN `login` ON `login`.`lid`=`local_owners`.`lid` WHERE `login`.`type`='local_owners' AND `complaint`.uid=%s"
        res = selectall2(qry, lid)
        print(res)
        return jsonify(res)


@app.route('/view_tc',methods=['post'])
def view_tc():

    qry="SELECT * FROM `trading_company`"
    res=selectall(qry)
    print(res)
    return jsonify(res)


@app.route('/view_complaintandsendreply',methods=['post'])
def view_complaintandsendreply():
    lid=request.form['lid']
    qry="SELECT * FROM `complaint` JOIN `user`ON `user`.`lid`=`complaint`.`uid` WHERE `complaint`.reply='pending' and `complaint`.`toid`=%s"
    res=selectall2(qry,lid)
    print(res)
    return jsonify(res)


@app.route('/send_complaint',methods=['post'])
def send_complaint():
    lid=request.form['lid']
    tid=request.form['exid']
    com=request.form['complaint']
    qry="insert into complaint values(null,%s,%s,%s,curdate(),'pending')"
    val=(lid,tid,com)
    iud(qry,val)
    return jsonify({'task': 'valid'})






@app.route('/viewdr',methods=['post'])
def viewdr():
    fname=request.form['uname']
    qry="SELECT * FROM `driver`JOIN `login`ON `login`.`lid`=`driver`.`lid` WHERE `login`.`type`='driver' and driver.fname LIKE '%"+fname+"%'"
    res = selectall(qry)
    return jsonify(res)

@app.route('/viewdrrrr',methods=['post'])
def viewdrrr():

    qry="SELECT * FROM `driver`JOIN `login`ON `login`.`lid`=`driver`.`lid` WHERE `login`.`type`='driver' "
    res = selectall(qry)
    return jsonify(res)
@app.route('/viewrating',methods=['post'])
def viewrating():
    lid=request.form['lid']
    qry="SELECT * FROM `rating`JOIN `user`ON `user`.lid=`rating`.`uid` WHERE toid=%s"
    res = selectall2(qry,lid)
    print(res)
    return jsonify(res)

@app.route('/in_message2',methods=['post'])
def in_message():
    print(request.form)
    fromid = request.form['fid']
    print("fromid",fromid)

    toid = request.form['toid']
    print("toid",toid)

    message=request.form['msg']
    print("msg",message)
    qry = "INSERT INTO `chat` VALUES(NULL,%s,%s,%s,CURDATE())"
    value = (fromid, toid, message)
    print("pppppppppppppppppp")
    print(value)
    iud(qry, value)
    return jsonify(status='send')

@app.route('/view_message2',methods=['post'])
def view_message2():
    print("wwwwwwwwwwwwwwww")
    print(request.form)
    fromid=request.form['fid']
    print(fromid)
    toid=request.form['toid']
    print(toid)
    lmid = request.form['lastmsgid']
    print("msgggggggggggggggggggggg"+lmid)
    sen_res = []
    # qry="SELECT * FROM chat WHERE (fromid=%s AND toid=%s) OR (fromid=%s AND toid=%s) ORDER BY DATE ASC"
    qry="SELECT `fromid`,`message`,`date`,`id` FROM `chat` WHERE `id`>%s AND ((`toid`=%s AND  `fromid`=%s) OR (`toid`=%s AND `fromid`=%s)  )  ORDER BY id ASC"
    print("SELECT `fromid`,`message`,`date`,`id` FROM `chat` WHERE `id`>%s AND ((`toid`=%s AND  `fromid`=%s) OR (`toid`=%s AND `fromid`=%s)  )  ORDER BY id ASC")
    val=(str(lmid),str(toid),str(fromid),str(fromid),str(toid))
    print("fffffffffffff",val)
    res = selectall2(qry,val)
    print("resullllllllllll")
    print(res)
    if res is not None:
        return jsonify(status='ok', res1=res)
    else:
        return jsonify(status='not found')



"========================================================================================================="

@app.route('/viewlocalo',methods=['post'])
def viewlocalo():
    name=request.form['uname']
    qry="SELECT * FROM `local_owners` JOIN `login` ON `login`.`lid`=`local_owners`.`lid` WHERE `login`.`type`='local_owners' and local_owners.name LIKE '%"+name+"%'"
    res = selectall(qry)
    return jsonify(res)

@app.route('/viewlocalowner',methods=['post'])
def viewlocalowner():
    qry="SELECT * FROM `local_owners` JOIN `login` ON `login`.`lid`=`local_owners`.`lid` WHERE `login`.`type`='local_owners' "
    res = selectall(qry)
    return jsonify(res)
@app.route('/viewuser',methods=['post'])
def viewuser():
    fname=request.form['uname']
    qry="SELECT * FROM `user`JOIN `login`ON `login`.`lid`=`user`.`lid` WHERE `login`.`type`='user' and user.fname LIKE '%"+fname+"%'"
    res = selectall(qry)
    return jsonify(res)
#
# @app.route('/in_message2',methods=['post'])
# def in_message():
#     print(request.form)
#     fromid = request.form['fid']
#     print("fromid",fromid)
#
#     toid = request.form['toid']
#     print("toid",toid)
#
#     message=request.form['msg']
#     print("msg",message)
#     qry = "INSERT INTO `chat` VALUES(NULL,%s,%s,%s,CURDATE())"
#     value = (fromid, toid, message)
#     print("pppppppppppppppppp")
#     print(value)
#     iud(qry, value)
#     return jsonify(status='send')
#
# @app.route('/view_message',methods=['post'])
# def view_message2():
#     print("wwwwwwwwwwwwwwww")
#     print(request.form)
#     fromid=request.form['fid']
#     print(fromid)
#     toid=request.form['toid']
#     print(toid)
#     lmid = request.form['lastmsgid']
#     print("msgggggggggggggggggggggg"+lmid)
#     sen_res = []
#     # qry="SELECT * FROM chat WHERE (fromid=%s AND toid=%s) OR (fromid=%s AND toid=%s) ORDER BY DATE ASC"
#     qry="SELECT `fromid`,`message`,`date`,`id` FROM `chat` WHERE `id`>%s AND ((`toid`=%s AND  `fromid`=%s) OR (`toid`=%s AND `fromid`=%s)  )  ORDER BY id ASC"
#     print("SELECT `fromid`,`message`,`date`,`id` FROM `chat` WHERE `id`>%s AND ((`toid`=%s AND  `fromid`=%s) OR (`toid`=%s AND `fromid`=%s)  )  ORDER BY id ASC")
#     val=(str(lmid),str(toid),str(fromid),str(fromid),str(toid))
#     print("fffffffffffff",val)
#     res = selectall2(qry,val)
#     print("resullllllllllll")
#     print(res)
#     if res is not None:
#         return jsonify(status='ok', res1=res)
#     else:
#         return jsonify(status='not found')
#
#
#
#
#
#






@app.route('/LOCATION',methods=['post'])
def LOCATION():
    lid=request.form['lid']
    tid=request.form['latitude']
    com=request.form['longitude']

    qry = "SELECT * FROM `location` WHERE `did`=%s"
    res = selectone(qry,lid)

    if res is None:

        qry="INSERT INTO  `location` VALUES(NULL,%s,%s,%s)"
        val=(lid,tid,com)
        iud(qry,val)
        return jsonify({'task': 'success'})
    else:
        qry = "UPDATE `location`SET `latitude`=%s,`longitude`=%s WHERE `id`=%s"
        val = (tid, com, lid)
        iud(qry, val)
        return jsonify({'task': 'success'})


# @app.route('/updateLOCATION',methods=['post'])
# def updateLOCATION():
#     lid=request.form['lid']
#     tid=request.form['latitude']
#     com=request.form['longitude']
#     qry="UPDATE `location`SET `latitude`=%s,`longitude`=%s WHERE `id`=%s"
#     val=(tid,com,lid)
#     iud(qry,val)
#     return jsonify({'task': 'success'})


@app.route('/requesttoload',methods=['post'])
def requesttoload():
    lid=request.form['lid']
    tid=request.form['tid']
    load=request.form['load']
    com=request.form['details']
    qry="INSERT INTO `request_for_load` VALUES(NULL,%s,%s,%s,%s,CURDATE(),'pending')"
    val=(lid,tid,load,com)
    iud(qry,val)
    return jsonify({'task': 'success'})




@app.route('/trackdr',methods=['post'])
def trackdr():
    fname=request.form['uname']
    # qry="SELECT * FROM `driver`JOIN `location` ON `location`.`did`=`driver`.lid  JOIN `login`ON `login`.`lid`=`driver`.`lid` WHERE `login`.`type`='driver' and driver.fname LIKE '%"+fname+"%'"
    qry="SELECT * FROM `driver`JOIN `location` ON `location`.`did`=`driver`.lid  JOIN `login`ON `login`.`lid`=`driver`.`lid` WHERE `driver`.fname LIKE '%"+fname+"%' AND `login`.`type`='driver' "
    res = selectall(qry)
    return jsonify(res)




@app.route('/requesttotrip',methods=['post'])
def requesttotrip():
    lid=request.form['lid']
    tid=request.form['uid']
    load=request.form['from']
    com=request.form['to']
    qry="INSERT INTO `request_for_trip` VALUES(NULL,%s,%s,%s,%s,CURDATE(),'pending')"
    val=(lid,tid,load,com)
    iud(qry,val)
    return jsonify({'task': 'success'})




@app.route('/viewrequesttrip',methods=['post'])
def viewrequest():
    lid=request.form['lid']
    qry = "SELECT `request_for_trip`.*,`user`.`fname`,`lname` FROM `request_for_trip` JOIN `user`ON `user`.lid=`request_for_trip`.uid WHERE request_for_trip.lid=%s"
    res = selectall2(qry,lid)
    return jsonify(res)



@app.route('/accrptreq',methods=['post'])
def accrptreq():
    lid = request.form['rid']
    qry = "update`request_for_trip`set status='accepted' where id=%s"
    iud(qry,lid)
    return jsonify({'task': 'success'})



@app.route('/rejrctreq',methods=['post'])
def rejrctreq():
    lid = request.form['rid']
    qry = "update`request_for_trip`set status='rejected' where id=%s"
    iud(qry,lid)
    return jsonify({'task': 'success'})



@app.route('/retunreq',methods=['post'])
def retunreq():
    lid = request.form['rid']
    qry = "update`request_for_trip`set status='return' where id=%s"
    iud(qry,lid)
    return jsonify({'task': 'success'})



@app.route('/viewrequesttripreturndr',methods=['post'])
def viewrequesttripreturndr():

    qry = "SELECT `request_for_trip`.*,`local_owners`.`name` FROM `request_for_trip` JOIN `local_owners`ON `local_owners`.`lid`=`request_for_trip`.`lid` WHERE `request_for_trip`.`status`='return' UNION SELECT `request_for_trip`.*,`driver`.`fname`AS `name` FROM `request_for_trip` JOIN `driver`ON `driver`.`lid`=`request_for_trip`.`lid` WHERE `request_for_trip`.`status`='return'"
    res = selectall(qry)
    return jsonify(res)

@app.route('/viewrteequ',methods=['post'])
def viewrteequ():
    lid = request.form['lid']
    type = request.form['type']
    if type == 'driver':
        qry = "SELECT `request_for_trip`.*,`driver`.`fname`AS `name` FROM `request_for_trip` JOIN `driver` ON `request_for_trip`.`lid`=`driver`.lid WHERE `request_for_trip`.`status`='return' AND `request_for_trip`.`uid`=%s"
        res = selectall2(qry, lid)
        return jsonify(res)
    else:
        qry = "SELECT * FROM `request_for_trip` JOIN `local_owners` ON `request_for_trip`.`lid`=`local_owners`.lid WHERE `request_for_trip`.`status`='return' AND `request_for_trip`.`uid`=%s"
        res = selectall2(qry, lid)
        return jsonify(res)



@app.route('/viewrequesttripreturndrUSER',methods=['post'])
def viewrequesttripreturndrUSER():
    lid = request.form['lid']
    type=request.form['type']
    if type=='driver':
        qry="SELECT `booking`.* ,`request_for_trip`.`from`,`request_for_trip`.`to`,`driver`.`fname`AS`name`FROM `request_for_trip` JOIN `driver`ON `driver`.`lid`=`request_for_trip`.`lid` JOIN `booking`ON `booking`.rt_id=`request_for_trip`.id WHERE `booking`.`uid`=%s"
        res = selectall2(qry,lid)
        return jsonify(res)
    else:
        qry="SELECT `booking`.* ,`request_for_trip`.`from`,`request_for_trip`.`to`,`local_owners`.`name`FROM `request_for_trip` JOIN `local_owners`ON `local_owners`.`lid`=`request_for_trip`.`lid` JOIN `booking`ON `booking`.rt_id=`request_for_trip`.id  WHERE `booking`.`uid`=%s"
        res = selectall2(qry,lid)
        return jsonify(res)

    # qry = "SELECT `request_for_trip`.from,`to`,`local_owners`.`name` ,`booking`.`date`,`booking`.`status`FROM `request_for_trip` JOIN `local_owners`ON `local_owners`.`lid`=`request_for_trip`.`lid` JOIN `booking`ON `booking`.rt_id=`request_for_trip`.id WHERE `booking`.`uid`=%s UNION SELECT `request_for_trip`.from,`to`,`driver`.`fname`AS `name` ,`booking`.`date`,`booking`.`status`FROM `request_for_trip` JOIN `driver`ON `driver`.`lid`=`request_for_trip`.`lid` JOIN `booking`ON `booking`.`rt_id`=`request_for_trip`.id WHERE `booking`.`uid`=%s"
    # res = selectall2(qry,(lid,lid))
    # return jsonify(res)




@app.route('/requestfoeRT',methods=['post'])
def requestfoeRT():
    id=request.form['lid']
    lid = request.form['lid']
    rid = request.form['rid']
    qry="select * from booking where uid=%s and rt_id=%s"
    res=selectone(qry,(lid,rid))
    if res is None:
            qry = "INSERT INTO `booking` VALUES(NULL,%s,%s,CURDATE(),'pending')"
            iud(qry,(rid,lid))
            return jsonify({'task': 'success'})
    else:
        qry = "update `booking` set RT_id=%s ,uid=%s where id=%s "
        iud(qry, (rid, lid,id))
        return jsonify({'task': 'success'})



@app.route('/viewbookingRtreq',methods=['post'])
def viewbookingRtreq():
    lid = request.form['lid']
    qry = "SELECT `booking`.*,`user`.`fname`,`lname`,`request_for_trip`.`from`,`to` FROM  `booking`JOIN `user`ON `user`.lid=`booking`.uid JOIN `request_for_trip`ON `request_for_trip`.id=`booking`.rt_id WHERE `request_for_trip`.`lid`=%s"
    res = selectall2(qry,lid)
    return jsonify(res)



@app.route('/accrptRTreq',methods=['post'])
def accrptRTreq():
    lid = request.form['rid']
    qry = "update`booking`set status='accepted' where id=%s"
    iud(qry,lid)
    return jsonify({'task': 'success'})


@app.route('/rejrctRTreq',methods=['post'])
def rejrctRTreq():
    lid = request.form['rid']
    qry = "update`booking`set status='rejected' where id=%s"
    iud(qry,lid)
    return jsonify({'task': 'success'})



@app.route('/viewassignwork',methods=['post'])
def viewassignwork():
    lid = request.form['lid']
    qry = "SELECT `assign`.id,assign.`date`,`assign`.`status`,`request_for_load`.`load`,`request_for_load`.`details`,`trading_company`.`name` FROM `assign` JOIN `request_for_load`ON `request_for_load`.`id`=`assign`.rid JOIN `trading_company`ON `trading_company`.lid=`request_for_load`.`tid`  WHERE `assign`.`Did`=%s"
    res = selectall2(qry,lid)
    return jsonify(res)



@app.route('/acceptetassign',methods=['post'])
def acceptetassign():
    lid = request.form['rid']
    qry = "update`assign`set status='accepted' where id=%s"
    iud(qry,lid)
    return jsonify({'task': 'success'})



@app.route('/rejectassign',methods=['post'])
def rejectassign():
    lid = request.form['rid']
    qry = "update`assign`set status='rejected' where id=%s"
    iud(qry,lid)
    return jsonify({'task': 'success'})



@app.route('/sendfeedtoooooooo',methods=['post'])
def sendfeedtoooooooo():
    type = request.form['type']
    if type=='driver':
        q="SELECT `driver`.`fname`AS `name`,`login`.* FROM `driver` JOIN `login` WHERE `login`.`type`='driver'"
        res=selectall(q)
        return jsonify(res)
    elif type=='local_owners':
        qry="SELECT * FROM `local_owners` JOIN `login`ON `local_owners`.lid=`login`.lid  WHERE `login`.`type`='local_owners'"
        res=selectall(qry)
        return jsonify(res)
    else:
        qry = "SELECT * FROM `trading_company` JOIN `login`ON `trading_company`.`lid`=`login`.`lid` WHERE `login`.`type`='Trading_Company'"
        res = selectall(qry)
        return jsonify(res)
    return jsonify({'task': 'success'})




@app.route('/viewfeedback',methods=['post'])
def viewfeedback():
    lid = request.form['lid']
    print(request.form)
    qry=" SELECT * FROM `feedback` JOIN `user`ON `user`.lid=`feedback`.`uid` WHERE `toid`=%s"
    res = selectall2(qry,lid)
    return jsonify(res)


@app.route('/sendreply1',methods=['post'])

def sendreply1():
    print(request.form)
    reply=request.form['reply']
    cid=request.form['cid']
    qry="UPDATE `complaint` SET `reply`=%s WHERE `id`=%s"
    val=(reply,cid)
    iud(qry,val)
    return jsonify({'task': 'success'})
app.run(host='0.0.0.0',port='5000')
