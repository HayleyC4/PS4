import os
import requests

API_KEY = os.environ["NASA_API_KEY"]
url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"

params = {
    "api_key": API_KEY,
    "start_date": "2025-01-01",
    "end_date": "2025-01-07"
}

response = requests.get(url, params=params, timeout=90)
response.raise_for_status()
data = response.json()

print("Entries retrieved:", len(data))
print("Dates returned:", [item["date"] for item in data])


import matplotlib.pyplot as plt

# Count the words in each explanation
dates = []
word_counts = []

for item in data:
    explanation = item.get("explanation", "")
    
    if explanation:
        dates.append(item["date"])
        word_counts.append(len(explanation.split()))

# Create the bar graph
plt.figure(figsize=(10, 5))
plt.bar(dates, word_counts)

plt.title("NASA APOD Explanation Length by Date")
plt.xlabel("Date")
plt.ylabel("Word Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save and display the graph
plt.savefig("nasa_apod_graph.png", dpi=300)
plt.show()
