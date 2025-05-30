# Project Hypatia

Project Hypatia is a prototype for an AI-assisted scientific discovery platform. It allows users to manage and step through simulated scientific experiments.

## Local Setup and Usage

To run this application locally:

1.  Clone or download this repository.
2.  Open the `index.html` file in your web browser.

That's it! There are no build steps or server-side dependencies for this version of the application.

## Application Overview

*   **Authentication**: The application uses `localStorage` in your browser to simulate user login. You can sign up and log in using any email/password combination.
*   **Dashboard (`dashboard.html`)**: After logging in, you'll be taken to the dashboard where you can see and manage your experiments.
*   **Experiments**: You can create new experiments or continue existing ones. Each experiment progresses through several stages.
*   **Workflow Pages**: The different stages of an experiment (e.g., Question Formulation, Methodology Design, Data Analysis) are represented by individual HTML pages located in the `workflow/` directory.

## Key Files

*   `index.html`: The main landing page, leading to login or signup.
*   `login.html`: User login page.
*   `signup.html`: User registration page.
*   `dashboard.html`: Main dashboard to view and manage experiments.
*   `workflow/`: This directory contains HTML files for each step of the scientific workflow.

## Note

This is a frontend-only application. All data (user authentication, experiment details) is stored locally in your browser's `localStorage` and will persist between sessions on the same browser. No backend or database is connected in this version.
