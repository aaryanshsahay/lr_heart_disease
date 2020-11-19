import os
os.environ['PATH']

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

df=pd.read_csv("framingham.csv")
#print(df.head())

#print(df.isnull().sum())
df.dropna(axis=0,inplace=True)
#print(df.head())
#print(df.isnull().sum())

X=df[['age','male','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose']]
y=df['TenYearCHD']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=101)

log_reg=LogisticRegression()
log_reg.fit(X_train,y_train)
y_pred=log_reg.predict(X_test)

user_age=int(input("Enter Age:"))

user_gender=input("Gender:")
if user_gender.lower()=='male':
    user_gender=1
elif user_gender.lower()=='female':
    user_gender=0
else:
    print("Please enter Gender (Male/Female)")
user_Smoking=input("Do you smoke?")

if user_Smoking.lower() =='yes':
    user_no_cigs=int(input("How many cigs do you smoke perday:"))
    user_Smoking=1
elif user_Smoking.lower()=='no':
    user_Smoking=0
    user_no_cigs=0

user_bp_meds=input("Are you on Blood Pressure meds?")
if user_bp_meds.lower()=='yes':
    user_bp_meds=1
elif user_bp_meds.lower()=='no':
    user_bp_meds=0
else:
    print("Enter proper information for BP meds (Yes/No)")

user_prev_stroke=input("Have you ever experienced a stroke?")
if user_prev_stroke.lower()=='yes':
    user_prev_stroke=1
elif user_prev_stroke.lower()=='no':
    user_prev_stroke=0
else:
    print("Enter proper information for prevelent stroke (Yes/No)")

user_diab=input("Do you have diabetes?")
if user_diab.lower()=='yes':
    user_diab=1
elif user_diab.lower()=='no':
    user_diab=0
else:
    print("Enter proper information for diabetes (Yes/No)")
user_chol=int(input("What is your total cholestrol?"))

user_sys_bp=float(input("What is your systolic blood pressure?"))
user_dia_bp=float(input("What is your diastolic blood pressure?"))
user_bmi=float(input("What is your BMI?"))
user_heartrate=int(input("What is your heart rate?"))
user_glucose=int(input("What is your current glucose level?"))

confusion_matrix = metrics.confusion_matrix(y_test,y_pred)
#print(confusion_matrix)
print('----------------DISCLAIMER----------------')
print('The machine learning model trained has:')
print('Accuracy:',metrics.accuracy_score(y_test,y_pred))
print('Consult a certified professional for detailed analysis of your condition, this model may overfit/underfit! Please use this for reference only!')

user_data={
    'age':[user_age],
    'male':[user_gender],
    'currentSmoker':[user_Smoking],
    'cigsPerDay':[user_no_cigs],
    'BPMeds':[user_bp_meds],
    'prevalentStroke':[user_prev_stroke],
    'diabetes':[user_diab],
    'totChol':[user_chol],
    'sysBP':[user_sys_bp],
    'diaBP':[user_dia_bp],
    'BMI':[user_bmi],
    'heartRate':[user_heartrate],
    'glucose':[user_glucose]

}

df2=pd.DataFrame(user_data,columns=['age','male','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose'])
y2_pred=log_reg.predict(df2)
print('----------------RESULT----------------')
if y2_pred==1:
    print("You have high risk of developing a cardivascular disease in the next 10 years!")
elif y2_pred==0:
    print("You have low risk of developing a cardivascular disease in the next 10 years!")
