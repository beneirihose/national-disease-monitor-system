#main.py
import config
from file_manager import FileManager
from analysis_manager import AnalysisManager
from visualization_manager import VisualizationManager

class HealthSystemApp:
    def __init__(self):
        # Initialize our specialized workers
        self.file_manager = FileManager()
        self.analyzer = AnalysisManager()
        self.visualizer = VisualizationManager()

    def input_data_userinterface(self):
        """Handles the user interface for inputting data."""
        date = self.file_manager.get_valid_date()
        
        daily_records = []
        for province in config.PROVINCES:
            print(f"\n--- Enter data for {province} ---")
            record = {"Date": date, "Province": province}
            
            for disease in config.DISEASES:
                while True:
                    try:
                        val = int(input(f"  {disease}: "))
                        if val < 0: raise ValueError
                        record[disease] = val
                        break
                    except ValueError:
                        print("  Invalid number.")
            
            daily_records.append(record)
        
        # Delegate saving to the file manager
        self.file_manager.save_records(daily_records)

    def run(self):
        while True:
            print("\n--- RWANDA HEALTH MONITORING SYSTEM ---")
            print("1. Input Daily Data")
            print("2. Analyze Data")
            print("3. Visualize Data")
            print("4. Exit")
            
            choice = input("Select: ")

            if choice == '1':
                self.input_data_userinterface()
            elif choice == '2':
                self.analyzer.run_analysis()
            elif choice == '3':
                self.visualizer.show_graphs()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    app = HealthSystemApp()
    app.run()