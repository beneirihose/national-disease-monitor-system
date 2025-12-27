# file_manager.py
import os
import pandas as pd
from datetime import datetime
import config # Import our settings

class FileManager:
    def __init__(self):
        self.filename = config.CSV_FILENAME
        self.initialize_file()

    def initialize_file(self):
        """Creates the CSV if it doesn't exist."""
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["Date", "Province"] + config.DISEASES)
            df.to_csv(self.filename, index=False)

    def get_valid_date(self):
        """Asks user for a date and ensures it is YYYY-MM-DD."""
        while True:
            date_str = input("\nEnter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
                return date_str
            except ValueError:
                print("  ERROR: Invalid format. Please use Year-Month-Day (e.g., 2025-05-20).")

    def save_records(self, records):
        """Appends a list of dictionaries to the CSV."""
        df_new = pd.DataFrame(records)
        # Append mode 'a', if file exists don't write header
        header_mode = not os.path.exists(self.filename)
        df_new.to_csv(self.filename, mode='a', header=header_mode, index=False)
        print("\nData saved successfully to storage!")

    def load_data(self):
        """Reads the CSV and returns a DataFrame."""
        if os.path.exists(self.filename) and os.stat(self.filename).st_size > 0:
            return pd.read_csv(self.filename)
        return pd.DataFrame() # Return empty if file not found
# file_manager.py
import os
import pandas as pd
from datetime import datetime
import config # Import our settings

class FileManager:
    def __init__(self):
        self.filename = config.CSV_FILENAME
        self.initialize_file()

    def initialize_file(self):
        """Creates the CSV if it doesn't exist."""
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["Date", "Province"] + config.DISEASES)
            df.to_csv(self.filename, index=False)

    def get_valid_date(self):
        """Asks user for a date and ensures it is YYYY-MM-DD."""
        while True:
            date_str = input("\nEnter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
                return date_str
            except ValueError:
                print("  ERROR: Invalid format. Please use Year-Month-Day (e.g., 2025-05-20).")

    def save_records(self, records):
        """Appends a list of dictionaries to the CSV."""
        df_new = pd.DataFrame(records)
        # Append mode 'a', if file exists don't write header
        header_mode = not os.path.exists(self.filename)
        df_new.to_csv(self.filename, mode='a', header=header_mode, index=False)
        print("\nData saved successfully to storage!")

    def load_data(self):
        """Reads the CSV and returns a DataFrame."""
        if os.path.exists(self.filename) and os.stat(self.filename).st_size > 0:
            return pd.read_csv(self.filename)
        return pd.DataFrame() # Return empty if file not found