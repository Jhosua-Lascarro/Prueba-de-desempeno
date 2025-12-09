# RWventas Sales Analysis

Sales data analysis and transformation project.

## What this project does

1. **Load data** - Reads sales CSV files
2. **Clean data** - Removes special characters and fixes formats
3. **Transform data** - Converts data types and removes missing values
4. **Create structure** - Organizes data into dimension and fact tables
5. **Store** - Saves results to PostgreSQL database

## Folders

- `data/` - Data in 3 phases: raw (original), staging (clean), curated (processed)
- `notebooks/` - Step-by-step analysis
- `src/` - Reusable code
- `docs/` - Reports and insights

## Notebooks

1. **01_inspection.ipynb** - Explores raw data
2. **02_cleaning.ipynb** - Cleans and standardizes data
3. **03_trasform.ipynb** - Converts data types
4. **04.schema.ipynb** - Creates final structure and loads to database

## Required files

### data/raw/
Must contain:
- `RWventas.csv` - Original sales data file

### .env
Create in project root:
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=database
POSTGRES_PORT=5432
```

## How to run

```bash
# Install dependencies
pip install -r requirements.txt

# Run notebooks in order
# Or use Docker
docker-compose up
```

## Requirements

- Python 3.9+
- PostgreSQL
- pandas, sqlalchemy, pyarrow

## Results

Main insights are in `docs/ACTIONABLE_INSIGHTS.md`
