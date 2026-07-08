# Author = Kiran
# Date = 7th July, 2026
"""
WAF to convert the USD into pkr
"""

def usd_to_pkr(usd_amount, conversion_rate=280):
    return usd_amount * conversion_rate

# Example usage
usd_amount = 100
pkr_amount = usd_to_pkr(usd_amount)
print(f"{usd_amount} USD is equal to {pkr_amount} PKR")  # Output: 100 USD is equal to 28000 PKR