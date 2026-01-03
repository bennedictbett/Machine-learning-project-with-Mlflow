from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline
from mlProject import logger


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homePage():
    """Render the home page with prediction form"""
    return render_template('index.html')


@app.route('/train', methods=['GET'])
def training():
    """Trigger the training pipeline"""
    try:
        logger.info("Training initiated from web interface")
        os.system('python main.py')
        return "Training Completed Successfully!"
    except Exception as e:
        logger.error(f"Training failed: {str(e)}")
        return f"Training Failed: {str(e)}"


@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests from the HTML form"""
    try:
        # Get JSON data from request (your HTML sends JSON)
        data = request.json
        logger.info(f"Prediction request received: {data}")
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Create prediction pipeline and make prediction
        obj = PredictionPipeline()
        predict_result = obj.predict(df)
        
        logger.info(f"Prediction successful: {predict_result}")
        
        # Return prediction as JSON
        return jsonify({
            'prediction': predict_result.tolist(),
            'status': 'success'
        })
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        print('The Exception message is:', e)
        return jsonify({
            'error': str(e),
            'status': 'failed'
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)