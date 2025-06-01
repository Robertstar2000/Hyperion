# Project Hypatia: AI-Assisted Research Workflow

## Overview

Project Hypatia is a web-based application designed to guide users through a 10-step scientific research workflow, from initial question formulation to final publication export. Its core purpose is to demonstrate how Artificial Intelligence can assist researchers at each stage by generating relevant content, suggesting ideas, and automating parts of the documentation process.

The application simulates the research journey, providing a structured path and leveraging a mock AI service to populate fields, offer suggestions, and even generate draft sections of an academic paper.

## Key Features

*   **10-Step Guided Research Process**: A structured workflow covering:
    1.  Question Formulation
    2.  Research Explorer (Literature Review)
    3.  Hypothesis Builder
    4.  Methodology Designer
    5.  Data Gatherer (including AI-generated Python simulation code)
    6.  Experiment Runner (mock Python execution)
    7.  Data Analyzer (including AI-generated interpretation)
    8.  Conclusion Drawer
    9.  Peer Reviewer (AI-generated mock review and draft response)
    10. Publication Exporter (AI-generated full paper draft)
*   **AI Content Generation**: At each step, a mock AI assistant helps generate relevant text, data, or code.
    *   Examples: Keywords, research domain, hypothesis statements, methodology details, Python code for experiment simulation, data interpretation, conclusion summaries, peer review feedback, and full academic paper sections.
*   **Interactive Workflow**: Users can input their own data in Step 1, and review and edit AI-generated content in subsequent steps.
*   **Data Persistence**: Utilizes browser `localStorage` to save progress and data across sessions within the same browser.
*   **Mock Python Environment**: Simulates Python code generation (Step 5) and execution (Step 6), including a mock error/fix cycle.
*   **Final Paper Generation**: Culminates in an AI-generated draft of a standard academic paper based on all data collected throughout the workflow.
*   **User Authentication**: Simple login/signup system (data also stored in `localStorage`).

## File Structure Map

The project is organized as follows:

```
.
├── Hyperion/
│   └── ai-service.js        # Mock AI service for generating text content.
│   └── project-hypatia-simplified-frontend-updated.zip # Original zip file (likely for reference)
├── workflow/
│   ├── conclusion-drawer.html   # Step 8: Draw conclusions.
│   ├── data-analyzer.html       # Step 7: Analyze experiment data.
│   ├── data-gatherer.html       # Step 5: Gather data, AI generates Python simulation code.
│   ├── experiment-runner.html   # Step 6: Mock Python code execution.
│   ├── hypothesis-builder.html  # Step 3: Formulate hypothesis.
│   ├── methodology-designer.html # Step 4: Design experimental methodology.
│   ├── peer-reviewer.html       # Step 9: Get AI-generated peer review feedback.
│   ├── publication-exporter.html # Step 10: Export AI-generated academic paper.
│   ├── question-formulation.html # Step 1: Define research question.
│   └── research-explorer.html   # Step 2: Explore existing research (literature review).
├── dashboard.html               # User dashboard page (post-login).
├── index.html                   # Main landing page, redirects to login or dashboard.
├── login.html                   # User login page.
├── signup.html                  # User signup page.
├── LICENSE                      # Project license file.
└── README.md                    # This file.
```

### Key Components:

*   **`index.html`**: The main entry point for the application. It typically handles routing to the login page or the dashboard if the user is already authenticated.
*   **`login.html`, `signup.html`, `dashboard.html`**: Standard pages for user authentication and navigating to the research workflow.
*   **`workflow/` directory**: Contains the HTML files for each of the 10 steps in the research process. Each file is a self-contained page for that specific stage.
*   **`Hyperion/ai-service.js`**: This crucial JavaScript file simulates the backend AI model. It contains the `generateAiText` function that takes prompts (constructed by the logic in each workflow HTML file) and returns predefined, mock AI-generated text responses. All AI capabilities in this project are routed through this mock service.
*   **HTML Files (`*.html`)**: Standard HTML structure, incorporating Bootstrap for styling and custom JavaScript within `<script>` tags for page-specific logic, AI interaction, `localStorage` management, and navigation.

