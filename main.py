import psutil
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent, memory_info.total, memory_info.used, memory_info.available

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return disk_info.percent, disk_info.total, disk_info.used, disk_info.free

def log_usage_to_csv(cpu_usage, memory_percent, total_memory, used_memory, available_memory, disk_percent, disk_used, disk_free):
    with open('system_usage_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), cpu_usage, memory_percent, total_memory, used_memory, available_memory, disk_percent, disk_used, disk_free])

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.plot(df['Timestamp'], df['CPU Usage (%)'], label='CPU Usage (%)')
    plt.xlabel('Timestamp')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage Over Time')
    plt.legend()
    
    plt.subplot(2, 2, 2)
    plt.plot(df['Timestamp'], df['Memory Usage (%)'], label='Memory Usage (%)')
    plt.xlabel('Timestamp')
    plt.ylabel('Memory Usage (%)')
    plt.title('Memory Usage Over Time')
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(df['Timestamp'], df['Disk Usage (%)'], label='Disk Usage (%)')
    plt.xlabel('Timestamp')
    plt.ylabel('Disk Usage (%)')
    plt.title('Disk Usage Over Time')
    plt.legend()

    plt.tight_layout()
    plt.show()

def provide_recommendations(cpu_usage, memory_percent, disk_percent):
    recommendations = []
    
    if cpu_usage > 80:
        recommendations.append("CPU usage is high. Consider upgrading your CPU or optimizing your applications.")
    
    if memory_percent > 80:
        recommendations.append("Memory usage is high. Consider adding more RAM or closing unnecessary applications.")
    
    if disk_percent > 80:
        recommendations.append("Disk usage is high. Consider cleaning up or expanding disk space.")
    
    if not recommendations:
        recommendations.append("System resources are within normal ranges.")
    
    return recommendations

if __name__ == "__main__":
    csv_file_path = 'system_usage_log.csv'
    try:
        with open(csv_file_path, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'CPU Usage (%)', 'Memory Usage (%)', 'Total Memory (Bytes)', 'Used Memory (Bytes)', 'Available Memory (Bytes)', 'Disk Usage (%)', 'Disk Used (Bytes)', 'Disk Free (Bytes)'])
    except FileExistsError:
        pass

cpu_usage = get_cpu_usage()
memory_percent, total_memory, used_memory, available_memory = get_memory_usage()
disk_percent, disk_total, disk_used, disk_free = get_disk_usage()

print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_percent}%")
print(f"Total Memory: {total_memory / (1024 ** 3):.2f} GB")
print(f"Used Memory: {used_memory / (1024 ** 3):.2f} GB")
print(f"Available Memory: {available_memory / (1024 ** 3):.2f} GB")
print(f"Disk Usage: {disk_percent}%")
print(f"Disk Used: {disk_used / (1024 ** 3):.2f} GB")
print(f"Disk Free: {disk_free / (1024 ** 3):.2f} GB")

log_usage_to_csv(cpu_usage, memory_percent, total_memory, used_memory, available_memory, disk_percent, disk_used, disk_free)

recommendations = provide_recommendations(cpu_usage, memory_percent, disk_percent)
print("Recommendations:")
for rec in recommendations:
    print(f"- {rec}")