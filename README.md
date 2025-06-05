# FastAPI App

A simple FastAPI application that demonstrates REST API development with Docker containerization and automated testing.

## Features

- **Simple REST API**: Single endpoint that returns application metadata
- **Git Integration**: Shows current git commit SHA in the response
- **Docker Support**: Full containerization with Docker and Docker Compose
- **Testing**: Unit tests with mocking using pytest and unittest
- **GitHub Actions**: CI/CD pipeline for automated builds and testing

## Quick Start

### Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API**:
   - Open your browser to `http://localhost:8000`
   - View API docs at `http://localhost:8000/docs`

### Using Docker

1. **Build and run with Docker Compose**:
   ```bash
   docker compose up --build
   ```

2. **Access the application**:
   - API endpoint: `http://localhost:8000`
   - Interactive docs: `http://localhost:8000/docs`

## API Endpoints

### `GET /`
Returns application information including version, description, and current git commit SHA.

**Response Example**:
```json
{
  "FastAPI": {
    "version": "1.0.0",
    "description": "This App demonstrate a Fast API example and some github actions",
    "sha": "15b1e12abc..."
  }
}
```

## Project Structure

```
├── main.py              # FastAPI application
├── __manifest__.py      # Application metadata
├── requirements.txt     # Python dependencies
├── test.py             # Unit tests
├── Dockerfile          # Docker container configuration
├── compose.yaml        # Docker Compose configuration
└── README.md           # This file
```

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **GitPython**: Git repository interaction
- **httpx**: HTTP client for testing
- **pytest**: Testing framework

## Testing

Run the test suite:

```bash
python -m pytest test.py
```

Or run with unittest:

```bash
python test.py
```

The tests include:
- API endpoint functionality testing
- Git SHA retrieval mocking
- Response format validation

## Docker Details

- **Base Image**: Python 3.9.6 slim
- **Port**: 8000
- **Security**: Runs as non-privileged user
- **Optimization**: Uses Docker layer caching for dependencies

## Development

### Adding New Features

1. Modify `main.py` to add new endpoints
2. Update tests in `test.py`
3. Update version in `__manifest__.py` if needed
4. Run tests to ensure everything works

### Environment Variables

The application uses these environment variables:
- `GIT_PYTHON_REFRESH=quiet` - Suppresses GitPython warnings

## Author

**Akash Bhavsar**  
Email: arbhavsar63@gmail.com

## License

This project is a demonstration application for FastAPI and GitHub Actions.
