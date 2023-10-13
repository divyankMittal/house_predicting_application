from flask import Flask,request,render_template
import pickle
from datetime import datetime
import pandas as pd

app=Flask(__name__)

#loading the model
with open('model_pickle','rb') as file:
  model=pickle.load(file)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    try:
         '''
        Required input for machine learning model
        1. Area 
        2. Bedrooms
        3. Bathrooms
        4. Balconies
        5. Status
        6. NewOrOld
        7. Parking
        8. Furnishing
        9. Lifts
        10. typeOfBuilding

        '''
         #syntax-->  var_name=request.form['<name which in present in html form(index.html)>']
         query_area=request.form['area']
         query_bedrooms=request.form['bedrooms']
         query_bathrooms=request.form['bathrooms']
         query_balconies=request.form['balconies']
         query_status=request.form['status']  #Categorical Data
         query_neworold=request.form['neworold'] #Categorical Data
         query_parking=request.form['parking']
         query_furnishing=request.form['furnishing'] #Categorical Data
         query_lifts=request.form['lifts']
         query_typeofbuilding=request.form['typeofbuilding'] #Categorical Data


         #For status 
         if query_status=="statusCondition_1":
            status = 1
         else:
            status = 0       

        # For neworold
         if query_neworold=="neworoldCondition_1":
            neworold = 0
         else:
            neworold = 1

        # For furnishing
         if query_furnishing=="furnishCondition_1":
            furnishing = 1
         elif query_furnishing == "furnishingCondition_2":
            furnishing = 2
         else :
            furnishing = 0

         # for type of building 
         if query_typeofbuilding == "typeofbuildingCondition_1":
            typeofbuilding = 0
         else :
            typeofbuilding = 1

         data = {
            "area": [query_area],
            "Bedrooms": [query_bedrooms],
            "Bathrooms": [query_bathrooms] ,
            "Balcony": [query_balconies],
            "Status": [status],
            "neworold": [neworold],
            "parking": [query_parking],
            "Furnished_status": [furnishing],
            "Lift": [query_lifts],
            "type_of_building": [typeofbuilding]    
         }
          
         model_data= pd.DataFrame(data)
        
         result=model.predict(model_data)[0]
         x=float(result)
         y="{:.0f}".format(x)

         return render_template('index.html',results=y)


    except ValueError:
        return render_template('index.html')
   

if __name__=="__main__":
    app.run(debug=True, port=8081,host='0.0.0.0')


