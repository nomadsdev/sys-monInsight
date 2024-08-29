# System Monitoring and Analysis Tool 
 
## Overview
This project is a Python-based system monitoring and analysis tool designed to track and log the CPU, memory, and disk usage of your computer. The tool provides real-time usage statistics, logs data to a CSV file, and offers recommendations based on system performance. It also includes data visualization capabilities for analyzing historical usage trends. 
 
## Features
- **Real-Time Monitoring**: Captures CPU, memory, and disk usage statistics every second. 
- **Data Logging**: Logs usage data to a CSV file for historical analysis. 
- **Data Analysis**: Analyzes logged data and generates plots to visualize CPU, memory, and disk usage over time. 
- **Recommendations**: Provides suggestions for optimizing system performance based on current usage metrics. 
 
## Installation
1. **Clone the Repository** 
 
   ```bash 
   git clone https://github.com/nomadsdev/sys-monInsight.git 
   cd system-monitoring-tool 
   ``` 
 
2. **Install Dependencies** 
 
   Ensure you have Python 3.x installed. Then install the required Python packages using pip: 
 
   ```bash 
   pip install psutil pandas matplotlib 
   ``` 
 
## Usage
1. **Run the Monitoring Script** 
 
   Execute the monitoring script to start logging system usage data: 
 
   ```bash 
   python main.py 
   ``` 
 
   The script will log data to `system_usage_log.csv` and print real-time statistics and recommendations to the console. 
 
2. **Analyze Data** 
 
   To visualize the logged data, run the following script: 
 
   ```bash 
   python main.py 
   ``` 
 
   This script will read the `system_usage_log.csv` file and generate plots for CPU, memory, and disk usage over time. 
 
## Scripts 
### `main.py` 
 
- **Function**: Collects system usage data and logs it to a CSV file. 
- **Functions**: 
  - `get_cpu_usage()`: Retrieves the current CPU usage percentage. 
  - `get_memory_usage()`: Retrieves current memory usage statistics. 
  - `get_disk_usage()`: Retrieves current disk usage statistics. 
  - `log_usage_to_csv()`: Logs the collected data to `system_usage_log.csv`. 
  - `provide_recommendations()`: Provides recommendations based on system usage. 
 
### `analyze.py` 
 
- **Function**: Analyzes and visualizes the logged system usage data. 
- **Functions**: 
  - `analyze_data(file_path)`: Loads data from a CSV file and generates usage plots. 
 
## File Structure
- `monitor.py`: Script for monitoring and logging system usage. 
- `analyze.py`: Script for analyzing and visualizing logged data. 
- `system_usage_log.csv`: CSV file where usage data is logged. 
- `README.md`: This documentation file. 
 
## Recommendations
- **High CPU Usage**: Consider upgrading your CPU or optimizing applications. 
- **High Memory Usage**: Consider adding more RAM or closing unnecessary applications. 
- **High Disk Usage**: Consider cleaning up or expanding disk space. 
 
## License
This project is licensed under the MIT License.
