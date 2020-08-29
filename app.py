# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:26:55 2020

@author: pradh
"""


from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.sqlite3'
app.config['SECRET_KEY'] = "prady"
db = SQLAlchemy(app)

class ticket(db.Model):
   id = db.Column('tid',db.Integer, primary_key = True)
   name = db.Column(db.String(100),nullable=False)
   time = db.Column(db.DateTime,nullable=False)
   phone = db.Column(db.String(200),nullable=False) 
   expired=db.Column(db.String(200),server_default="false")
   
def __init__(self, name, phone, time ):
   self.name = name
   self.time = time
   self.phone = phone
   self.expired='false'

@app.route('/')
def show():
   return render_template('show.html',tickets = ticket.query.all() )

@app.route('/query', methods = ['GET', 'POST'])
def query():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['phone'] or not request.form['time']:
         flash('Please enter all the fields', 'error')
      else:
         t=request.form['time']
        
         d=t[8:10]+'/'+t[5:7]+'/'+t[0:4]+' '+t[11:13]+':'+t[14:16]+':'+t[17:19]
         tickets = ticket(name=request.form['name'], phone=request.form['phone'],time=datetime.strptime(d, "%d/%m/%Y %H:%M:%S"),expired='false')
        
         if(ticket.query.filter_by(time=datetime.strptime(d, "%d/%m/%Y %H:%M:%S")).count()<=3):
             db.session.add(tickets)
             db.session.commit()
             flash('Ticket was successfully booked')
         else:
             flash("Slots full for the time")
         return redirect(url_for('show'))
   return render_template('query.html')



@app.route('/update', methods = ['GET', 'POST'])
def update():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['phone'] or not request.form['time']:
         flash('Please enter all the fields', 'error')
      else:
         t=request.form['time']
        
         d=t[8:10]+'/'+t[5:7]+'/'+t[0:4]+' '+t[11:13]+':'+t[14:16]+':'+t[17:19]
         
         ticket.query.filter_by(phone=request.form['phone']).update(dict(time=datetime.strptime(d, "%d/%m/%Y %H:%M:%S")))
         db.session.commit()
         flash('Time was successfully booked')
         return redirect(url_for('show'))
   return render_template('query.html')

@app.route('/allattime', methods = ['GET', 'POST'])
def allattime():
   t=request.form['time']
        
   d=t[8:10]+'/'+t[5:7]+'/'+t[0:4]+' '+t[11:13]+':'+t[14:16]+':'+t[17:19]
         
   return render_template('show.html',ticketsattime =ticket.query.filter_by(time = datetime.strptime(d, "%d/%m/%Y %H:%M:%S")).all())

@app.route('/deleteparticular',methods = ['GET', 'POST'])
def deleteparticular():
   t=request.form['phone']
   ticket.query.filter_by(phone=t).delete()
   db.session.commit()
   return render_template('show.html',tickets=ticket.query.all())

@app.route('/findusingid',methods = ['GET', 'POST'])
def findusingid():
   t=request.form['id']
   f=ticket.query.filter_by(id=t).all()
   return render_template('show.html',found=f,tickets=ticket.query.all())

@app.route('/deletegreat8',methods = ['GET', 'POST'])
def deletegreat8():
   f=ticket.query.all()
   for x in f:
       a=x.time.replace(microsecond=0)
       b=datetime.now().replace(microsecond=0)
       if(b>a):
           d=b-a;
           seconds=d.total_seconds()
           hours = seconds // 3600
           if(hours>8):
               ticket.query.filter_by(id=x.id).update(dict(expired='True'))
               db.session.commit()
   return render_template('show.html',tickets=ticket.query.all())

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)