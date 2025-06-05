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

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment. The pipeline automatically builds, tests, and packages the application.

### Pipeline Features

- **Automated Testing**: Runs unit tests on every push and pull request
- **Docker Build**: Creates Docker images with automatic tagging
- **Multi-Platform Support**: Builds for both AMD64 and ARM64 architectures
- **Container Registry**: Pushes images to GitHub Container Registry (ghcr.io)
- **Security Scanning**: Validates code and container security

### Workflow Triggers

The CI/CD pipeline runs on:
- **Push to main/master branch**: Full build, test, and deployment
- **Pull Requests**: Testing and validation only
- **Manual Dispatch**: Can be triggered manually from GitHub Actions tab

### Package Distribution

Built Docker images are available at:
```
ghcr.io/akash-bhavsar/fastapi-app:latest
ghcr.io/akash-bhavsar/fastapi-app:v1.0.0
```

To use the pre-built image:
```bash
docker pull ghcr.io/akash-bhavsar/fastapi-app:latest
docker run -p 8000:8000 ghcr.io/akash-bhavsar/fastapi-app:latest
```

### Pipeline Configuration

The GitHub Actions workflow includes:
1. **Setup**: Python environment and dependencies
2. **Test**: Run pytest with coverage reporting
3. **Build**: Create Docker image with proper tagging
4. **Security**: Scan for vulnerabilities
5. **Deploy**: Push to container registry

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
