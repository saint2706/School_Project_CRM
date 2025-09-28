# Project TODO List

This file outlines the remaining tasks for the School Project CRM refactoring.

## Phase 2: Feature Implementation

-   **Develop Core CRM Features:**
    -   [ ] Implement full CRUD (Create, Read, Update, Delete) functionality for "Customers".
    -   [ ] Implement full CRUD functionality for "Leads".
    -   [ ] Implement the logic for converting a "Lead" into a "Customer".
    -   [ ] Use pagination to display long lists of customers and leads efficiently.

-   **Implement Manager-Specific Functionality:**
    -   [ ] Create administrative views for managing salesmen (add, update, fire).
    -   [ ] Implement functionality for managers to view sales data for all salesmen.
    -   [ ] Protect manager routes using RBAC decorators.

-   **Data Analytics and Reporting:**
    -   [ ] Re-implement the sales analytics features.
    -   [ ] Generate charts on the backend or use a frontend charting library (e.g., Chart.js) to display data.
    -   [ ] Develop advanced reporting features as requested.

## Phase 3: Frontend and User Interface

-   **Build a Responsive UI:**
    -   [ ] Create a main dashboard page.
    -   [ ] Design and implement templates for all CRM features (CRUD pages, lists, etc.).
    -   [ ] Ensure all pages are fully responsive using the Bootstrap grid system.

## Phase 4: Testing, CI/CD, and Documentation

-   **Write More Tests:**
    -   [ ] Add unit tests for the `Customer` and `Lead` models.
    -   [ ] Add integration tests for all CRUD operations.
    -   [ ] Add tests for manager-specific functionality.

-   **Set Up CI/CD Pipeline:**
    -   [ ] Create a GitHub Actions workflow to automatically install dependencies and run the test suite on every push.
    -   [ ] (Optional) Add a deployment step to the CI/CD pipeline.

-   **Update Documentation:**
    -   [ ] Thoroughly update the `README.md` file with detailed instructions on how to set up the development environment, configure the database, and run the new web application.

## Phase 5: Advanced Features & Security

-   **Enhance Performance and Security:**
    -   [ ] Implement caching for frequently accessed data.
    -   [ ] Set up asynchronous tasks for long-running processes (e.g., sending email notifications).
    -   [ ] Implement Two-Factor Authentication (2FA).
    -   [ ] Encrypt sensitive data in the database.