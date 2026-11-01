import json

# Example 1: JSON starting with an object
json_string_object = """
{
    "id": 1,
    "name": "Product A",
    "price": 29.99
}
"""

print("--- Example 1: JSON Object ---")
# The JSON converter interprets the top-level '{' as a Python dictionary.
data_object = json.loads(json_string_object)
print(f"Parsed type: {type(data_object)}")
print(f"Parsed data: {data_object}\n")

# Example 2: JSON starting with an array
json_string_array = """
[
    {"id": 101, "item": "Apple"},
    {"id": 102, "item": "Banana"}
]
"""

print("--- Example 2: JSON Array ---")
# The JSON converter interprets the top-level '[' as a Python list.
data_array = json.loads(json_string_array)
print(f"Parsed type: {type(data_array)}")
print(f"Parsed data: {data_array}\n")

# Example 3: JSON object containing an array of objects
json_string_nested = """
{
    "storeName": "My Store",
    "products": [
        {"productId": "P001", "productName": "Laptop", "stock": 10},
        {"productId": "P002", "productName": "Mouse", "stock": 50}
    ],
    "isOpen": true
}
"""

print("--- Example 3: Nested JSON Structure ---")
# The converter first interprets the top-level '{' as a Python dictionary.
# It then recursively interprets nested structures, such as the 'products' array as a list.
data_nested = json.loads(json_string_nested)
print(f"Parsed type: {type(data_nested)}")
print(f"Parsed data: {data_nested}")
print(f"Type of 'products' field: {type(data_nested['products'])}")
print(f"Type of first product in 'products': {type(data_nested['products'][0])}\n")

print("--- Conclusion ---")
print("JSON converters infer the initial native data type (e.g., Python dict or list)")
print("based on the very first character of the JSON string ('{' for object, '[' for array).")
print("This 'first object translation' dictates the top-level structure of the parsed data.")
