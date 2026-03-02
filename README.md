# Online Retail Data Analysis

## Dataset (Brief)
This is an online retail transaction dataset data processing containing invoice-level purchase records for a UK-based online store.
Typical fields include invoice number, stock code, product description, quantity, invoice date, unit price, customer ID, and country. [Link to dataset](https://archive.ics.uci.edu/dataset/352/online+retail)

- Raw download/collection logic: [download_data.py](download_data.py)  
- Cleaned output used in analysis: [online_retail_cleaned.csv](online_retail_cleaned.csv)  
- Analysis notebook: [online_retail_analysis.ipynb](online_retail_analysis.ipynb)

## Data Processing Completed
The workflow in this project performs data preparation before analysis, including:

1. Loading/downloading source retail data.
2. Cleaning missing or invalid records.
3. Removing duplicate/noisy rows where needed.
4. Converting data types (for example, date/time and numeric fields).
5. Creating a cleaned dataset for downstream analysis and visualization.

## Recreate Local Environment (Python venv)
Assuming Python is installed and Jupyter Notebook is already available on your machine.

### 1) Create virtual environment
```bash
python -m venv venv
```

### 2) Activate virtual environment
- **Windows (PowerShell)**:
  ```bash
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (cmd)**:
  ```bash
  .\venv\Scripts\activate.bat
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3) Install dependencies
Dependencies are listed in [requirements.txt](requirements.txt).

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Run the Jupyter Notebook
From the project root:

```bash
jupyter notebook online_retail_analysis.ipynb
```

Then open and run cells in [online_retail_analysis.ipynb](online_retail_analysis.ipynb).

## Run Unit Tests
Test module location: [tests/test_download_data.py](tests/test_download_data.py)

Run all tests:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
