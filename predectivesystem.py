import numpy as np
import pickle

# Specify the full path to the saved model
filename = r'C:\Users\LENOVO\OneDrive\Desktop\diabetes final\trained_model.sav'

# Load the saved model
loaded_model = pickle.load(open(filename,'rb'))

# Input data
input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

# Convert input data to a NumPy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array for predicting a single instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make a prediction
prediction = loaded_model.predict(input_data_reshaped)

# Print the prediction
print("Prediction:", prediction)

# Determine the diagnosis based on the prediction
if prediction[0] == 0:
    print("The person is not diabetic.")
else:
    print("The person is diabetic.")