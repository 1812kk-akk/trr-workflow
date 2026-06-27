import pandas as pd
import os

# Input and output paths
input_folder = "data"
output_file = "output/output_format.xlsx"

# Collect all Excel files in data/
for file in os.listdir(input_folder):
    if file.endswith(".xlsx"):
        xls = pd.ExcelFile(os.path.join(input_folder, file))
        
        # Loop through all sheets
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet)
            
            # Apply transformation rules here
            # Example: split Machines vs Parts, calculate totals
            # (Use instructions.md as your guide)
            
            print(f"Processed {sheet} from {file}")

# Save consolidated output
# For now, just create a blank Excel to confirm workflow
pd.DataFrame({"Status":["Success"]}).to_excel(output_file, index=False)
