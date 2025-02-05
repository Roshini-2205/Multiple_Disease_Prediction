import pickle
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)



# Load the saved models
diabetes_model = joblib.load('diabetes_model.sav')
parkinsons_model = joblib.load('parkinsons_model.sav')
kidney_model = joblib.load('kidney.sav')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    if request.method == 'POST':
        # Process the form data and make predictions for Diabetes
        Pregnancies = request.form['Pregnancies']
        Glucose = request.form['Glucose']
        BloodPressure = request.form['BloodPressure']
        SkinThickness = request.form['SkinThickness']
        Insulin = request.form['Insulin']
        BMI = request.form['BMI']
        DiabetesPedigreeFunction = request.form['DiabetesPedigreeFunction']
        Age = request.form['Age']


        if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            return render_template('diabetes.html', error_message='Please enter values for all fields.')

        try:
            Pregnancies = float(Pregnancies)
            Glucose = float(Glucose)
            BloodPressure = float(BloodPressure)
            SkinThickness = float(SkinThickness)
            Insulin = float(Insulin)
            BMI = float(BMI)
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
            Age = float(Age)
        except ValueError:
            return render_template('diabetes.html', error_message='Invalid input. Please enter valid numbers.')

        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

        return render_template('diabetes.html', diab_diagnosis=diab_diagnosis)

    return render_template('diabetes.html')


@app.route('/parkinsons', methods=['GET', 'POST'])
def parkinsons():
    if request.method == 'POST':
        # Process the form data and make predictions for Parkinson's
        fo = request.form['fo']
        fhi = request.form['fhi']
        flo = request.form['flo']
        Jitter_percent = request.form['Jitter_percent']
        Jitter_Abs = request.form['Jitter_Abs']
        RAP = request.form['RAP']
        PPQ = request.form['PPQ']
        DDP = request.form['DDP']
        Shimmer = request.form['Shimmer']
        Shimmer_dB = request.form['Shimmer_dB']
        APQ3 = request.form['APQ3']
        APQ5 = request.form['APQ5']
        APQ = request.form['APQ']
        DDA = request.form['DDA']
        NHR = request.form['NHR']
        HNR = request.form['HNR']
        RPDE = request.form['RPDE']
        DFA = request.form['DFA']
        spread1 = request.form['spread1']
        spread2 = request.form['spread2']
        D2 = request.form['D2']
        PPE = request.form['PPE']

        # Check if any input field is empty
        if not all([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                    Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
                    RPDE, DFA, spread1, spread2, D2, PPE]):
            error_message = "Please enter values for all fields"
            return render_template('parkinsons.html', error_message=error_message)

        try:
            # Convert input values to float
            fo = float(fo)
            fhi = float(fhi)
            flo = float(flo)
            Jitter_percent = float(Jitter_percent)
            Jitter_Abs = float(Jitter_Abs)
            RAP = float(RAP)
            PPQ = float(PPQ)
            DDP = float(DDP)
            Shimmer = float(Shimmer)
            Shimmer_dB = float(Shimmer_dB)
            APQ3 = float(APQ3)
            APQ5 = float(APQ5)
            APQ = float(APQ)
            DDA = float(DDA)
            NHR = float(NHR)
            HNR = float(HNR)
            RPDE = float(RPDE)
            DFA = float(DFA)
            spread1 = float(spread1)
            spread2 = float(spread2)
            D2 = float(D2)
            PPE = float(PPE)

            # Make predictions
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                               Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
                                                               RPDE, DFA, spread1, spread2, D2, PPE]])

            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[
                                                                               0] == 1 else "The person does'nt have Parkinson's disease"

            return render_template('parkinsons.html', parkinsons_diagnosis=parkinsons_diagnosis)

        except ValueError:
            error_message = "Invalid input values. Please enter valid numbers."
            return render_template('parkinsons.html', error_message=error_message)

    return render_template('parkinsons.html')



@app.route('/kidney', methods=['GET', 'POST'])
def kidney():
    if request.method == 'POST':
        # Process the form data and make predictions for Parkinson's
        age= request.form['age']
        bp = request.form['bp']
        al = request.form['al']
        su = request.form['su']
        rbc = request.form['rbc']
        pc = request.form['pc']
        pcc = request.form['pcc']
        ba = request.form['ba']
        bgr = request.form['bgr']
        bu = request.form['bu']
        sc = request.form['sc']
        pot = request.form['pot']
        wc = request.form['wc']
        htn = request.form['htn']
        dm= request.form['dm']
        cad= request.form['cad']
        pe = request.form['pe']
        ane = request.form['ane']


        # Check if any input field is empty
        if not all([age, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, pot, wc, htn, dm, cad, pe, ane]):
            error_message = "Please enter values for all fields"
            return render_template('kidney.html', error_message=error_message)

        try:
            # Convert input values to float
            age = float(age)
            bp = float(bp)
            al = float(al)
            su = float(su)
            rbc = float(rbc)
            pc = float(pc)
            pcc = float(pcc)
            ba = float(ba)
            bgr = float(bgr)
            bu = float(bu)
            sc = float(sc)
            pot = float(pot)
            wc = float(wc)
            htn = float(htn)
            dm = float(dm)
            cad = float(cad)
            pe = float(pe)
            ane = float(ane)

            # Make predictions
            kidney_prediction = kidney_model.predict([[age, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, pot, wc, htn, dm, cad, pe, ane]])

            kidney_diagnosis = "The person has kidney disease" if kidney_prediction[
                                                                               0] == 1 else "The person does not have kidney disease"

            return render_template('kidney.html', kidney_diagnosis=kidney_diagnosis)

        except ValueError:
            error_message = "Invalid input values. Please enter valid numbers."
            return render_template('kidney.html', error_message=error_message)

    return render_template('kidney.html')

if __name__ == '__main__':
    app.run(debug=True)

   
