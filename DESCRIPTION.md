# GES Promotion Exam Practice - Project Description

## Overview
GES Promotion Exam Practice is a web-based interactive quiz application designed to help Ghana Education Service (GES) staff prepare for the promotion examination. The application provides an engaging, self-paced learning environment with immediate feedback and comprehensive study features.

## Key Features
- **Interactive Quiz Mode**: Answer questions with immediate feedback and detailed explanations
- **Text-to-Speech (TTS)**: Native browser-based voice narration with customizable voice, speed, and pitch
- **Review Mode**: Re-examine all questions and answers after completing a quiz session
- **Performance Appraisal**: Receive personalized feedback based on quiz performance
- **Question Management**: Upload and manage multiple JSON-formatted question sets
- **Session Settings**: Customize number of questions, randomization, and TTS preferences
- **Auto-Save**: All settings persist across sessions via browser local storage
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Scalable Architecture**: Supports up to 50 question sets with automatic merging and deduplication

## Technology Stack
- **Frontend**: HTML5, CSS3 (Tailwind CSS), Vanilla JavaScript
- **TTS Engine**: Web Speech API (browser native)
- **Data Storage**: JSON files + Browser localStorage
- **No Backend Required**: Runs entirely in the browser
- **No Build Tools**: Pure HTML/CSS/JavaScript - no dependencies

## Target Users
- GES Staff preparing for promotion examination
- Teachers and administrators seeking professional development
- Educational institutions implementing assessment tools

## Developer
**Mr. Michael Darko**
- Contact: 0542410613
- Support Donations: 0241899862 (Mobile Money)

## File Structure
```
Promotions web app/
├── index.html                    # Main application file
├── questions.json                 # Original questions file
├── Default questions/
│   ├── set1.json                 # Question set 1
│   ├── set2.json                 # Question set 2
│   ├── set3.json                 # Question set 3
├── DESCRIPTION.md                # This file
└── README.md                     # Comprehensive documentation
```

## Quick Start
1. Place HTML file on an HTTP server (required for browser fetch operations)
2. Ensure JSON question files are in the `Default questions/` directory
3. Navigate to the application URL in a web browser
4. Questions auto-load from available JSON files
5. Click "Start Session" to begin the quiz

## Note
This application requires an HTTP server to run (file:// protocol doesn't support fetch operations). Use `python -m http.server 8000` for local testing.
