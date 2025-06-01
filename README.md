# Exploratory-Data-Analysis-on-COVID-19



# COVID-19 Cases and Vaccination Analysis

This project analyzes the relationship between daily new COVID-19 cases and vaccination rates across multiple countries — specifically the US, India, the United Kingdom, and Brazil. It includes data preprocessing, time-series visualization, and correlation analysis.

## 📁 Project Structure

```
.
├── covid19/                             # Folder containing the dataset(s)
├── Output fig_1.png                     # Time-series plot: Cases vs Vaccination (scaled)
├── Output fig_2.png                     # Bar chart: Correlation by country
├── analysis.ipynb                       # Jupyter notebook with code and visualizations (if included)
└── README.md                            # Project documentation
```

## 📊 Visualizations

- **Figure 1:** Time-series plot showing daily new COVID-19 cases and scaled vaccination rates for US, India, UK, and Brazil.
- **Figure 2:** Bar chart depicting correlation between new case counts and vaccination rates for each country.

## 📌 Key Insights

- **United Kingdom** shows a **positive correlation**, likely due to increased testing alongside vaccination efforts.
- **India** has a **moderate negative correlation**, suggesting a potential reduction in cases with vaccination rollout.
- **US** and **Brazil** show weaker or slightly negative correlations.

## 📦 Dataset

- Source: [Johns Hopkins University], [Our World in Data], or similar public datasets.
- Format: CSV or similar, located in the `covid19/` directory.

## 🛠️ Requirements

To run the analysis and generate the plots, install the following packages:

```bash
pip install pandas matplotlib seaborn numpy
```

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/covid-vaccination-analysis.git
   cd covid-vaccination-analysis
   ```

2. Open and run the Jupyter notebook (if provided):
   ```bash
   jupyter notebook analysis.ipynb
   ```

## 📄 License

This project is licensed under the MIT License.

## 🙌 Acknowledgements

- Johns Hopkins University COVID-19 Data Repository  
- Our World in Data  
