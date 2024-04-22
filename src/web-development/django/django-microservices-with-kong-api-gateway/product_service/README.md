# Product Service

This microservice handles product-related functionalities such as product catalog management, product search, and product details retrieval.

## Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```

2. Activate the virtual environment:
   ```bash
   source myenv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `/products/`: Create a new product or retrieve a list of products.
- `/products/{id}/`: Retrieve, update, or delete a specific product.

For more details on the API endpoints and request/response formats, please refer to the API documentation.