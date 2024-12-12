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
   - Update the values in `.env` with your Google Cloud credentials

## Configuration

This project requires Google Cloud Project credentials. Make sure you have:

1. A Google Cloud Project with the Talent Solution API enabled
2. Proper credentials set up for accessing the API

See `.env.example` for required environment variables.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
