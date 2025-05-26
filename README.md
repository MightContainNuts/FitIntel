# FitIntel
updated: 2025-05-26

**FitIntel** is a personal health and activity tracking application built with Python and PyQt. It uses AI-based analysis to provide meaningful insights into your fitness and well-being over time. The app focuses on endurance, functional strength, and long-term usability.

## Features

- 📊 Interactive dashboard with health metrics and activity data
- 🧠 AI-powered assessment and personalized feedback (planned)
- 📈 Matplotlib-based visualizations
- 🗂️ Modular design with integration to Strava and Apple Health
- 🧘 Focus on endurance and functional strength over aesthetics

## Installation

```bash
git clone https://github.com/MightContainNuts/FitIntel
cd FitIntel
pip install -r requirements.txt
```

## Requirements
	•	Python 3.8+
	•	PyQt5
	•	matplotlib

Install them via:
```
pip install PyQt5 matplotlib
```
## Usage
```aiignore
python main.py
```

## Project Structure
```aiignore
vitalscope/
├── main.py             # Main GUI application
├── dashboard.py        # HealthDashboard widget
├── analysis/           # Placeholder for AI models (future)
├── data/               # Data import and transformation (planned)
├── db/                 # Database models handlers
├── services/           # additional tools for handling data
└── README.md
```

## Roadmap
- Import health data from fitness APIs (Strava, Apple)
- Create user profile and goals
- Integrate AI-based trend analysis
- Export reports (PDF, CSV)
- Theme and layout customizations


## Licence
This project is licensed under the MIT License.


Built with ❤️ for a healthier, stronger future.