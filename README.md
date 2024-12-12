# MilJobs

MilJobs is a platform that leverages Google's Cloud Talent Solution API to provide a streamlined job search experience. The platform is designed to help users find relevant job opportunities efficiently.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/truaxki/milJobs.git
   cd milJobs
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your credentials

## Configuration

This project requires the following credentials:

1. GitHub Personal Access Token (for development)
2. Google Cloud Project credentials

See `.env.example` for required environment variables.

## Development

To verify your GitHub authentication:
```bash
python github_auth.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
