import numpy as np

# Given data
query_execution_durations = [0.2662, 0.2514, 0.2329, 0.18999, 0.23155, 0.18917, 0.1868, 0.20817]
read_latencies = [0.2131, 0.2231, 0.2287, 0.17366, 0.2205, 0.17654, 0.1715, 0.19018]

# Function to calculate confidence interval
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # ddof=1 for sample standard deviation
    z_score = 1.96  # For 95% confidence
    h = z_score * std_dev / np.sqrt(n)
    return mean, mean - h, mean + h

# Calculate confidence intervals
query_mean, query_ci_lower, query_ci_upper = confidence_interval(query_execution_durations)
latency_mean, latency_ci_lower, latency_ci_upper = confidence_interval(read_latencies)

# Print the results
print(f"Query Execution Duration (sec): Mean = {query_mean:.5f}, 95% CI = ({query_ci_lower:.5f}, {query_ci_upper:.5f})")
print(f"Read Latency (sec): Mean = {latency_mean:.5f}, 95% CI = ({latency_ci_lower:.5f}, {latency_ci_upper:.5f})")
