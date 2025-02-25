app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the date from the request
    data = request.get_json()
    date = data['date']
    
    # Convert date to ordinal
    date_ordinal = pd.to_datetime(date).toordinal()
    
    # Make prediction
    prediction = model.predict(np.array([[date_ordinal]]))
    
    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)