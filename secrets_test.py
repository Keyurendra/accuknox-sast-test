# 🚨 Intentionally vulnerable file for testing Secret Scanning
# DO NOT USE THESE KEYS IN PRODUCTION

# AWS - AKIA + exactly 20 characters
AWS_ACCESS_KEY_ID = "AKIAQ7XVQH3MFJYV8KZNABCDEF"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY"

# GitHub PAT - ghp_ + exactly 36 characters
GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890"

# Slack - xoxb- + 12 digits + 12 digits + 24 alphanumeric
SLACK_TOKEN = "xoxb-123456789012-123456789012-abcdefghijklmnopqrstuvwx"

# Stripe - sk_live_ + 24 chars
STRIPE_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"

print("This file contains fake hardcoded secrets for testing only.")
