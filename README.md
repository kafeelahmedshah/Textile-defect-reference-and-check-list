# Textile Defect Reference & Checklist App

**Student Roll No:** 25TE052  
**Department:** Textile Engineering  
**Framework:** Streamlit

## Project overview

A Streamlit web application that provides a searchable reference guide to common textile fabric defects. It explains each defect, its possible causes, inspection points, and simple remedies. It also includes a fabric inspection checklist that can be downloaded as a CSV file.

## Main assigned features

- Searchable guide to common fabric defects
- Defect descriptions and categories
- Possible causes of each defect
- Simple remedies and corrective actions
- Fabric inspection checklist
- Download inspection results as CSV
- Dashboard and project information page

## Assigned defects

1. Slub
2. Missing Pick
3. Hole
4. Oil Stain

Additional sample reference entries are included to demonstrate search and filtering.

## Project files

- `app.py` — Main Streamlit application
- `requirements.txt` — Required Python packages
- `README.md` — Project documentation

## Run locally

### 1. Install Python

Install Python 3.9 or newer.

### 2. Open the project folder

Open a terminal or command prompt inside the project folder.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser. If it does not open automatically, use the local URL displayed in the terminal (usually `http://localhost:8501`).

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt`, and `README.md`.
3. Open Streamlit Community Cloud and connect your GitHub account.
4. Select the repository and `app.py` as the main file.
5. Deploy the application.

## Important note

The listed causes and remedies are general educational guidance. Actual corrective action and fabric acceptance decisions should be based on the applicable textile inspection standard, fabric construction, process conditions, and quality-control procedures.
