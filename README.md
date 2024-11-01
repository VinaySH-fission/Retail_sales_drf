# Retail_sales_drf

# Django Retail Sales API

## Project Description
The Django Retail Sales API provides a RESTful service for accessing and managing aggregated sales data from a PostgreSQL database using Django and Django Rest Framework (DRF). It includes a custom management command to sync sales data from a PostgreSQL view into Django's model.

## Installation

### Prerequisites
- Python 3.8 or newer
- pip and virtualenv
- PostgreSQL

### Setup
1. Clone the repository:
   ```
   git clone [your-repository-url]
   ```
2. Navigate to the project directory:
   ```
   cd django-retail-sales
   ```
3. Create a virtual environment:
   ```
   python -m virtualenv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Configure the environment variables by creating an `.env` file based on the provided template in the Environment Setup section below.

### Database Setup
Run the following commands to prepare your database:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Environment Setup
Ensure you have a `.env` file in the root of your project with the following content (update values accordingly):
```
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=retail_sales
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
```
**Note:** Never commit your `.env` file to version control.

## Usage
To run the server:
```
python manage.py runserver
```
Access the API at: http://127.0.0.1:8000/api/sales/

To fetch and update the sales data from the PostgreSQL view:
```
python manage.py fetch_sales_data
```

## API Endpoints
### GET /api/sales/
- **Description:** Retrieves all sales summary data.
- **Method:** GET
- **Response:**
  ```json
  [
      {
          "product_name": "Widget A",
          "category": "Widgets",
          "total_sales": 1500
      },
      {
          "product_name": "Gadget B",
          "category": "Gadgets",
          "total_sales": 3000
      }
  ]
  ```
- **Status Codes:**
  - `200 OK`: Successfully retrieved data
  - `500 Internal Server Error`: Server error

## Custom Management Commands
- **fetch_sales_data**
  - **Description:** Fetches sales data from the PostgreSQL view `v_sales_summary` and updates the `SalesSummary` model in Django.
  - **Execution:** Run `python manage.py fetch_sales_data` from the command line within your project directory.

## Contributing
To contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License
Include information about the project's license here.
```

This version reflects the correct URL for accessing the sales data API. It is more precise and aligns with the actual URL structure you've set up in your Django project.