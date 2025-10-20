# Import necessary libraries
import pandas as pd
import joblib 
import numpy as np 
import os 
from django.conf import settings 
from django.shortcuts import render 

# Construct the absolute path to the model file 
model_path = os.path.join(settings.BASE_DIR, 'ml_models', 'fraud_detection_smote_rf.pkl') 
# load the trained model pipeline 
pipeline = joblib.load(model_path)

def predict_view(request):
    context = {
        'v_range': range(1, 29)  # Add this range for the template loop
    }
    if request.method == "POST":
        # Get features from the form
        features_dict = {}
        
        # Log-transform the Amount feature
        amount = float(request.POST.get('Amount', 0))
        features_dict["Amount_log"] = np.log1p(amount)
        features_dict["Hourly"] = int(request.POST.get('Hourly', 0))
        for i in range(1, 29):
            features_dict[f'V{i}'] = float(request.POST.get(f'V{i}', 0))
        

       # Convert dictionary to pd DataFrame
        input_df = pd.DataFrame([features_dict])

        # To ensure the order of columns matches the training data      
        training_column = ["Amount_log", "Hourly"] + [f'V{i}' for i in range(1, 29)]
        input_df = input_df[training_column]

        # Make prediction
        prediction = pipeline.predict(input_df)
        prediction_proba = pipeline.predict_proba(input_df) 

        # Get predicted class( 0 for Legitimate, 1 for Fraudulent) and confidence
        predicted_class = prediction[0]

        # Get the probability of the predicted class
        confidence_score = prediction_proba[0][predicted_class]

        # Set result and confidence in human-readable format
        result = "Fraudulent" if predicted_class == 1 else "Legitimate"
        confidence = f"{float(confidence_score) * 100:.2f}%"

        # Update context with results
        context['result'] = result
        context['confidence'] = confidence
        
        return render(request, 'fraud_app/predict.html', context)
    
    # This is for the GET request when the page first loads
    return render(request, 'fraud_app/predict.html', context)