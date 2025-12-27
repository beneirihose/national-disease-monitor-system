# analysis_manager.py
import pandas as pd
import config
from file_manager import FileManager

class AnalysisManager:
    def __init__(self):
        self.file_manager = FileManager()

    def run_analysis(self):
        df = self.file_manager.load_data()

        if df.empty:
            print("\nNo data found to analyze.")
            return

        print("\n" + "="*75)
        print(f"{'DATA ANALYSIS REPORT':^75}") # Center align the title
        print("="*75)

        # --- Step 1: Build a list of data for our table ---
        summary_data = []

        for disease in config.DISEASES:
            # A. Calculate Countrywide Total
            total_cases = df[disease].sum()
            
            # B. Find the Province with the highest cases for this disease
            prov_sum = df.groupby('Province')[disease].sum()
            top_prov = prov_sum.idxmax()
            top_val = prov_sum.max()
            
            # C. Add to our list
            summary_data.append({
                "Disease Name": disease,
                "Total Cases (National)": total_cases,
                "Most Affected Province": top_prov,
                "Cases in Province": top_val
            })

        # --- Step 2: Convert to DataFrame for pretty printing ---
        summary_df = pd.DataFrame(summary_data)
        
        # print(summary_df.to_string(index=False)) renders the table without row numbers
        # col_space padding helps keep columns aligned
        print(summary_df.to_string(index=False, col_space=15, justify='left'))

        # --- Step 3: Overall Summary (The "Winner" Province) ---
        print("-" * 75)
        
        # We calculate the sum of ALL diseases per province
        df_copy = df.copy()
        df_copy['Grand_Total'] = df_copy[config.DISEASES].sum(axis=1)
        province_totals = df_copy.groupby('Province')['Grand_Total'].sum()
        
        highest_prov = province_totals.idxmax()
        highest_val = province_totals.max()

        print(f" HIGHEST OVERALL CASES:  {highest_prov.upper()} is the most affected province")
        print(f"                         ({highest_val} total cases across all diseases)")
        print("=" * 75)