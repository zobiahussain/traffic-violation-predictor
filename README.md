
# Traffic Violation Prediction using Urban + Weather Data

This project aims to predict **serious traffic violations** using historical violation data, geographical locations, and weather conditions. The goal is to identify **when and where serious violations are likely to occur**, so urban planners, traffic authorities, or smart-city systems can take preventive action.

Built using Python, LightGBM, and real datasets from Montgomery County (USA) and a public weather archive.


## Datasets Used

### 1. **Traffic Violations Dataset**
- Source: Kaggle ([US Traffic Violations - Montgomery County](https://www.kaggle.com/datasets/ujjwalchowdhury/traffic-violations-in-montgomery-county))
- Contains over 1 million records with timestamp, location (lat/lon), vehicle type, alcohol/work zone status, etc.
- Target variable (`is_serious_violation`) is derived from flags like:
  - `Accident = Yes`
  - `Alcohol = Yes`
  - `Commercial Vehicle = Yes`
  - `Work Zone = Yes`

### 2. **Weather History Dataset**
- Source: Kaggle ([Weather Dataset](https://www.kaggle.com/datasets/muthuj7/weather-dataset))
- Hourly weather data (Temperature, Humidity, Visibility, Precipitation Type)
- Merged on date with violation data

---

## Features Used

- `hour`, `day_of_week`, `month`, `is_weekend`
- `Latitude`, `Longitude` (location)
- `Temperature`, `Humidity`, `Visibility`, `Precip Type` (from weather)

---

## Machine Learning Approach

| Stage                  | Details                                         |
|------------------------|--------------------------------------------------|
| Model                  | LightGBM Classifier (fast & handles imbalance)   |
| Evaluation             | Classification report + Confusion Matrix        |
| Feature Importance     | Ranked and visualized                           |
| Class Balance          | `class_weight='balanced'` used to improve recall|

---

## Performance (With Weather)

| Class              | Precision | Recall | F1-Score |
|--------------------|-----------|--------|----------|
| Not Serious (0)    | 1.00      | 0.86   | 0.92     |
| Serious (1)        | 0.05      | 0.90   | 0.10     |

✅ The model improves significantly with weather data and learns patterns in serious incidents quite well (despite class imbalance).



## Visualizations Included

- Serious violations by time of day and week
- Interactive heatmap using Folium to show violation hotspots
- Feature importance barplots



## Output

- Trained model saved as: `traffic_violation_final_model.pkl`
- Notebook: `traffic_violation_prediction_lightgbm.ipynb`



## How to Run

1. Clone this repo or upload to [Kaggle Notebook](https://www.kaggle.com/code) or Jupyter.
2. Make sure your datasets are inside a `/data/` folder or adjust paths.
3. Run all cells in the notebook.
4. (Optional) Create a Streamlit app using `model_weather.pkl`.

---

## Future Improvements

- Use clustering (e.g., KMeans) to group violation zones
- Time series forecasting: predict daily or weekly counts
- Add SHAP or LIME for model explainability
- Deploy as a public web app (Streamlit or Flask)

---

## Author

Made with ❤️ by Zobia Hussain
Based in Pakistan | Passionate about AI for Urban Systems


## License

This project is for educational and research purposes. Attribution appreciated.

