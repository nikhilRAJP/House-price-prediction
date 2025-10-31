import streamlit as st
import pandas as pd
import joblib

# 1. LOAD YOUR SAVED FILES 
# Load the trained model
model = joblib.load('california_housing_model.pkl')

# Load the fitted scaler
scaler = joblib.load('scaler.pkl')

# Load the column names
model_columns = joblib.load('model_columns.pkl')


# 2. SET UP THE APP TITLE AND HEADER 
st.title('🏠 California House Price Predictor')
st.write("Enter the details of a housing block to get a predicted price.")


#  3. CREATE INPUT FIELDS FOR USER 
st.header("Housing Block Features")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input('Median Income (in $10,000s)', min_value=0.0, max_value=20.0, value=3.5, step=0.1)
    HouseAge = st.number_input('Median House Age (years)', min_value=1, max_value=100, value=25, step=1)
    AveRooms = st.number_input('Average Rooms per Household', min_value=1.0, max_value=20.0, value=5.0, step=0.1)
    AveBedrms = st.number_input('Average Bedrooms per Household', min_value=0.5, max_value=10.0, value=1.0, step=0.1)
    
with col2:
    Population = st.number_input('Block Population', min_value=1, max_value=40000, value=1500, step=10)
    AveOccup = st.number_input('Average Occupancy per Household', min_value=1.0, max_value=20.0, value=2.5, step=0.1)
    Latitude = st.number_input('Latitude', min_value=32.0, max_value=42.0, value=37.8, step=0.01)
    Longitude = st.number_input('Longitude', min_value=-125.0, max_value=-114.0, value=-122.0, step=0.01)


# 4. PREDICTION BUTTON 
if st.button('Predict House Value'):
    
    # 1. Create a DataFrame from the user's inputs
    # The dictionary keys MUST match the 'model_columns'
    user_data = {
        'MedInc': MedInc,
        'HouseAge': HouseAge,
        'AveRooms': AveRooms,
        'AveBedrms': AveBedrms,
        'Population': Population,
        'AveOccup': AveOccup,
        'Latitude': Latitude,
        'Longitude': Longitude
    }
    
    # Convert to DataFrame in the correct column order
    input_df = pd.DataFrame([user_data], columns=model_columns)

    # 2. Scale the user's input
    # Use the LOADED scaler to transform the data
    input_scaled = scaler.transform(input_df)

    # 3. Make the prediction
    # Use the LOADED model to predict
    prediction = model.predict(input_scaled)

    # 4. Display the result
    predicted_price = prediction[0] * 100000  # Convert back from $100k units

    st.success(f'The predicted median house value is: ${predicted_price:,.2f}')