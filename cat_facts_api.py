
import requests
import matplotlib.pyplot as plt

# Step 1: Get cat facts from the API
url = "https://catfact.ninja/facts"

params = {"limit": 100}

response = requests.get(url, params=params, timeout=15)
response.raise_for_status()
data = response.json()

# Step 2: Extract just the cat facts
facts = [item["fact"] for item in data["data"]]

# Step 3: Calculate the length of each fact
fact_lengths = []

for fact in facts:
    fact_lengths.append((fact, len(fact)))

# Step 4: Sort facts from longest to shortest
fact_lengths.sort(key=lambda x: x[1], reverse=True)

# Select the five longest facts
top_five = fact_lengths[:5]

# Step 5: Print the results
print("The 5 Longest Cat Facts:\n")

for i, (fact, length) in enumerate(top_five, 1):
    print(f"{i}. {fact}")
    print(f"Length: {length} characters\n")

# Step 6: Create a bar graph
labels = [f"Fact {i}" for i in range(1, 6)]
lengths = [item[1] for item in top_five]

plt.bar(labels, lengths)
plt.xlabel("Cat Facts")
plt.ylabel("Number of Characters")
plt.title("Five Longest Cat Facts")
plt.tight_layout()

# Save graph to repository
plt.savefig("cat_facts_graph.png")
plt.show()
