# 🚨 Intentionally vulnerable file for testing Secret Scanning
# DO NOT USE THESE KEYS IN PRODUCTION

# AWS Access Key - AKIA + exactly 20 characters (A-Z and 0-9)
AWS_ACCESS_KEY_ID = "AKIAQ7XVQH3MFJYV8KZNABCD"  # 20 chars after AKIA

# AWS Secret Key - 40 characters of high entropy
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY"  # 40 chars

# GitHub PAT - ghp_ + exactly 36 characters
GITHUB_TOKEN = "ghp_aBcD1234EfGh5678IjKl9012MnOp3456QrSt"

# Slack Token - xoxb- + 12 digits + 12 digits + 24 alphanumeric
SLACK_TOKEN = "xoxb-123456789012-123456789012-abcdefghijklmnopqrstuvwx"

# Stripe - sk_live_ + 24 chars
STRIPE_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"

# API Key with high entropy
API_KEY = "f8b3c7a9d2e1f4b6c8a0e3d5f7b9c2a4e6d8f0b2c4a6e8d0f2b4c6a8e0d2f4b6"

print("This file contains fake hardcoded secrets for testing only.")
