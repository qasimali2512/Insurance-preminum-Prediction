import pickle
import pandas as pd
#add confidence score

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_output(user_input):
    input_data = pd.DataFrame([user_input])
    output = model.predict(input_data)
    confidence = model.predict_proba(input_data)

    return output[0], confidence[0].max()