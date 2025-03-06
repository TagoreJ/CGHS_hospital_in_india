# 🏥 CGHS Hospital Coverage Analysis in India

This project analyzes the distribution of hospitals empaneled under the **Central Government Health Scheme (CGHS)** across India. Using **Python, Machine Learning (K-Means Clustering), and Geospatial Visualization (Folium)**, we identify underserved areas and visualize healthcare accessibility.

---

## 📊 **Project Overview**
- **Data Source**: [data.gov.in - CGHS Hospital List](https://www.data.gov.in/resource/list-hospitals-empaneled-under-cghs-all-over-india)
- **Objective**: Identify states and cities with low CGHS hospital coverage.
- **Methods Used**:
  - **Data Cleaning & Preprocessing**
  - **Clustering with K-Means** to classify cities based on coverage levels.
  - **Mapping underserved areas using Folium**.
- **Output**: `cghs_coverage_map.html` (An interactive map)

---

## 📂 **Project Structure**
📁 CGHS_Hospital_Analysis/
│── 📄 cghs_hospitals.csv # Raw dataset
│── 📜 cghs_hospitals.py # Python script for data analysis & clustering
│── 📜 generate_map.py # Python script for map visualization
│── 🗺️ cghs_coverage_map.html # Final interactive map
│── 📄 requirements.txt # List of required Python packages
│── 📜 app.py # Streamlit app for online deployment
│── 📄 README.md # Project documentation

Copy

---

## 🚀 **How to Run Locally**

### 1️⃣ **Install Dependencies**  
Ensure you have Python 3.x installed, then install the required packages:  
```sh
pip install -r requirements.txt
2️⃣ Run the Clustering Script
sh
Copy
python cghs_hospitals.py
This script:

Groups cities based on hospital count.

Applies K-Means clustering to classify well-covered vs. underserved areas.

3️⃣ Generate & View the Map
sh
Copy
python generate_map.py
This script:

Uses Folium & Geopy to plot hospital clusters on an interactive map.

Saves the map as cghs_coverage_map.html (open it in any browser).

🌍 Deploying Online
1️⃣ Hosting the Map on GitHub Pages
To publish cghs_coverage_map.html online:

Upload the file to GitHub.

Go to Settings → Pages → Enable GitHub Pages.

Access your hosted map at:

Copy
https://yourusername.github.io/CGHS_Hospital_Analysis/cghs_coverage_map.html
2️⃣ Deploying with Streamlit
Run the Streamlit app locally or deploy it online:

sh
Copy
streamlit run app.py
📌 Key Insights from the Analysis
Well-covered cities (🟩 Green): High number of CGHS hospitals.

Medium coverage cities (🟧 Orange): Need slight improvements.

Underserved areas (🟥 Red): Require urgent attention for better healthcare access.

🛠 Tech Stack Used
Data Analysis: Pandas, Scikit-learn

Geospatial Mapping: Folium, Geopy

Web Deployment: GitHub Pages, Streamlit

📜 License
This project is open-source under the MIT License.

✨ Contributions & Feedback
Feel free to fork this repo, improve the analysis, or suggest ideas! 😊
🔗 Connect with me on LinkedIn

