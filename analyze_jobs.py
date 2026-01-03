"""
Data Science Job Market Analyzer
Analyzes salary trends, top roles, and market insights from 19K+ job postings
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Neon Purple color scheme for Project 4
NEON_PURPLE = '#9d00ff'

print("=" * 70)
print("DATA SCIENCE JOB MARKET ANALYZER")
print("=" * 70)

# ============================================================================
# 1. LOAD AND CLEAN DATA
# ============================================================================
print("\n📊 Loading data...")
df = pd.read_csv('data/bquxjob_11397f55_19b041d03ab.csv')
roles_df = pd.read_csv('data/bquxjob_bca4f80_19b041e24b0.csv')

print(f"✅ Loaded {len(df)} job postings")
print(f"   Years: {df['year'].min()} - {df['year'].max()}")
print(f"   Countries: {df['company_location'].nunique()}")

# Clean data
print("\n🔧 Cleaning data...")

# Standardize location names
df['company_location'] = df['company_location'].replace({
    'United States': 'US',
    'United Kingdom': 'GB',
    'Canada': 'CA',
    'Germany': 'DE',
    'Spain': 'ES'
})

# Standardize employment type
df['employment_type'] = df['employment_type'].replace({
    'Full-Time': 'FT',
    'Part-Time': 'PT',
    'Contract': 'CT',
    'Freelance': 'FL'
})

# Standardize company size
df['company_size'] = df['company_size'].replace({
    'Small': 'S',
    'Medium': 'M',
    'Large': 'L'
})

# Merge with role categories
df = df.merge(roles_df, on='job_title', how='left')

# Fill missing categories
df['role_archetype'] = df['role_archetype'].fillna('Other')

print("✅ Data cleaned")

# ============================================================================
# 2. KEY STATISTICS
# ============================================================================
print("\n" + "=" * 70)
print("KEY STATISTICS")
print("=" * 70)

print(f"\nTotal Job Postings: {len(df):,}")
print(f"Average Salary: ${df['salary_in_usd'].mean():,.0f}")
print(f"Median Salary: ${df['salary_in_usd'].median():,.0f}")
print(f"Salary Range: ${df['salary_in_usd'].min():,.0f} - ${df['salary_in_usd'].max():,.0f}")

print(f"\n\nTop 10 Job Titles:")
print(df['job_title'].value_counts().head(10).to_string())

print(f"\n\nTop 10 Locations:")
print(df['company_location'].value_counts().head(10).to_string())

print(f"\n\nExperience Level Distribution:")
print(df['experience_level'].value_counts().to_string())

# ============================================================================
# 3. SALARY ANALYSIS
# ============================================================================
print("\n" + "=" * 70)
print("SALARY ANALYSIS")
print("=" * 70)

# By experience level
print("\nAverage Salary by Experience Level:")
exp_salary = df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)
for exp, salary in exp_salary.items():
    print(f"   {exp}: ${salary:,.0f}")

# By role
print("\nTop 10 Highest Paying Roles:")
role_salary = df.groupby('job_title')['salary_in_usd'].agg(['mean', 'count']).query('count >= 10').sort_values('mean', ascending=False).head(10)
print(role_salary.to_string())

# By location
print("\nTop 10 Highest Paying Locations:")
location_salary = df.groupby('company_location')['salary_in_usd'].agg(['mean', 'count']).query('count >= 20').sort_values('mean', ascending=False).head(10)
print(location_salary.to_string())

# ============================================================================
# 4. CREATE VISUALIZATIONS
# ============================================================================
print("\n📊 Creating visualizations...")

import os
os.makedirs('visualizations', exist_ok=True)

plt.style.use('dark_background')

# Visualization 1: Salary Trends Over Time
print("\n   Creating salary trends chart...")
fig, ax = plt.subplots(figsize=(12, 6))
yearly_avg = df.groupby('year')['salary_in_usd'].mean()
ax.plot(yearly_avg.index, yearly_avg.values, marker='o', linewidth=3, 
        markersize=12, color=NEON_PURPLE)
ax.fill_between(yearly_avg.index, yearly_avg.values, alpha=0.3, color=NEON_PURPLE)
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Average Salary (USD)', fontsize=14, fontweight='bold')
ax.set_title('Data Science Salary Trends (2021-2024)', 
             fontsize=16, fontweight='bold', color=NEON_PURPLE, pad=20)
ax.grid(alpha=0.3, linestyle='--')
# Format y-axis as currency
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
plt.tight_layout()
plt.savefig('visualizations/salary_trends.png', dpi=300, bbox_inches='tight', facecolor='black')
plt.close()
print("✅ Saved: salary_trends.png")

# Visualization 2: Top 15 Paying Roles
print("   Creating top roles chart...")
fig, ax = plt.subplots(figsize=(12, 10))
top_roles = df.groupby('job_title')['salary_in_usd'].agg(['mean', 'count']).query('count >= 20').sort_values('mean', ascending=False).head(15)
bars = ax.barh(range(len(top_roles)), top_roles['mean'], 
               color=NEON_PURPLE, edgecolor='white', linewidth=2)
ax.set_yticks(range(len(top_roles)))
ax.set_yticklabels(top_roles.index)
ax.invert_yaxis()
ax.set_xlabel('Average Salary (USD)', fontsize=14, fontweight='bold')
ax.set_title('Top 15 Highest Paying Data Science Roles', 
             fontsize=16, fontweight='bold', color=NEON_PURPLE, pad=20)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
# Add count labels
for i, (idx, row) in enumerate(top_roles.iterrows()):
    ax.text(row['mean'], i, f"  n={int(row['count'])}", 
            va='center', fontsize=9, color='white')
plt.tight_layout()
plt.savefig('visualizations/top_paying_roles.png', dpi=300, bbox_inches='tight', facecolor='black')
plt.close()
print("✅ Saved: top_paying_roles.png")

# Visualization 3: Salary by Experience Level
print("   Creating experience level chart...")
fig, ax = plt.subplots(figsize=(10, 6))
exp_order = ['Entry', 'Mid', 'Senior', 'Executive']
exp_data = df.groupby('experience_level')['salary_in_usd'].mean().reindex(exp_order)
bars = ax.bar(range(len(exp_data)), exp_data.values, 
              color=NEON_PURPLE, edgecolor='white', linewidth=2)
ax.set_xticks(range(len(exp_data)))
ax.set_xticklabels(exp_data.index)
ax.set_ylabel('Average Salary (USD)', fontsize=14, fontweight='bold')
ax.set_title('Salary by Experience Level', 
             fontsize=16, fontweight='bold', color=NEON_PURPLE, pad=20)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
# Add value labels on bars
for i, v in enumerate(exp_data.values):
    ax.text(i, v, f'${v/1000:.0f}K', ha='center', va='bottom', 
            fontsize=12, fontweight='bold', color='white')
plt.tight_layout()
plt.savefig('visualizations/salary_by_experience.png', dpi=300, bbox_inches='tight', facecolor='black')
plt.close()
print("✅ Saved: salary_by_experience.png")

# Visualization 4: Top Locations
print("   Creating top locations chart...")
fig, ax = plt.subplots(figsize=(12, 8))
top_locations = df.groupby('company_location')['salary_in_usd'].agg(['mean', 'count']).query('count >= 30').sort_values('mean', ascending=False).head(15)
bars = ax.barh(range(len(top_locations)), top_locations['mean'], 
               color=NEON_PURPLE, edgecolor='white', linewidth=2)
ax.set_yticks(range(len(top_locations)))
ax.set_yticklabels(top_locations.index)
ax.invert_yaxis()
ax.set_xlabel('Average Salary (USD)', fontsize=14, fontweight='bold')
ax.set_title('Top 15 Highest Paying Locations (min 30 jobs)', 
             fontsize=16, fontweight='bold', color=NEON_PURPLE, pad=20)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
plt.tight_layout()
plt.savefig('visualizations/top_locations.png', dpi=300, bbox_inches='tight', facecolor='black')
plt.close()
print("✅ Saved: top_locations.png")

# Visualization 5: Company Size Impact
print("   Creating company size chart...")
fig, ax = plt.subplots(figsize=(10, 6))
size_map = {'S': 'Small', 'M': 'Medium', 'L': 'Large'}
size_data = df.groupby('company_size')['salary_in_usd'].mean()
size_data.index = size_data.index.map(size_map)
bars = ax.bar(range(len(size_data)), size_data.values, 
              color=NEON_PURPLE, edgecolor='white', linewidth=2)
ax.set_xticks(range(len(size_data)))
ax.set_xticklabels(size_data.index)
ax.set_ylabel('Average Salary (USD)', fontsize=14, fontweight='bold')
ax.set_title('Salary by Company Size', 
             fontsize=16, fontweight='bold', color=NEON_PURPLE, pad=20)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
# Add value labels
for i, v in enumerate(size_data.values):
    ax.text(i, v, f'${v/1000:.0f}K', ha='center', va='bottom', 
            fontsize=12, fontweight='bold', color='white')
plt.tight_layout()
plt.savefig('visualizations/salary_by_company_size.png', dpi=300, bbox_inches='tight', facecolor='black')
plt.close()
print("✅ Saved: salary_by_company_size.png")

# Visualization 6: Most Common Jobs
print("   Creating job distribution chart...")
fig, ax = plt.subplots(figsize=(12, 8))
top_jobs = df['job_title'].value_counts().head(15)
bars = ax.barh(range(len(top_jobs)), top_jobs.values, 
               color=NEON_PURPLE, edgecolor='white', linewidth=2)
ax.set_yticks(range(len(top_jobs)))
ax.set_yticklabels(top_jobs.index)
ax.invert_yaxis()
ax.set_xlabel('Number of Job Postings', fontsize=14, fontweight='bold')
ax.set_title('15 Most Common Data Science Job Titles', 
             fontsize=16, fontweight='bold', color=NEON_PURPLE, pad=20)
ax.grid(axis='x', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('visualizations/most_common_jobs.png', dpi=300, bbox_inches='tight', facecolor='black')
plt.close()
print("✅ Saved: most_common_jobs.png")

# ============================================================================
# 5. SUMMARY STATISTICS
# ============================================================================
print("\n" + "=" * 70)
print("ANALYSIS COMPLETE!")
print("=" * 70)

print(f"\n✅ Analyzed {len(df):,} job postings")
print(f"✅ Created 6 visualizations")
print(f"✅ Average Salary: ${df['salary_in_usd'].mean():,.0f}")
print(f"✅ Top Role: {df['job_title'].value_counts().index[0]}")
print(f"✅ Top Location: {df['company_location'].value_counts().index[0]}")

print("\n🚀 Ready for deployment!")
