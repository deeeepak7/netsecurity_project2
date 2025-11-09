NetSecurity Pipeline
====================

NetSecurity is an end‑to‑end machine learning pipeline focused on phishing detection for network security data. The project automates data ingestion, validation, transformation, and model training, while also providing a utility to seed MongoDB with raw phishing records.

Features
--------
- Automated training pipeline orchestrated from `main.py`.
- CSV → JSON conversion and bulk insert helper for MongoDB in `push_data.py`.
- Centralized logging and custom exception handling.
- Modular configs under `networksecurity.entity.config_entity` to keep parameters organized.

Getting Started
---------------
1. **Clone & Install**
   ```bash
   git clone <repo-url>
   cd netsecurity
   python -m venv .venv
   .venv\Scripts\activate
   pip install -e .
   ```

2. **Environment Variables**
   Create a `.env` file at the project root and set:
   ```
   mongo_url=<your MongoDB connection string>
   ```

3. **Seed MongoDB (optional)**
   Update `File_path`, `database`, and `collection` in `push_data.py`, then run:
   ```bash
   python push_data.py
   ```
   This loads the phishing CSV into MongoDB for experimentation.

4. **Run the Training Pipeline**
   ```bash
   python main.py
   ```
   The script executes data ingestion, validation, transformation, and model training sequentially. Logs and artifacts are written to the configured output directories.

Testing the Connection
----------------------
Use `test_push_Data.py` to verify MongoDB connectivity:
```bash
python test_push_Data.py
```
Successful execution prints a confirmation ping message.

Project Structure
-----------------
- `networksecurity/` – Core package housing pipeline components, configs, logging, and exception utilities.
- `main.py` – Entry point for the training workflow.
- `push_data.py` – Utility to load phishing data into MongoDB.
- `test_push_Data.py` – Connectivity smoke test for MongoDB.

Support
-------
Open an issue or reach out to the maintainers for questions or feature requests.
