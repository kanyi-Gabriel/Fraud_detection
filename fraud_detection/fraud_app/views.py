# fraud_app/views.py
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
        # ... your feature collection and prediction logic ...
        
        features = []
        
        amount = float(request.POST.get('Amount', 0))
        Amount_log = np.log1p(amount)
        features.append(Amount_log)

        hour = int(request.POST.get('Hourly', 0))
        features.append(hour)

        for i in range(1, 29):
            feature_value = float(request.POST.get(f'V{i}', 0))
            features.append(feature_value)

        prediction = pipeline.predict([features])[0]
        prediction_proba = pipeline.predict_proba([features])[0][1]

        result = "Fraudulent" if prediction == 1 else "Legitimate"
        confidence = f"{prediction_proba * 100:.2f}%"

        # Update context with results
        context['result'] = result
        context['confidence'] = confidence
        
        return render(request, 'fraud_app/predict.html', context)
    
    # This is for the GET request when the page first loads
    return render(request, 'fraud_app/predict.html', context)