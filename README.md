# House Price Prediction Using ML (joblib)
This project leverages machine learning to predict house prices based on the area of the property using a simple linear regression model. The integration is achieved through the joblib library for model persistence. A user-friendly web-based frontend showcases the predictions.

## Key Features
**Linear Regression Model**: The project utilizes a straightforward linear regression model to estimate house prices.
**joblib Integration:** The trained machine learning model is saved and loaded using joblib, ensuring efficient model persistence.
**Frontend Interface:** A user-friendly web interface allows users to input an area, returning an estimated house price.
**Data Visualization:** The application provides graphical representation of the linear regression line for a visual understanding of price predictions.
**Customization:** The project can be extended with more advanced models and additional features.

## Usage

**Requirements:** Ensure you have Python, joblib, and the required libraries installed. You can install them using the provided requirements.txt file.

## Usage

1. **Requirements**: Ensure you have Python, `joblib`, and the required libraries installed. You can install them using the provided `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

2. **Running the Application**: Execute the main script to run the application.

    ```bash
    python main.py
    ```

3. **Access the Frontend**: Open your web browser and navigate to `http://localhost:5000` to access the user interface.

4. **Input Area**: Enter the area of the house for which you want a price prediction.

5. **View Prediction**: The application will provide an estimated house price based on the input area.



## Use Cases
- Home Buyers and Sellers: Obtain quick estimates of house values for decision-making.
- Real Estate Agents: Provide clients with preliminary price estimates.
- Property Investors: Analyze potential returns on investment.

