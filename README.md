# DAVIET College Chatbot

A Python Flask-based chatbot to answer DAVIET college queries via a simple web chat interface.

---

## How to Run

1. **Clone the repository:**
    git clone <your-repo-url>
    cd <project-folder>

2. **(Optional) Create and activate a virtual environment:**
    python -m venv venv
    # Activate:
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate

3. **Install dependencies:**
    pip install -r requirements.txt

4. **Run the app:**
    python app.py
    
    The chatbot will be available at [http://localhost:5000](http://localhost:5000)

---

## Freezing Dependencies

After installing packages, update `requirements.txt` with:
```bash
pip freeze > requirements.txt
