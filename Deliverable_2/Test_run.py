from deliverable_2 import *

# Instantiate the URLValidator class
validator = URLValidator()

# Define user prompt and URL
user_prompt = "Spine Surgery"
url_to_check = "https://pubmed.ncbi.nlm.nih.gov/8950879/"

# Run the validation
result = validator.rate_url_validity(user_prompt, url_to_check)

# Print the results
import json
print(json.dumps(result, indent=2))