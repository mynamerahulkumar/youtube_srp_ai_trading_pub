# Copilot/ChatGPT Prompt: Generate a Delta Exchange India BTCUSD Order Placement Project

You are an expert Python developer, algorithmic trading engineer, and API integration specialist.

Create a **beginner-friendly** project that demonstrates how to place an order on **Delta Exchange India** using the **official Python REST Client**.

The project is intended for educational purposes so students can understand how to connect to Delta Exchange and place their first trade.

---

## Project Requirements

Create the following files:

```
delta_order.py
requirements.txt
setup.md
README.md
```

Do not create multiple Python files. Everything should be inside **delta_order.py**.

---

# Python Version

The project should support:

* Python 3.10
* Python 3.11
* Python 3.12

Avoid using Python 3.13 or newer features.

---

# Requirements

Use the official Delta Exchange Python SDK.

requirements.txt should include only the required lightweight dependencies.

Example:

```
delta-rest-client
requests
```

Do not include unnecessary libraries.

---

# Python Script

Create a clean and well-commented Python program.

The script should contain:

## Configuration Section

```python
API_KEY

API_SECRET

BASE_URL

SYMBOL

SIDE

SIZE
```

These should be easy for beginners to modify.

---

## Connect to Delta Exchange

Use the official REST client.

---

## Fetch Product Information

Retrieve the BTCUSD product information.

Display:

* Product ID
* Mark Price

---

## Place Order

Submit a Market Order.

The side should be configurable:

```
buy

sell
```

The quantity should also be configurable.

---

## Console Output

Print beginner-friendly messages such as

```
Connecting...

Fetching Product...

Current Price...

Placing Order...

Order Successful
```

---

## Error Handling

Wrap everything inside try/except.

Print meaningful error messages.

Do not display huge stack traces.

---

## Code Quality

The code should include

* comments
* docstrings
* clean variable names
* readable formatting
* PEP8 style

---

# setup.md

Generate a complete setup guide.

Include:

## Windows

* Create virtual environment
* Activate virtual environment
* Install requirements
* Run the script

## macOS

* Create virtual environment
* Activate virtual environment
* Install requirements
* Run the script

## Linux

* Create virtual environment
* Activate virtual environment
* Install requirements
* Run the script

Explain every command.

---

# README.md

Create a professional README.

Include

* Project Overview
* Features
* Requirements
* Installation
* Configuration
* Running the Project
* Example Output
* Troubleshooting
* Disclaimer

Mention that this project is intended for educational purposes.

---

# Best Practices

Do not hardcode credentials.

Use variables for configuration.

Write beginner-friendly code.

Avoid unnecessary complexity.

Keep the code under approximately 150 lines.

---

# Official References
https://docs.delta.exchange/#place-order

Use the latest official Delta Exchange documentation and official Python REST Client as the implementation reference.

Do not use deprecated endpoints.

Follow the official API naming conventions.

---

# Expected Output

Generate:

* `delta_order.py`
* `requirements.txt`
* `setup.md`
* `README.md`

All files should be complete, production-quality, well-documented, and ready to run after the user adds their API Key and API Secret.
