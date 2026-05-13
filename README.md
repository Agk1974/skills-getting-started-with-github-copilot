# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey Agk1974!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/Agk1974/skills-getting-started-with-github-copilot/issues/1)

---

## Project Overview

This repository contains a small FastAPI application for students at Mergington High School to browse extracurricular activities, sign up for them, and manage participant registrations.

## Running the App

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the server:

   ```bash
   uvicorn src.app:app --reload
   ```

3. Open the app in your browser:

   - Main page: http://localhost:8000/static/index.html
   - API docs: http://localhost:8000/docs

## Tests

The backend includes API tests in `tests/test_app.py` using `pytest` and FastAPI `TestClient`.

Run the tests with:

```bash
pytest -q
```

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

