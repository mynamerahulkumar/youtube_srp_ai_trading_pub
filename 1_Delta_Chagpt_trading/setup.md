# Setup Guide

This guide explains how to set up the project on **Windows** and **macOS/Linux** using a Python virtual environment.

---

# Prerequisites

* Python **3.10 or newer**
* Internet connection
* Delta Exchange API Key
* Delta Exchange API Secret

Verify Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

# Project Structure

```
project/
│
├── delta_order.py
├── requirements.txt
└── setup.md
```

---

# Windows Setup

## Step 1: Open Command Prompt or PowerShell

Navigate to your project directory.

```bash
cd path\to\project
```

Example:

```bash
cd C:\Users\Rahul\Desktop\delta_bot
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3: Activate Virtual Environment

### Command Prompt

```bash
venv\Scripts\activate
```

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

You should now see:

```
(venv)
```

at the beginning of your terminal.

---

## Step 4: Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6: Configure API Credentials

Open **delta_order.py**

Replace:

```python
API_KEY = "YOUR_API_KEY"

API_SECRET = "YOUR_API_SECRET"
```

with your own credentials.

---

## Step 7: Run the Program

```bash
python delta_order.py
```

---

# macOS / Linux Setup

## Step 1: Open Terminal

Navigate to your project folder.

```bash
cd /path/to/project
```

Example:

```bash
cd ~/Desktop/delta_bot
```

---

## Step 2: Create Virtual Environment

```bash
python3 -m venv venv
```

---

## Step 3: Activate Virtual Environment

```bash
source venv/bin/activate
```

You should now see:

```
(venv)
```

---

## Step 4: Upgrade pip

```bash
python -m pip install --upgrade pip
```

or

```bash
python3 -m pip install --upgrade pip
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6: Configure API Credentials

Edit **delta_order.py**

Replace:

```python
API_KEY = "YOUR_API_KEY"

API_SECRET = "YOUR_API_SECRET"
```

with your own API credentials.

---

## Step 7: Run the Program

```bash
python delta_order.py
```

If `python` is unavailable:

```bash
python3 delta_order.py
```

---

# Deactivate Virtual Environment

When finished:

```bash
deactivate
```

---

# Reopen the Project Later

## Windows

```bash
cd path\to\project

venv\Scripts\activate

python delta_order.py
```

---

## macOS / Linux

```bash
cd /path/to/project

source venv/bin/activate

python3 delta_order.py
```

---

# requirements.txt

```text
delta-rest-client
```

Install dependencies anytime with:

```bash
pip install -r requirements.txt
```

---

# Common Errors

### ModuleNotFoundError

Install dependencies again:

```bash
pip install -r requirements.txt
```

---

### Virtual Environment Not Activated

Activate the virtual environment before running:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

---

### Invalid API Key or Secret

Verify that:

* Your API Key is correct.
* Your API Secret is correct.
* Trading permissions are enabled for the API key.
* You are using the correct Delta Exchange India API endpoint.

---

# You're Ready!

After completing the setup, you can place an order by running:

```bash
python delta_order.py
```

The script will connect to Delta Exchange India and submit the configured order using your API credentials.
