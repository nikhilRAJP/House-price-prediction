# California House Price Predictor App

This is a project I built to practice end-to-end machine learning. It's a Streamlit web app that predicts house prices in California based on data from the 1990 census.

I did all the data analysis in a Jupyter Notebook and then built the final app in Streamlit.

**Live App:** [Link to your Streamlit app]
**My Analysis Notebook:** [Link to your .ipynb notebook on GitHub]

---

## What it does:

Here's a screenshot of the app running:

![My App Screenshot](app_screenshot.png)

You can enter 8 features about a housing block (like median income, house age, location) and it will predict the median house price for that block.

---

## Tech I Used:

* **Python**
* **Pandas & NumPy** (for data cleaning and handling)
* **Matplotlib & Seaborn** (for making graphs)
* **Scikit-learn** (for building the models)
* **Streamlit** (for the web app)

---

## How I Built It:

1.  **Looked at the data (EDA):** First, I loaded the data and made some plots.
    * I found that **Median Income** was the most important feature for predicting the price.
    * I also found a lot of houses were "capped" at $500,000, which seemed like bad data, so I removed those rows.
2.  **Cleaned the data:**
    * Got rid of the $500k rows.
    * Used `StandardScaler` to put all the features on the same scale, since things like `Population` were huge and `MedInc` was small.
3.  **Trained Models:**
    * I tried **Linear Regression** first, which gave an RMSE of `$0.6429`.
    * Then I tried a **Random Forest** model, which was much better and got an RMSE of `$0.4653`.
    * I picked the Random Forest for the final app.

---

##  How to Run This Project:

1.  Clone this repo.
2.  Install the libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app from your terminal:
    ```bash
    python -m streamlit run app.py
    ```
