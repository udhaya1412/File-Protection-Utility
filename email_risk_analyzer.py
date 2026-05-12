# Suspicious keywords list
suspicious_words = [
    "urgent",
    "immediately",
    "password",
    "bank",
    "click here",
    "verify",
    "account suspended",
    "otp"
]

# Sample email content
email_content = """
URGENT! Your bank account is suspended.
Click here: https://fakebank.com
Enter your password immediately.
"""

# Convert email to lowercase
email_lower = email_content.lower()

# Risk score
risk_score = 0

# Check suspicious keywords
for word in suspicious_words:
    if word in email_lower:
        print(f"Suspicious keyword detected: {word}")
        risk_score += 1

# Check suspicious links
if "http://" in email_lower or "https://" in email_lower:
    print("Suspicious link detected!")
    risk_score += 1

# Final analysis result
print("\n--- Analysis Result ---")

if risk_score == 0:
    print("Email looks SAFE")
elif risk_score <= 2:
    print("Email is MODERATELY SUSPICIOUS")
else:
    print("WARNING: Email is HIGHLY SUSPICIOUS")