# DAVIET College Chatbot

A Python Flask-based chatbot to answer DAVIET college queries via a simple web chat interface.

---

## How to Run

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <project-folder>
    ```

2. **(Optional) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Activate:
    # Windows (CMD):
    venv\Scripts\activate
    # Windows (PowerShell):
    .\venv\Scripts\Activate.ps1
    # Mac/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app:**
    ```bash
    python app.py
    ```
    The chatbot will be available at [http://localhost:5000](http://localhost:5000).

---

## Running Tests

Make sure your virtual environment is activated and dependencies (including `pytest`) are installed.

Run tests using:

- **Windows CMD:**
    ```bash
    set PYTHONPATH=. && pytest tests/test_bot.py
    ```

- **Windows PowerShell:**
    ```powershell
    $env:PYTHONPATH="." ; pytest tests/test_bot.py
    ```

- **Mac/Linux terminal:**
    ```bash
    PYTHONPATH=. pytest tests/test_bot.py
    ```

This ensures that the `chatbot` package is discoverable by the test runner.

---

## Freezing Dependencies

After installing or updating packages, update `requirements.txt` with:

```bash
pip freeze > requirements.txt
