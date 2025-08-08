# Book Manager API

A simple RESTful API for managing books, built with FastAPI and Pydantic.

## Features

- List all books  
- Add a new book  
- Retrieve a book by ID  
- Retrieve books by rating  
- Update book details  
- Delete a book  

## Technology Stack

- **FastAPI** - Web framework for building APIs  
- **Pydantic** - Data validation and settings management  
- **Python 3.10+**

## Project Structure
   ```
      src/
      ├── commons/ # Common models (e.g. Book class)
      ├── models/
      │ ├── requests/ # Request schemas
      │ ├── book_response.py/ # Book response schema
      │ └── response.py # BasicResponse model
      ├── business_logic/ # Core business logic
      └── main.py # FastAPI app entry point
   ```

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/api-sage/book_manager.git
   cd book_manager
   
2. Create and activate a virtual environment:
   ```bash
    python -m venv venv
    source venv/bin/  # Linux/macOS
    venv\Scripts\ # Windows
    activate     

4. Install dependencies:
   ```bash
   cd src
   pip install -r requirements.txt

6. Running the Application
     ```bash
     cd ..
     uvicorn main:app --reload

#### The API will be available at: http://127.0.0.1:8000/docs


| Method | Endpoint                | Description              |
| ------ | ----------------------- | ------------------------ |
| GET    | /get\_all\_books        | Retrieve all books       |
| POST   | /insert\_a\_book        | Insert a new book        |
| GET    | /get\_book\_by\_id/{id} | Retrieve a book by ID    |
| GET    | /get\_book\_by\_rating  | Retrieve books by rating |
| PUT    | /update\_a\_book/{id}   | Update an existing book  |
| DELETE | /delete\_a\_book/{id}   | Delete a book by ID      |

### Notes
* This project uses an in-memory list (Books) as a mock database.
* The id for new books is auto-incremented based on the last inserted book.
* Responses are standardized using the BasicResponse model.

### License
This project is open source and available under the MIT License.