## Installation and Use Guide

### Installation

Project Hypatia is a client-side web application and does not require a complex installation process or backend server.

1.  **Clone or Download the Repository:**
    *   Obtain the project files by cloning the GitHub repository or downloading it as a ZIP file and extracting it.
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    cd <project_directory>   # Replace <project_directory> with the folder name
    ```
2.  **Open in a Web Browser:**
    *   Navigate to the project's root directory.
    *   Open the `index.html` file in a modern web browser (e.g., Chrome, Firefox, Edge, Safari) that supports HTML5, CSS3, modern JavaScript (ES6+), and Web Storage (`localStorage`).
    *   No build steps or dependencies installations are required to run the basic frontend. The application uses Bootstrap via a CDN, and Plotly.js (for Step 7) is also loaded via a CDN, so an internet connection is recommended for these libraries to load correctly.

### Use Guide / Operating Instructions

1.  **Authentication:**
    *   On first visit, you'll be directed to `login.html`.
    *   If you don't have an account, click the link to navigate to `signup.html` to create one. User credentials (email and password) are stored in `localStorage` for demonstration purposes.
    *   Upon successful login/signup, you'll be redirected to `dashboard.html`.

2.  **Starting a New Workflow:**
    *   From the dashboard, you can typically start or continue a research project. (The current dashboard is basic; navigation to Step 1, `workflow/question-formulation.html`, is the primary path).

3.  **Navigating the 10-Step Workflow:**
    *   The application guides you through 10 distinct steps. Each step is represented by an HTML page in the `workflow/` directory.
    *   **Step 1: Question Formulation**: Enter your "Experiment Title" and "Research Question". Click "Generate AI Suggestions" to have the mock AI populate "Keywords" and "Research Domain". You can edit these. Click "Next" to save and proceed.
    *   **Step 2: Research Explorer**: This step is primarily for user input regarding literature review.
    *   **Step 3: Hypothesis Builder**: Click "Generate Full Hypothesis with AI". The AI will use data from Steps 1 & 2 to generate hypothesis components. Edit as needed.
    *   **Step 4: Methodology Designer**: Click "Generate Complete Methodology". The AI uses prior data to suggest methodology details.
    *   **Step 5: Data Gatherer**: Click "Generate AI Suggestions for This Step". The AI suggests data source types, formats, generates mock "Available Datasets", and Python code for simulating your experiment.
    *   **Step 6: Experiment Runner**: The Python code from Step 5 is displayed. Click "Run Experiment" for a simulated execution (including a mock error/fix cycle).
    *   **Step 7: Data Analyzer**: Click "Generate AI Analysis & Interpretation". The AI suggests chart/test parameters and generates a textual interpretation of Step 6's outcome.
    *   **Step 8: Conclusion Drawer**: Click "Generate Complete Conclusion". The AI determines hypothesis support and generates conclusion text.
    *   **Step 9: Peer Reviewer**: Click "Generate AI Peer Review & Draft Response". The AI generates mock peer review comments and drafts a response.
    *   **Step 10: Publication Exporter**: Click "Generate Full Paper with AI". The AI drafts an academic paper based on all prior data.

4.  **AI Interaction:**
    *   Most steps feature a button that explicitly calls the (mock) AI to generate content.
    *   AI suggestions are drafts. **Users can and should edit AI-generated content.**

5.  **Data Persistence:**
    *   All data is saved in the browser's `localStorage`. Progress is saved per browser. Clearing storage erases work.
    *   No backend database is used.

6.  **Mock Nature:**
    *   The AI (`Hyperion/ai-service.js`) is a simulation, returning predefined text.
    *   Python code execution (Step 6) is also a frontend simulation.

## Data Flow Map for Agentic Processes

The "agentic process" in Project Hypatia refers to how the application uses AI (currently mocked) to generate content. Data flow is orchestrated via JavaScript and `localStorage`.

1.  **User Input & Context Aggregation:**
    *   User triggers AI action (button click).
    *   JS retrieves current user input and prior step data from `localStorage` (this is the **context**).
2.  **Prompt Construction:**
    *   JS dynamically creates a detailed **prompt string** including the context.
3.  **AI Service Call:**
    *   Prompt goes to `generateAiText()` in `Hyperion/ai-service.js` (mock service).
    *   Service returns a predefined text response based on prompt keywords.
4.  **Response Processing & UI Population:**
    *   JS receives the mock AI response.
    *   Response populates form fields or display areas.
5.  **User Review and Editing:**
    *   User reviews and **can edit/overwrite** AI content.
6.  **Data Persistence for Next Step:**
    *   On "Next", JS saves final field states (including edits) to `localStorage`.
    *   This data informs future AI generation.

### Example Data Flow Snippets:

*   **Step 1 -> Step 3:**
    1.  **Step 1**: User inputs title/question. AI suggests keywords/domain. Data saved to `localStorage`.
    2.  **Step 3**: AI uses Step 1 data from `localStorage` to generate hypothesis components.
*   **Step 5 -> Step 6 -> Step 7:**
    1.  **Step 5**: AI generates Python code (`generatedPythonCode`), saved to `localStorage`.
    2.  **Step 6**: Code loaded. Mock execution. Output/error (`experimentRunOutput`/`Error`) saved. `actualGeneratedPythonCode` (possibly "fixed") also saved.
    3.  **Step 7**: AI uses code, output/error, and hypothesis from `localStorage` for `aiDataInterpretation`.
*   **Step 9 -> Step 10:**
    1.  **Step 9**: AI generates mock peer review (`aiPeerReviewData`) and draft response, saved to `localStorage`.
    2.  **Step 10**: AI uses all prior data from `localStorage` (Steps 1-9) to draft each section of the final paper.

## Technical Stack and Mocking

### Technical Stack

*   **HTML5**: Structure.
*   **CSS3**: Styling, with [Bootstrap 5.3](https://getbootstrap.com/) via CDN.
*   **JavaScript (ES6+)**: Dynamic behavior, workflow logic, AI calls, `localStorage`. (Embedded or in linked `.js` files).
*   **Plotly.js**: Graphing library (Step 7), via CDN.
*   **Web Storage (`localStorage`)**: Data persistence.

No backend technologies or databases are currently used.

### AI and Python Execution Mocking

Key functionalities are **mocked**:

1.  **AI Service (`Hyperion/ai-service.js`)**:
    *   **No connection to a real LLM.**
    *   `generateAiText(prompt)` simulates AI by returning predefined text based on prompt keywords.
    *   Allows demonstration without real AI integration complexities or costs.
2.  **Python Code Execution (Step 6)**:
    *   **Does not actually execute Python code.**
    *   JavaScript simulates execution by checking the AI-generated Python string for patterns and displaying mock success/error messages.
    *   No Python interpreter is used.

## Future Enhancements

While Project Hypatia is a conceptual demo, future development could include:

1.  **Real AI Integration:** Connect to actual LLM APIs (e.g., Google's Gemini, OpenAI's GPT models).
2.  **Real Python Execution Environment:** Use Pyodide, Skulpt, or a backend to run Python code, with AI generating code for specific, pre-installed libraries.
3.  **Backend Database Storage:** For multi-device access and robust data storage.
4.  **Enhanced Literature Review (Step 2):** Integrate with academic search APIs.
5.  **Improved UI/UX:** Refine interface, add richer editing and visualization.
6.  **Collaboration Features.**
7.  **Version Control for Research Steps.**
8.  **More Sophisticated Prompt Engineering** for real AI models.
