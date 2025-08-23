# JuicyMango


This is primarily an exercise in how different LLMs handle code migration.  This code was written in ~2010, primarily in Python2 by the contributors listed below (myself included).  This repository contains the first pass using Gemini 2.5.  There are bugs, feel free to contribute or whatever.

JuicyMango is an open-source intelligence (OSINT) analysis engine designed to collect and analyze data from various sources, including IRC, Twitter, Facebook, RSS feeds, and Gmail. It provides a web-based interface for interactive analysis and visualization of collected intelligence.

## Features

*   **Modular Data Collection:** Gathers data from:
    *   IRC channels
    *   Twitter (via its API)
    *   Facebook (via its Graph API)
    *   RSS feeds
    *   Gmail messages (via IMAP)
*   **Web-based Interface:** Provides a graphical user interface for:
    *   Viewing collected events and alerts
    *   Managing keywords and thresholds
    *   User authentication and password management
*   **SQLite3 Database Integration:** Stores collected data, keywords, alerts, and user information in SQLite3 databases.
*   **Configurable Output:** Supports output to console, file, or SQLite3 database.

## Installation

To set up JuicyMango, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/gunnoej5/juicymango.git
    cd juicymango
    ```

2.  **Create and Activate a Virtual Environment:**
    It is highly recommended to use a Python virtual environment to manage project dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *If `python3 -m venv venv` fails with an error about `ensurepip` or `python3-venv` not being available, you may need to install it first (e.g., `sudo apt install python3.12-venv` on Debian/Ubuntu systems) and then retry creating the virtual environment.*

3.  **Install Dependencies:**
    Install the required Python libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the Application:**
    Copy the sample configuration file and edit it to suit your needs:
    ```bash
    cp config.sample config.ini
    ```
    Open `config.ini` and review the settings, especially:
    *   `WEB_VIEW_IP` and `WEB_VIEW_PORT` for the web interface.
    *   `COOKIE_SECRET`: **IMPORTANT:** Change `your_secret_key_here` to a strong, randomly generated secret for production environments.
    *   Module-specific settings (e.g., `MOD_IRC`, `MOD_TWITTER`, `MOD_FACEBOOK`, `MOD_RSS`, `MOD_GMAIL` and their respective configurations).
    *   `OUTPUT_SQLITE3_DB_PATH` for your database file path.

5.  **Set Admin Password:**
    The initial admin password is a placeholder. You should generate a strong bcrypt hash for your admin password and update the `INSERT` statement in juicymango.py (around line 82) before running the application in production.

## Usage

To run JuicyMango, execute the main script:

```bash
python3 juicymango.py
```

Once running, you can access the web interface in your browser at the configured `WEB_VIEW_IP` and `WEB_VIEW_PORT` (e.g., `http://127.0.0.1:8080`).

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPLv3). See the `LICENSE` file for details.

## Credits

Originally written by: Chris Centore, Steve Swann, Jason Gunnoe
