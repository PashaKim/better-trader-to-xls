import csv
import re

# Open a cfg file
with open('item_defaults.cfg', 'r') as file:
    cfg_text = file.read() # str

# get text by lines
list_of_lines = cfg_text.splitlines()

# get index of unused lines
index_after_remove_text = None
index_before_remove_text = None
for index, line in enumerate(list_of_lines):
    if line == '#Better Trader#':
        index_after_remove_text = index  # 27
    elif line == '#EpicLoot#':
        index_before_remove_text = index  # 226


# remove unused text before "#Better Trader#"
data_list = list_of_lines[(index_after_remove_text + 1):(index_before_remove_text - 1)]  # [28:225]

# from text line to {"name": "Amber"}
def str_line_to_dicts(line:str) -> dict:
    return {
        "Name": re.search(r'(\b[A-z]*:)', line).group(),
        "Stack": int(re.findall(r'Stack = (\d*)', line)[0]),
        "Price": int(re.findall(r'Price = (\d*)', line)[0]),
        "SellPrice": int(re.findall(r'SellPrice = (\d*)', line)[0]),
        "Tradeable": re.findall(r'Tradeable = (true|false)', line)[0],
        "IgnoreWaitForDiscovery": re.findall(r'IgnoreWaitForDiscovery = (true|false)', line)[0],
        "Sellable": re.findall(r'Sellable = (true|false)', line)[0],
    }

data_dicts_list = [str_line_to_dicts(line) for line in data_list]

# Create CSV
with open('NEW_item_defaults.csv', 'w') as csvfile:
    csv_columns = ['Name', 'Stack', 'Price', 'SellPrice', 'Tradeable', 'IgnoreWaitForDiscovery', 'Sellable']
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in data_dicts_list:
        writer.writerow(data)

print("*"*8)
print("Cerated NEW_item_defaults.csv")
print("*"*8)