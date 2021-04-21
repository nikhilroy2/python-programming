
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates

templates = read_templates('test.pdf')
result = extract_data('test.pdf', templates=templates)




# st = "Total: 4.00 4,123.00"
# result = st.split()
# result.pop(1)
# print(" ".join(result))