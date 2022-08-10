import json
a=[{"id":94,
   "name":"patient1",
   "age":48,
   "gender":"male",
   "mobile":[9494949494,123456987],
   "email":'patient1@gmail.com',
   "address":'Vellore',
   "Symptom":"Fever",
   },
{
   "id":105,
   "name":"patient2",
   "age":28,
   "gender":"Female",
   "mobile":[9595959595,2587413692],
   "email":'patient2@gmail.com',
   "address":'Ellure',
   "Symptom":"Cough",
   }]
while(True):
   choice=int(input('Enter Your Choice : '))
   if(choice==1):
      dump1 = json.dumps(a, indent=4)
      print('Data set: ',dump1)
      print(type(dump1))
   elif(choice==2):
      try :
         with open("Patient_Details","w") as file:
             json.dump(a,file,indent=4)
         print("Successfully created........!")
      except Exception as e:
         print(e)
   else:
      print('Improper Selection')
      exit()