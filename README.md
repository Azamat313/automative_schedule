# Schedule App - Python Flask Web Application

A simple and elegant web application for managing schedules, built with Flask and SQLite.

## Features

- View all scheduled events
- Add new events with title, description, date, time, and location
- Edit existing events
- Delete events
- Local SQLite database (no external database required)
- Clean and responsive UI
- REST API endpoint for events

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite (local database)
- **Frontend**: HTML, CSS, Jinja2 templates
- **No external dependencies** except Flask

## Quick Start

### 1. Install Python

Make sure you have Python 3.7+ installed:

```bash
python3 --version
```

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd automative_schedule
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python3 app.py
```

The application will start on `http://localhost:5000`

## Database

The application uses SQLite as a local database. The database file `schedule.db` will be automatically created when you first run the application.

Sample events are automatically added on the first run.

## Project Structure

```
automative_schedule/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── schedule.db            # SQLite database (created automatically)
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── add_event.html    # Add event form
│   └── edit_event.html   # Edit event form
└── static/               # Static files
    └── css/
        └── style.css     # Stylesheet
```

## API Endpoints

### Web Routes

- `GET /` - Home page with list of events
- `GET /add` - Add event form
- `POST /add` - Submit new event
- `GET /edit/<id>` - Edit event form
- `POST /edit/<id>` - Update event
- `POST /delete/<id>` - Delete event

### API Route

- `GET /api/events` - Get all events as JSON

Example response:
```json
[
  {
    "id": 1,
    "title": "Team Meeting",
    "description": "Weekly team sync",
    "date": "2025-11-10",
    "time": "10:00",
    "location": "Conference Room A"
  }
]
```

## Deployment Options

### Option 1: Local Development

Run on your local machine (see Quick Start above).

### Option 2: Deploy on a Server

1. Install Python and pip on your server
2. Clone the repository
3. Install dependencies: `pip install -r requirements.txt`
4. Run with production server:

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option 3: Deploy with Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Build and run:

```bash
docker build -t schedule-app .
docker run -p 5000:5000 schedule-app
```

## Usage

1. **View Events**: Visit the home page to see all scheduled events
2. **Add Event**: Click "Add Event" button and fill in the form
3. **Edit Event**: Click "Edit" on any event card
4. **Delete Event**: Click "Delete" on any event card (with confirmation)

## Development

To modify the application:

1. Edit `app.py` for backend logic
2. Edit templates in `templates/` for HTML structure
3. Edit `static/css/style.css` for styling

The application will automatically reload when you make changes (in debug mode).

## License

MIT License - feel free to use this project for learning or production.

## Support

For issues or questions, please open an issue on GitHub.
