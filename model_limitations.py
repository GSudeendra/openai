#Boie is a real company, the product name is not real.
### Model Limitations: Hallucinations
from auth import get_completion

prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
response = get_completion(prompt)
print(response)