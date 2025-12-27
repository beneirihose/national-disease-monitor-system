import matplotlib.pyplot as plt
import config
from file_manager import FileManager
from matplotlib.gridspec import GridSpec
class VisualizationManager:
    def __init__(self):
        self.file_manager = FileManager()

    def show_graphs(self):
        df = self.file_manager.load_data()

        if df.empty:
            print("No data available to visualize.")
            return
        plt.close('all')  # Close any existing plots
        # Calculate total cases per disease for the pie chart
        fig = plt.figure(figsize=(14, 18))
        ax1 = fig.add_subplot(2, 2, 1)
        total_per_disease = df[config.DISEASES].sum()
       

        total_per_disease.plot(kind='bar', color='teal', ax=ax1)
        ax1.set_title('Total Disease Cases in Country')
        ax1.set_ylabel('Number of Cases')
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        #plt.tight_layout()
        print("Displaying Bar Chart... (Close window to continue)")
        #plt.show()

        # --- Graph 2: Province Grouped Bar Chart ---
        ax2 = fig.add_subplot(2,2,2)
        province_group = df.groupby('Province')[config.DISEASES].sum()
       
        province_group.plot(kind='bar', ax=ax2)
        ax2.set_title('Disease Cases by Province')
        ax2.set_ylabel('Number of Cases')
        ax2.tick_params(axis='x', rotation=0)
        ax2.legend(title='Diseases')
        ax2.grid(axis='y', linestyle='--', alpha=0.7)
        #plt.tight_layout()
        print("Displaying Grouped Bar Chart... (Close window to continue)")
        #plt.show()

        # --- Graph 3: Pie Chart  ---
        ax3 = fig.add_subplot(2,1,2)

        #plt.figure(figsize=(8, 8))
        
        # We use the totals we calculated earlier
        ax3.pie(total_per_disease, 
                labels=total_per_disease.index, 
                autopct='%1.1f%%',  # Shows percentage with 1 decimal
                startangle=140, 
                colors=["#e73434","#1c6ab9","#37c837","#d39658", "#757598"])
        
        ax3.set_title('Distribution of Diseases (Percentage)')
        print("Displaying Pie Chart... (Close window to finish)")
       
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, hspace=0.5)
        plt.show()
        


        