from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a Pandas DataFrame
rules = pd.read_csv('rules.csv')
print(type(rules['antecedents'][0]))

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON array from the request
    json_data = request.json
    
    # Check if the JSON data contains the key 'items'
    
    # Convert the JSON array into a set
    data_set = set(json_data)

    print(data_set)
    
    # Search for the set in the DataFrame
    result = rules[rules['antecedents'] == data_set]

    print(result)
    
    # Convert the result to JSON and return it
    result_json = result.to_json(orient='records')
    return result_json

if __name__ == '__main__':
    app.run(debug=True, port=8080)
