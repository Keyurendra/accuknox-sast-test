# 🚨 Test file for Verified vs Unverified Secrets
# Using Stripe TEST keys (safe for testing)

# Stripe Test Secret Key - TruffleHog can verify this
STRIPE_TEST_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# Fake GitHub Token - Unverified (fake/expired)
GITHUB_FAKE = "ghp_aBcD1234EfGh5678IjKl9012MnOp3456QrSt"

# AWS Fake - Unverified
AWS_FAKE = "AKIA55PLKVCCO3DK3UVB"

print("Testing verified vs unverified secrets")
