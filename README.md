# Project Hypatia: AI-Assisted Research Workflow

## Overview

Project Hypatia is a web-based application designed to guide users through a 10-step scientific research workflow, from initial question formulation to final publication export. Its core purpose is to leverage Artificial Intelligence (via Google's Gemini API) to assist researchers at each stage by generating relevant content, suggesting ideas, and automating parts of the documentation process.

The application combines a JavaScript-based frontend for user interaction with a Python (Flask) backend that handles communication with the Gemini API.

## Key Features

*   **10-Step Guided Research Process**: A structured workflow covering:
    1.  Question Formulation
    2.  Research Explorer (Literature Review)
    3.  Hypothesis Builder
    4.  Methodology Designer
    5.  Data Gatherer (including AI-generated Python simulation code)
    6.  Experiment Runner (simulated Python execution in frontend)
    7.  Data Analyzer (including AI-generated interpretation)
    8.  Conclusion Drawer
    9.  Peer Reviewer (AI-generated mock review and draft response)
    10. Publication Exporter (AI-generated full paper draft)
*   **Real AI Content Generation**: Utilizes Google's Gemini API (via a Python backend) to generate text, data, and code suggestions.
*   **Interactive Workflow**: Users can input their own data (Step 1) and review/edit AI-generated content in subsequent steps.
*   **Data Persistence**: Employs browser `localStorage` to save progress and data across sessions within the same browser.
*   **Python Code Generation**: AI generates Python code for experiment simulation in Step 5.
*   **Simulated Python Execution**: Step 6 provides a frontend simulation of running the generated Python code.
*   **User Authentication**: Simple login/signup system (data stored in `localStorage`).

## File Structure Map

The project is organized with a frontend application and a Python backend:

```
.
├── backend/
│   ├── .env                 # Environment variables (GEMINI_API_KEY) - DO NOT COMMIT
│   ├── .gitignore           # Specifies intentionally untracked files for backend
│   ├── app.py               # Flask application, API endpoint
│   ├── gemini_client.py     # Gemini API interaction logic
│   ├── requirements.txt     # Python dependencies
│   └── venv/                # Python virtual environment (if created here) - DO NOT COMMIT
├── Hyperion/
│   └── project-hypatia-simplified-frontend-updated.zip # Original zip file (for reference)
│   └── ai-service.js        # DEPRECATED: Mock AI service (no longer used by core workflow)
├── workflow/
│   ├── conclusion-drawer.html   # Step 8
│   ├── data-analyzer.html       # Step 7
│   ├── data-gatherer.html       # Step 5
│   ├── experiment-runner.html   # Step 6
│   ├── hypothesis-builder.html  # Step 3
│   ├── methodology-designer.html # Step 4
│   ├── peer-reviewer.html       # Step 9
│   ├── publication-exporter.html # Step 10
│   ├── question-formulation.html # Step 1
│   └── research-explorer.html   # Step 2
├── dashboard.html
├── index.html
├── login.html
├── signup.html
├── LICENSE
└── README.md                    # This file.
```

### Key Components:

*   **`index.html`**: Main frontend entry point.
*   **`login.html`, `signup.html`, `dashboard.html`**: User authentication and navigation.
*   **`workflow/` directory**: HTML files for each of the 10 research workflow steps.
*   **`backend/app.py`**: The Flask application server that provides the `/api/generate` endpoint for AI requests.
*   **`backend/gemini_client.py`**: Contains the Python logic to interact with the Google Gemini API.
*   **`backend/requirements.txt`**: Lists Python dependencies for the backend (Flask, google-generativeai, python-dotenv, Flask-CORS).
*   **`backend/.env`**: Stores the `GEMINI_API_KEY` (must be created manually by the user).
*   **`Hyperion/ai-service.js`**: **Deprecated.** Previously simulated the AI; now replaced by the Python backend.

## Installation and Use Guide

Project Hypatia now consists of a frontend (HTML/JS client-side application) and a Python-based backend for AI capabilities. Both need to be set up correctly for the application to function as intended.

### Prerequisites

*   A modern web browser (e.g., Chrome, Firefox, Edge, Safari).
*   Python 3.7+ installed on your system.
*   Ability to create and manage Python virtual environments.
*   A valid Google Gemini API Key.

### 1. Backend Setup

The backend server handles communication with the Google Gemini API.

1.  **Navigate to Backend Directory:**
    Open your terminal or command prompt and navigate into the `backend/` directory from the project root:
    ```bash
    cd backend
    ```

2.  **Create a Python Virtual Environment:**
    It's highly recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv  # Or python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    Your terminal prompt should change to indicate the active virtual environment.

4.  **Install Dependencies:**
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up Environment Variables (`.env` file):**
    *   In the `backend/` directory, create a file named `.env` (if it doesn't exist or if you need to modify the template).
    *   Add your Google Gemini API key to this file:
        ```env
        GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"
        FLASK_APP="app.py"
        FLASK_DEBUG=1 # Enables debug mode for development
        ```
    *   **Important:** Replace `"YOUR_ACTUAL_GEMINI_API_KEY"` with your real API key.
    *   The `.env` file is listed in `backend/.gitignore`, so your API key will not be committed to version control. **Keep your API key secure.**

6.  **Run the Backend Server:**
    Once the dependencies are installed and the `.env` file is configured, run the Flask development server:
    ```bash
    python app.py
    ```
    You should see output indicating the server is running, typically on `http://localhost:5000/` or `http://0.0.0.0:5000/`.
    The server needs to remain running while you use the frontend application.

### 2. Frontend Setup & Usage

1.  **Open `index.html` in a Web Browser:**
    *   Navigate to the project's **root** directory (the one containing `index.html`, not the `backend/` directory).
    *   Open the `index.html` file in your web browser.

2.  **Ensure Backend is Running:**
    *   For the AI features in the application to work, the Python backend server (set up in the previous section) **must be running** and accessible (typically at `http://localhost:5000`).

3.  **Using the Application:**
    *   **Authentication:** Log in or sign up as before. This data is still stored in `localStorage`.
    *   **Workflow Navigation:** Proceed through the 10-step workflow.
    *   **AI Interaction:** When you click buttons like "Generate AI Suggestions," "Generate Full Hypothesis with AI," etc., the frontend will now make API calls to your local Python backend. The backend then queries the Gemini API and returns the results.
    *   **Editing & Saving:** You can still edit AI-generated content. All data is saved to `localStorage` when you click "Next" to move between steps.

### Key Operational Notes:

*   **Two Components:** Remember you are running two main parts: the Python backend server in your terminal and the HTML/JavaScript frontend in your browser.
*   **API Key Security:** Your Gemini API key is used by the backend. Ensure the `.env` file is secure and not shared or committed.
*   **Error Handling:** If the backend isn't running or if there's an issue with your API key or the Gemini service, the frontend should display an error message (often in an alert). Check the browser's developer console and the backend terminal output for more detailed error information.
*   **CORS:** The backend is configured with `Flask-CORS` to allow requests from the frontend. The default development setting allows all origins, which is fine for local development.

## Data Flow Map for Agentic Processes

The "agentic process" in Project Hypatia now involves communication between the frontend JavaScript, the Python backend server, and the Google Gemini API for AI-driven content generation. `localStorage` remains crucial for passing data between frontend workflow steps.

1.  **User Input & Context Aggregation (Frontend):**
    *   User initiates an AI action (e.g., clicking a "Generate..." button).
    *   JavaScript on the current HTML page gathers:
        *   Direct user input from the page.
        *   Relevant data from previous steps, retrieved from `localStorage`. This forms the **context**.
2.  **Prompt Construction (Frontend):**
    *   Based on the specific task, JavaScript dynamically constructs a detailed **prompt string**, incorporating the aggregated context.
3.  **API Request to Backend (Frontend to Backend):**
    *   The frontend JavaScript uses the `fetch()` API to make an HTTP POST request to the `/api/generate` endpoint on the local Python backend server (typically `http://localhost:5000/api/generate`).
    *   The request body contains the constructed `prompt` in JSON format (e.g., `{"prompt": "your detailed prompt here"}`).
4.  **AI Service Call (Backend to Gemini API):**
    *   The Python Flask backend receives the request.
    *   The `/api/generate` endpoint in `backend/app.py` calls the `generate_text_async()` function in `backend/gemini_client.py`, passing the received prompt.
    *   `gemini_client.py` uses the `google-generativeai` SDK to send the prompt to the configured Google Gemini model.
5.  **Response from Gemini API (Gemini API to Backend):**
    *   The Gemini API processes the prompt and returns the generated text (or an error) to the Python backend.
6.  **API Response to Frontend (Backend to Frontend):**
    *   The Python backend sends a JSON response back to the frontend.
        *   On success: `{"text": "AI-generated content"}`
        *   On error (either from Gemini or within the backend): `{"error": "Error message"}`
7.  **Response Processing & UI Population (Frontend):**
    *   The frontend JavaScript (`fetch` call's `.then()` or `await`) receives and parses the JSON response from the backend.
    *   If an error is present, it's typically displayed in an alert.
    *   If successful, the `text` content is used to populate the relevant form fields or display areas on the current HTML page.
8.  **User Review and Editing (Frontend):**
    *   The user reviews the AI-generated content provided by the Gemini API.
    *   The user can **edit or overwrite** this content.
9.  **Data Persistence for Next Step (Frontend):**
    *   When the user clicks the "Next" button, JavaScript on the current page saves the final state of all relevant form fields (including any user-edited AI-generated content) into `localStorage`.
    *   This data then becomes part of the context for AI generation in subsequent steps.

## Technical Stack

### Frontend
*   **HTML5**: Structure.
*   **CSS3**: Styling, with [Bootstrap 5.3](https://getbootstrap.com/) via CDN.
*   **JavaScript (ES6+)**: Dynamic behavior, workflow logic, `fetch` API calls to the backend, `localStorage`.
*   **Bootstrap 5.3**: CSS framework (CDN).
*   **Plotly.js**: Graphing library (Step 7), via CDN.
*   **Web Storage (`localStorage`)**: Data persistence.

### Backend
*   **Python 3.x**: Language for the backend server.
*   **Flask**: Lightweight web framework for the API.
*   **`google-generativeai`**: Google Python SDK for Gemini API.
*   **`python-dotenv`**: Manages environment variables from `.env`.
*   **`Flask-CORS`**: Handles Cross-Origin Resource Sharing.

### Deprecated Components
*   **`Hyperion/ai-service.js`**: Previously provided mock AI responses; now **deprecated** and replaced by the Python backend.

## Python Execution Simulation (Step 6)

While AI content generation now uses the real Google Gemini API, one key area remains a **simulation within the frontend**:

1.  **Python Code Execution (Step 6 - `experiment-runner.html`)**:
    *   In Step 5 (`data-gatherer.html`), the Gemini API generates Python code.
    *   In Step 6 (`experiment-runner.html`), this code is displayed. However, the application **does not actually execute this Python code**.
    *   The "Run Experiment" functionality is a **JavaScript-based simulation**. It checks the Python code string for patterns and displays mock success/error messages.
    *   The "Attempt AI Fix & Rerun" feature also simulates an AI fix before the mock rerun.
    *   No Python interpreter is used by the frontend for execution.

## Future Enhancements

While Project Hypatia now leverages a real AI backend, future development can enhance its capabilities:

1.  **Real Python Execution Environment:**
    *   Integrate a service (e.g., Pyodide, Skulpt, or a custom sandboxed backend) to execute the AI-generated Python code from Step 6.
    *   Refine AI code generation (Step 5) to use only pre-approved dependencies for such an environment.
2.  **Refined AI Prompt Engineering:**
    *   Continuously improve prompts for the Gemini API for higher quality and more nuanced AI-generated content.
3.  **Backend Database Storage:**
    *   Implement a database for persistent user accounts and project data, enabling multi-device access.
4.  **Enhanced Literature Review (Step 2):**
    *   Integrate with academic search APIs (e.g., Semantic Scholar) for real literature searches and summarization.
5.  **Improved UI/UX:**
    *   Refine error display, data visualization, and overall user experience.
6.  **Collaboration Features & Version Control.**
7.  **Cleanup Deprecated Code:** Remove the unused `Hyperion/ai-service.js`.
