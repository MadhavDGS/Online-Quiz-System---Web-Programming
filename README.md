# Online-Quiz-System---Web-Programming

An interactive web-based quiz application for testing knowledge in web programming concepts. Built with Flask and modern web technologies.

## Features

- Multiple choice questions organized by units
- Immediate feedback on answers
- Progress tracking
- Dark/Light theme toggle
- Responsive design
- Score tracking and final results

## Tech Stack

- Python/Flask
- HTML/CSS/JavaScript
- Bootstrap 5
- Font Awesome

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## Deployment on Render

This application is configured for deployment on Render.com. Follow these steps to deploy:

1. Fork or clone this repository to your GitHub account
2. Sign up for a free account at [Render.com](https://render.com)
3. From your Render dashboard, click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure the deployment:
   - Name: `web-programming-quiz`
   - Environment: `Python`
   - Region: Choose closest to your users
   - Branch: `main`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Click "Create Web Service"

The application will be automatically deployed using the configuration in `render.yaml`. Render will provide you with a URL where your quiz application is accessible. 