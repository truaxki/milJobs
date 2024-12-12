# MilJobs

MilJobs is a platform that leverages Google's Cloud Talent Solution API to provide a streamlined job search experience. The platform is designed to help users find relevant job opportunities efficiently.

## Google Cloud Platform Setup

Before running the application, you'll need to set up your Google Cloud Platform project and enable the necessary APIs. Here's a step-by-step guide:

### 1. Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the project dropdown at the top of the page
3. Click "New Project" and give it a name (e.g., "miljobs")
4. Make note of your Project ID as you'll need it later

### 2. Enable the Cloud Talent Solution API

1. In the Google Cloud Console, go to the [APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard)
2. Click "+ ENABLE APIS AND SERVICES" at the top of the page
3. Search for "Cloud Talent Solution API"
4. Click on the API and then click "ENABLE"

### 3. Create Service Account and Download Credentials

1. In the Google Cloud Console, navigate to [IAM & Admin > Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
2. Click "CREATE SERVICE ACCOUNT"
3. Fill in the service account details:
   - Name: `miljobs-service-account` (or your preferred name)
   - Description: "Service account for MilJobs application"
4. Click "CREATE AND CONTINUE"
5. Assign these roles to the service account:
   - "Cloud Talent Solution Job Editor"
   - "Cloud Talent Solution Profile Editor"
   - "Cloud Talent Solution API User"
6. Click "CONTINUE" and then "DONE"
7. Find your new service account in the list and click on it
8. Go to the "KEYS" tab
9. Click "ADD KEY" > "Create new key"
10. Choose "JSON" format
11. Click "CREATE" - this will download your credentials file

### 4. Configure Your Environment

1. Rename your downloaded credentials file to something memorable (e.g., `gcp-credentials.json`)
2. Move the credentials file to your project directory (make sure it's listed in .gitignore!)
3. Create a `.env` file in your project directory by copying `.env.example`:
   ```bash
   cp .env.example .env
   ```
4. Edit your `.env` file with your specific values:
   ```
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_APPLICATION_CREDENTIALS=./gcp-credentials.json
   ```

### Security Notes

- Never commit your credentials file or .env file to version control
- Keep your service account key secure and don't share it
- Consider using environment variables in production environments
- Regularly rotate your service account keys

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/truaxki/milJobs.git
   cd milJobs
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify your setup:
   ```bash
   python -c "from google.cloud import talent; print('Talent API Client imported successfully')"
   ```

## Running the Application

1. Make sure your virtual environment is activated (if using one)
2. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Troubleshooting

Common issues and solutions:

1. "Permission denied" errors:
   - Verify your service account has the correct roles assigned
   - Check that your GOOGLE_APPLICATION_CREDENTIALS path is correct
   - Ensure the credentials file has the correct permissions

2. "API not enabled" errors:
   - Return to the Google Cloud Console
   - Verify the Cloud Talent Solution API is enabled for your project
   - Check that you're using the correct Project ID in your .env file

3. Credentials file issues:
   - Ensure the file path in GOOGLE_APPLICATION_CREDENTIALS matches your credentials file location
   - Check that the credentials file is valid JSON
   - Verify you're using the correct project ID

For additional help, consult the [Google Cloud Talent Solution documentation](https://cloud.google.com/talent-solution/docs).

## License

This project is licensed under the MIT License - see the LICENSE file for details.