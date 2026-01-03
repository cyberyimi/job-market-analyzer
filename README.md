# Data Science Job Market Analyzer

**Analyzes 19,558 data science job postings to uncover salary trends, top roles, and market insights.**

---

## What This Does

Scrapes and analyzes real job posting data to answer questions like:
- What do data science roles actually pay?
- Which jobs pay the most?
- How does experience level affect salary?
- Which companies and locations offer the best compensation?

Built using Python, pandas, and data visualization libraries with neon purple styling.

---

## Key Findings

Job Market Overview:
- 19,558 job postings analyzed (2021-2024)
- Average salary: $148,705
- Median salary: $140,100
- Salary range: $15K - $800K

Top Paying Roles:
- AI Architect: $247K avg
- Director of Data Science: $212K avg
- ML Engineer: $200K avg
- Applied Scientist: $190K avg
- Research Scientist: $189K avg

By Experience Level:
- Executive: $192K avg
- Senior: $163K avg
- Mid-Level: $123K avg
- Entry: $89K avg

Most Common Jobs:
- Data Engineer: 4,088 postings
- Data Scientist: 3,883 postings
- Data Analyst: 2,839 postings
- Machine Learning Engineer: 2,000 postings

---

## How to Run

Analyze the data:
```bash
python analyze_jobs.py
```

Creates 6 visualizations showing:
- Salary trends over time
- Top paying roles
- Experience level comparison
- Geographic differences
- Company size impact
- Most common job titles

---

## What's Inside

- `analyze_jobs.py` - Main analysis script
- `data/` - 19K+ job postings with salary, location, experience level
- `visualizations/` - 6 charts with neon purple styling

---

## Data Source

Dataset includes:
- Job titles (Data Engineer, ML Engineer, Data Scientist, etc.)
- Salaries in USD
- Company locations (US, UK, Canada, Germany, etc.)
- Experience levels (Entry, Mid, Senior, Executive)
- Company sizes (Small, Medium, Large)
- Employment types (Full-time, Contract, Part-time)
- Years: 2021-2024

---

## Insights

Salary trends:
- Salaries increased 50% from 2021 to 2024
- US jobs pay significantly more than other countries
- Large companies don't always pay more than medium companies
- ML/AI roles command premium salaries

Market observations:
- Data Engineer is the most in-demand role
- Senior positions make up 65% of all postings
- Full-time positions dominate (95%+)
- Remote work became standard post-2021

---

## Built With

- Python - Data processing
- pandas - Data manipulation
- matplotlib - Visualizations
- seaborn - Statistical plots

---

## Author

Monse Rojo
- Portfolio: monserojo.com
- GitHub: @cyberyimi
- LinkedIn: linkedin.com/in/monse-rojo-6b70b3397/

---

Built with data and Python.
