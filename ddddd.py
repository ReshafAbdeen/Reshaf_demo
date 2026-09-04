import csv


class DataFilter:

    def __init__(self, data):
        self.data = data

    def filter_by_key(self, key, value):
        return [row for row in self.data if row.get(key) == value]

    def select_columns(self, columns):
        return [{k: row[k] for k in columns if k in row} for row in self.data]

    def export_csv(self, filename):
        if not self.data:
            return
        keys = self.data[0].keys()
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.data)
        print(f"Exported to {filename}")


dataset = [
    {"name": "Alice", "role": "Dev", "age": "28"},
    {"name": "Bob", "role": "Design", "age": "34"},
    {"name": "Charlie", "role": "Dev", "age": "22"},
]

df = DataFilter(dataset)
devs = df.filter_by_key("role", "Dev")
print(f"Developers: {devs}")
print(f"Names only: {df.select_columns(['name'])}")
df.export_csv("devs.csv")