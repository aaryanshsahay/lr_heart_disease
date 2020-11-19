from flask import Flask,request,render_template
from logging.config import dictConfig



import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

import smtplib
from email.message import EmailMessage



dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})






app=Flask(__name__)

df=pd.read_csv('framingham.csv')
df.dropna(axis=0,inplace=True)
X=df[['age','male','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose']]
y=df['TenYearCHD']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=101)
log_reg=LogisticRegression()
log_reg.fit(X_train,y_train)
y_pred=log_reg.predict(X_test)
	

str='ok'
@app.route('/',methods=['GET','POST'])
def result():
	str='before'
	if request.method=='POST':
		#return find_condition(user_age,user_gender,user_smoker,user_no_cigs,user_bp_meds,user_prev_stroke,user_diab,user_chol,user_sysbp,user_diabp,user_bmi,user_heartrate,user_glucose)


#def find_condition(user_age,user_gender,user_smoker,user_no_cigs,user_bp_meds,user_prev_stroke,user_diab,user_chol,user_sysbp,user_diabp,user_bmi,user_heartrate,user_glucose):
		result=''
		user_age=request.form['user_age']
	
		user_gender=request.form['user_gender']
		if user_gender.lower()=='male':
    			user_gender=1
		elif user_gender.lower()=='female':
    			user_gender=0
		#else:
    	#		result+="Please enter Gender (Male/Female)\n"

		user_smoker=request.form['user_smoker']
		if user_smoker.lower() =='yes':
    			user_smoker=1
    			user_no_cigs=request.form['user_no_cigs']
		elif user_smoker.lower()=='no':
    			user_smoker=0
    			user_no_cigs=0
    	#else:
    	#	user_no_cigs=0
    	#	result+="appropriate value for smoking cigerattes"

	
		user_bp_meds=request.form['user_bp_meds']
		if user_bp_meds.lower()=='yes':
    			user_bp_meds=1
		elif user_bp_meds.lower()=='no':
    			user_bp_meds=0
		#else:
    	#		result+="Enter proper information for BP meds (Yes/No)\n"

		user_prev_stroke=request.form['user_prev_stroke']
		if user_prev_stroke.lower()=='yes':
    			user_prev_stroke=1
		elif user_prev_stroke.lower()=='no':
    			user_prev_stroke=0
		#else:
    	#		result+="Enter proper information for prevelent stroke (Yes/No)\n"

		user_diab=request.form['user_diab']
		if user_diab.lower()=='yes':
    			user_diab=1
		elif user_diab.lower()=='no':
    			user_diab=0
		#else:
    	#		result+="Enter proper information for diabetes (Yes/No)\n"

		user_chol=request.form['user_chol']
		#if type(user_chol)==int:
		#	condition=True
		
		#else:

		#			result+="Enter an integer value for Cholestrol Level!\n"
	
		user_sysbp=request.form['user_sys_bp']
		#if type(user_sysbp)==float:
		#		condition=True
		#else:
		#		result+="Enter appropriate value for Systolic Blood Pressure!\n"
	
		user_diabp=request.form['user_dia_bp']
		#if type(user_diabp)==float:
		#		condition=True
		#else:
		#		result+="Enter appropriate value for Diastolic Blood Pressure!\n"
		
		user_bmi=request.form['user_bmi']
		#if type(user_bmi)==float:
		#		condition=True
		#else:
		#		result+="\nEnter appropriate value for Body Mass Index(BMI)!"
	
		user_heartrate=request.form['user_heartrate']
		#if type(user_heartrate)==int:
		#		condition=True
		#else:
		#		result+="\nPlease enter appropriate value for Heart Rate!"

		user_glucose=request.form['user_glucose']
		#if type(user_glucose)==int:
		#		condition=True
		#else:
		#		result+="\nPlease enter appropriate value for Glucose content!"


		user_data={
		'age':[user_age],
		'male':[user_gender],
		'currentSmoker':[user_smoker],
		'cigsPerDay':[user_no_cigs],
		'BPMeds':[user_bp_meds],
		'prevalentStroke':[user_prev_stroke],
		'diabetes':[user_diab],
		'totChol':[user_chol],
		'sysBP':[user_sysbp],
		'diaBP':[user_diabp],
		'BMI':[user_bmi],
		'heartRate':[user_heartrate],
		'glucose':[user_glucose]
		}

		df2=pd.DataFrame(user_data,columns=['age','male','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose'])
		y2_pred=log_reg.predict(df2)
	#	print('------------RESULT------------')
		
		if y2_pred==1:
			return render_template('highrisk.html')
		elif y2_pred==0:
			return render_template('lowrisk.html')
		else:
			return render_template('error.html')
		return render_template('index.html')
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)