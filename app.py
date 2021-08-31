from flask import Flask,render_template,url_for,redirect,request
import numpy as np
import pickle 

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/predict', methods = ["GET", "POST"])

def predict():
    if request.method == 'POST':
        mf_year = int(request.form['Year'])
        Mileage = int(request.form['Mileage'])
        Engine = int(request.form['Engine'])
        KDriven = int(request.form['KDriven'])
        logkd = np.log(KDriven)

        # Location details, make it comatible with dymmies
        location=request.form['Location']
        if (location == 'Bangalore'):
            bangalore = 1
            chennai = 0
            coimbatore =0
            delhi = 0
            hyderabad = 0
            jaipur = 0
            kochi = 0
            kolkata = 0
            mumbai = 0
            pune = 0
        elif (location == 'Chennai'):
            bangalore = 0
            chennai = 1
            coimbatore =0
            delhi = 0
            hyderabad = 0
            jaipur = 0
            kochi = 0
            kolkata = 0
            mumbai = 0
            pune = 0
        elif (location == 'Coimbatore'):
            bangalore = 0
            chennai = 0
            coimbatore =1
            delhi = 0
            hyderabad = 0
            jaipur = 0
            kochi = 0
            kolkata = 0
            mumbai = 0
            pune = 0
        elif (location == 'Delhi'):
            bangalore = 0
            chennai = 0
            coimbatore =0
            delhi = 1
            hyderabad = 0
            jaipur = 0
            kochi = 0
            kolkata = 0
            mumbai = 0
            pune = 0
        elif (location == 'Hyderabad'):
            bangalore = 0
            chennai = 0
            coimbatore =0
            delhi = 0
            hyderabad = 1
            jaipur = 0
            kochi = 0
            kolkata = 0
            mumbai = 0
            pune = 0
        elif (location == 'Jaipur'):
            bangalore = 0
            chennai = 0
            coimbatore =0
            delhi = 0
            hyderabad = 0
            jaipur = 1
            kochi = 0
            kolkata = 0
            mumbai = 0
            pune = 0
        elif (location == 'Kochi'):
            bangalore = 0
            chennai = 0
            coimbatore =0
            delhi = 0
            hyderabad = 0
            jaipur = 0
            kochi = 1
            kolkata = 0
            mumbai = 0
            pune = 0
        elif (location == 'Kolkata'):
            bangalore = 0
            chennai = 0
            coimbatore =0
            delhi = 0
            hyderabad = 0
            jaipur = 0
            kochi = 0
            kolkata = 1
            mumbai = 0
            pune = 0
        elif (location == 'Mumbai'):
            bangalore = 0
            chennai = 0
            coimbatore =0
            delhi = 0
            hyderabad = 0
            jaipur = 0
            kochi = 0
            kolkata = 0
            mumbai = 1
            pune = 0
        else :
            bangalore = 0
            chennai = 0
            coimbatore =0
            delhi = 0
            hyderabad = 0
            jaipur = 0
            kochi = 0
            kolkata = 0
            mumbai = 0
            pune = 1
        
        # fuel type
        ftype=request.form['ftype']
        if ftype == 'Diesel':
            Diesel = 1
            Petrol = 0
            LPG = 0
        elif ftype == 'Petrol':
            Diesel = 0
            Petrol = 1
            LPG = 0
        else:
            Diesel = 0
            Petrol = 0
            LPG = 1
        
        #Engine Emiision type
        etype=request.form['etype']
        if etype=='Automatic':
            emission_type = 0
        else:
            emission_type = 1
        
        # with open('F:\Flask_learning\car_price\Pk_RandomForest.pkl','rb') as file:
        #     model=pickle.load(file)
        
        with open('lrm.pkl','rb') as file:
             model=pickle.load(file)
        
        price=model.predict([[mf_year,
                              Mileage,
                              Engine,
                              logkd,
                              bangalore,
                              chennai,
                              coimbatore,
                              delhi,
                              hyderabad,
                              jaipur,
                              kochi,
                              kolkata,
                              mumbai,
                              pune,
                              Diesel,
                              Petrol,
                              LPG,
                              emission_type]])
        car_price=np.exp(price)
        car_price=round(car_price[0],2)
        print('predicted car price is {car_price} Lakhs')

        return render_template('home.html',prediction_text="Your car price is Rs. {} Lakhs".format(car_price))

    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
