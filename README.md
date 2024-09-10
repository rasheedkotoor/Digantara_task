# Scheduler Microservice

## Overview
The Scheduler Microservice is a Django-based application designed to facilitate job scheduling and management. It provides a flexible API for creating, listing, and retrieving jobs, and includes basic logic for scheduling tasks.

## Features

1. **Job Scheduling**: Allows the scheduling of customizable jobs with flexible configuration.
   - **Note**: Includes a proof-of-concept (POC) logic for job scheduling and execution.

2. **API Endpoints**:
   - **GET /jobs**: List all available jobs.
   - **GET /jobs/:id**: Retrieve details of a specific job by ID.
   - **POST /jobs**: Create new jobs with input validation.

3. **Database Integration**: Stores job-related information such as job name, last run timestamp, next run timestamp, and other details.

4. **Customization**: Each job can be customized with specific attributes and scheduling intervals.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Django 4.0 or higher
- Celery
- PostgreSQL (or your preferred database)
- Redis (for Celery)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/scheduler-microservice.git
   cd scheduler-microservice

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv

3. Activate the Virtual Environment

- Windows:

  ```bash
  venv\Scripts\activate

- macOS/Linux:

  ```bash
  source venv/bin/activate

4. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

5. Configure the Database

    Update the DATABASES settings in scheduler/settings.py to match your database configuration.

6. Apply Migrations

    ```bash
    python manage.py migrate
    ```

7. Run the Development Server

    ```bash
    python manage.py runserver
    ```

8. Run Celery Worker

    Open a new terminal and start the Celery worker:

    ```bash
    celery -A scheduler worker --loglevel=info
    ```

## API Documentation

The API documentation is generated using the drf-yasg library. It can be accessed at:

- Swagger UI: /swagger/
- ReDoc: /redoc/

## Scaling and Deployment

To achieve scalability for handling increased load:

1. Horizontal Scaling: Deploy multiple instances of the service across different servers or containers.
2. Load Balancing: Use a load balancer to distribute traffic evenly among instances.
3. Database Optimization: Ensure the database is optimized for read and write operations.
4. Caching: Implement caching mechanisms to reduce load on the database.
5. Monitoring: Set up monitoring and alerting to track performance and issues.

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push the branch (git push origin feature/your-feature).
5. Open a pull request.

