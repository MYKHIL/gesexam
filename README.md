# GES Promotion Exam Practice - README

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Usage Guide](#usage-guide)
5. [Settings & Customization](#settings--customization)
6. [File Management](#file-management)
7. [Technical Details](#technical-details)
8. [Troubleshooting](#troubleshooting)
9. [Developer Contact](#developer-contact)

---

## Overview

**GES Promotion Exam Practice** is a web-based quiz application designed to help Ghana Education Service staff prepare for the promotion examination. The application features an intuitive interface, text-to-speech capabilities, and comprehensive study tools.

### Why This App?
- **No Installation Required**: Works in any modern web browser
- **Offline Ready**: Questions load locally (after initial load)
- **Privacy Focused**: All data stored locally in your browser
- **Customizable**: Adjust quiz settings to match your learning style
- **Accessible**: Native text-to-speech for users who prefer audio learning

---

## Features

### 1. Interactive Quiz Mode
- **Immediate Feedback**: See if your answer is correct instantly
- **Detailed Explanations**: Understand why each answer is correct
- **Question Navigation**: Jump between questions using the navigator
- **Progress Tracking**: Visual progress bar shows completion status
- **Session Control**: Quit or start new sessions anytime

### 2. Text-to-Speech (TTS)
- **Multi-Voice Selection**: Choose from available system voices
- **Speed Control**: Adjust playback speed (0.5x to 2x)
- **Pitch Adjustment**: Fine-tune voice pitch (0 to 2)
- **Auto-Narration**: Questions read automatically when enabled
- **Test Voice**: Preview selected voice before using

### 3. Review Mode
- **Post-Quiz Review**: Examine all questions after completion
- **Answer Verification**: See your answers vs. correct answers
- **Explanation Review**: Re-read explanations for learning
- **No Re-answering**: Review mode is read-only

### 4. Performance Appraisal
- **Score-Based Feedback**: Personalized messages based on performance
  - 90%+: Excellent work with exceptional mastery
  - 80-89%: Great job with strong understanding
  - 70-79%: Good effort with solid understanding
  - 60-69%: Basic understanding - review recommended
  - Below 60%: Comprehensive review recommended
- **Spoken Feedback**: Hear your performance appraisal via TTS

### 5. Question Management
- **Upload JSON Files**: Import custom question sets
- **Multiple Formats**: Supports any JSON array of questions
- **Auto-Merge**: Combines questions from multiple files
- **Deduplication**: Automatically removes duplicate questions
- **Auto-Load**: Questions from `Default questions/` folder load automatically

### 6. Settings & Customization
- **Session Questions**: Choose 1 to max available questions
- **Randomization**: Enable/disable random question order
- **Voice Settings**: Voice selection, speed, pitch
- **Auto-Save**: All settings saved automatically on change
- **Persistent**: Settings preserved across browser sessions

---

## Getting Started

### Requirements
- Modern web browser (Chrome, Firefox, Safari, Edge)
- HTTP server (cannot run from file:// protocol)
- JSON question files (provided in `Default questions/` folder)

### Setup Instructions

#### Option 1: Python HTTP Server (Recommended for Local Testing)
```bash
cd "d:\Projects\Promotions web app"
python -m http.server 8000
```
Then open: `http://localhost:8000`

#### Option 2: Node.js HTTP Server
```bash
npm install -g http-server
cd "d:\Projects\Promotions web app"
http-server
```

#### Option 3: Live Server (VS Code Extension)
1. Install "Live Server" extension in VS Code
2. Right-click on ADII Promotions.html
3. Select "Open with Live Server"

### First Time Setup
1. Open the application in your browser
2. Navigate to **Settings** to configure TTS (optional)
3. Go to **Study** and click **Start Session**
4. Begin answering questions

---

## Usage Guide

### Study Mode (Home Page)
**Screen Elements:**
- Session configuration summary (Questions, Order, TTS Status)
- TTS toggle button (top-right)
- **Start Session** button

**Actions:**
- Click **Start Session** to begin quiz with current settings
- Modify settings in **Settings** tab before starting
- Toggle TTS on/off without changing other settings

### Quiz Mode
**Screen Layout:**
- Question display with formatted text
- Multiple-choice options (A, B, C, D)
- Question navigator (numbered buttons)
- Progress bar showing answered/total questions
- Action buttons: Previous, Check Answer/Next, Quit Quiz

**Answering Questions:**
1. Click an option button to select it
2. Click **Check Answer** to submit
3. Receive immediate feedback (Correct/Incorrect)
4. See explanation for the correct answer
5. Click **Next** to continue or **Previous** to review

**Navigation:**
- Use arrow buttons or number buttons to jump between questions
- Green buttons = answered questions
- Gray buttons = unanswered questions
- Blue button = current question

### Results & Appraisal Page
**Displayed Information:**
- Total questions in session
- Correct answers count
- Percentage score
- Performance appraisal message (spoken via TTS)

**Available Actions:**
- **New Session**: Reset and start over
- **Review Questions**: Enter review mode to see all answers

### Review Mode
**Walkthrough:**
1. From results page, click **Review Questions**
2. Questions show in read-only format
3. Correct answers highlighted in green
4. Your incorrect answers highlighted in red
5. Full explanations displayed
6. Navigate using Previous/Next or question navigator
7. Click **Review Complete** on last question to return to results

---

## Settings & Customization

### Session Settings

#### Questions per Session
- **Range**: 1 to maximum available questions
- **Default**: 25 questions
- **Impact**: Affects quiz length and time commitment
- **Note**: If set value > available questions, will use all available

#### Randomize Question Order
- **Default**: Enabled
- **Benefit**: Better retention, prevents memorization of question order
- **Disable**: For sequential learning or reviewing in order

### Text-to-Speech (TTS) Settings

#### Enable/Disable TTS
- **Default**: Disabled
- **When Enabled**: Questions and feedback read aloud
- **Audio Output**: Spoken to your device speakers

#### Voice Selection
- **Default**: System default English voice
- **Test Voice Button**: Preview selected voice before using
- **Auto-Speak**: Plays when voice is changed to confirm selection

#### Playback Speed (Rate)
- **Range**: 0.5x (half speed) to 2x (double speed)
- **Default**: 1.0 (normal speed)
- **Use Case**: Slow down for clarity, speed up to save time

#### Voice Pitch
- **Range**: 0 (low pitch) to 2 (high pitch)
- **Default**: 1.0 (normal pitch)
- **Use Case**: Adjust for preference or hearing needs

### Auto-Save
- All settings save immediately on change
- No manual save button required
- Settings persist via browser's localStorage

---

## File Management

### Question File Format

**Required Structure:**
```json
[
  {
    "id": 1,
    "question": "What is the capital of Ghana?",
    "options": {
      "A": "Kumasi",
      "B": "Accra",
      "C": "Sekondi",
      "D": "Tema"
    },
    "answer": "B",
    "explanation": "Accra is the capital city of Ghana and the largest city in the country."
  },
  {
    "id": 2,
    ...
  }
]
```

**Field Requirements:**
- `id`: Unique integer (will be auto-reindexed after merge)
- `question`: String with question text (supports **bold** formatting)
- `options`: Object with keys A, B, C, D containing option text
- `answer`: Single letter (A, B, C, or D) indicating correct option
- `explanation`: String explaining why the answer is correct

**Optional Formatting:**
- Wrap text in `**asterisks**` to display in bold blue text
- Example: `"The **primary** goal is to educate."`

### Uploading Questions

**Steps:**
1. Go to **Management** tab
2. Click on "Click to select JSON file(s)" area
3. Select one or more JSON files
4. Click **Process & Load Questions**
5. New questions replace existing ones

**Multiple Files:**
- Can upload multiple files at once
- Questions from all files merge together
- Duplicates automatically removed
- IDs auto-reindexed sequentially

### Auto-Loading Questions

**Default Behavior:**
- App automatically loads questions from `Default questions/` folder
- Scans for files: set1.json through set50.json
- Supports up to 50 question sets (3,750 maximum questions)
- Deduplicates and merges all found questions
- Happens on app startup

**Adding Questions:**
1. Create JSON file following format above
2. Place in `Default questions/` folder
3. Refresh the application
4. Questions load automatically

### Download Options

**Download Current Quiz:**
- Exports all loaded questions as JSON file
- Useful for backup or sharing with others

**Download Template:**
- Gets empty JSON template for creating new questions
- Use as starting point for custom question sets

---

## Technical Details

### Browser Compatibility
| Browser | Support | Notes |
|---------|---------|-------|
| Chrome  | ✅ Full | Recommended |
| Firefox | ✅ Full | Full support |
| Safari  | ✅ Full | Full support |
| Edge    | ✅ Full | Full support |
| IE 11   | ❌ No   | Not supported |

### Data Storage
- **LocalStorage**: Settings and quiz state (max ~5-10MB)
- **SessionStorage**: Temporary quiz data
- **No Cloud**: Everything stays on your device
- **No Tracking**: No analytics or user tracking

### Performance
- **Load Time**: < 2 seconds typical
- **Question Limit**: Handles 1000+ questions smoothly
- **Memory**: Minimal footprint, uses ~2-5MB RAM
- **Offline**: Works offline after initial load

### Supported Question Count
- **Minimum**: 1 question
- **Maximum**: 50 sets × 75 questions = 3,750 questions
- **Typical**: 225 questions (3 sets of 75)

### Architecture
```
┌─────────────────────────────────────┐
│   Browser (HTML5 + JavaScript)      │
├─────────────────────────────────────┤
│  ├─ Quiz Engine (Question Logic)    │
│  ├─ TTS Engine (Web Speech API)     │
│  ├─ State Manager (localStorage)    │
│  └─ UI Controller (DOM Management)  │
├─────────────────────────────────────┤
│  JSON Files (Static Data)           │
│  ├─ set1.json - set50.json          │
│  └─ questions.json (legacy)         │
└─────────────────────────────────────┘
```

---

## Troubleshooting

### Questions Not Loading
**Problem**: App shows "No Quiz Data Loaded"

**Solutions:**
1. Ensure JSON files are in `Default questions/` folder
2. Verify files are named set1.json, set2.json, etc.
3. Check JSON syntax (valid JSON required)
4. Hard refresh browser (Ctrl+F5 or Cmd+Shift+R)
5. Check browser console for errors (F12)

### TTS Not Working
**Problem**: Voice doesn't play when enabled

**Solutions:**
1. Check if TTS is enabled (button should be green)
2. Test voice in Settings tab
3. Ensure computer volume is on
4. Try different voice from dropdown
5. Check browser permissions for audio

### Settings Not Saving
**Problem**: Settings reset on refresh

**Solutions:**
1. Allow localStorage in browser privacy settings
2. Check if "Private/Incognito" mode is enabled
3. Clear browser cache and try again
4. Check browser console for errors (F12)

### Questions Load Slowly
**Problem**: App takes long time to load

**Solutions:**
1. Normal for 1000+ questions (< 5 seconds typical)
2. Check internet connection speed
3. Try different browser
4. Close other browser tabs
5. Restart browser and try again

### Duplicate Questions Detected
**Problem**: Same question appears multiple times

**Solutions:**
1. Run find_duplicates.py utility to identify duplicates
2. Edit JSON files to remove exact duplicates
3. Upload corrected files
4. App automatically deduplicates on load

### JSON Upload Fails
**Problem**: "Invalid structure" error when uploading

**Solutions:**
1. Verify JSON format (use online validator)
2. Ensure all required fields present (id, question, options, answer, explanation)
3. Check for special characters causing issues
4. Validate options have keys A, B, C, D
5. Ensure answer is one of A, B, C, D

---

## Developer Contact

### Mr. Michael Darko
- **Phone**: 0542410613
- **Service**: Development, Support, Customization

### Support This Project
If you find this application helpful, please consider supporting the developer:
- **Mobile Money**: 0241899862
- **Your support enables**: Continued development, bug fixes, new features

---

## Version History

### v1.0.0 (November 2025)
- ✅ Core quiz functionality
- ✅ Text-to-speech with voice customization
- ✅ Review mode
- ✅ Performance appraisal system
- ✅ Multi-file question loading
- ✅ Automatic deduplication
- ✅ Responsive design
- ✅ Developer contact footer

---

## License
This application is provided for educational purposes. Please contact the developer for licensing or commercial use inquiries.

---

## Changelog

**Recent Updates:**
- Added bold text formatting support (**text**)
- Implemented review mode with performance analysis
- Enhanced voice test functionality
- Optimized for up to 50 question sets
- Improved mobile responsiveness

---

## FAQ

**Q: Can I use this on my phone?**
A: Yes! The app is fully responsive and works on mobile browsers. TTS works on most mobile devices too.

**Q: Will my settings be lost if I close the browser?**
A: No. Settings are saved in localStorage and persist across sessions.

**Q: Can I use this without internet?**
A: Yes, after the initial load. Questions and settings cache locally.

**Q: How do I add my own questions?**
A: Create a JSON file following the format in the README, place it in `Default questions/` folder, and refresh.

**Q: Can multiple people use this on the same computer?**
A: Yes, each browser profile has its own localStorage.

**Q: How accurate is the score calculation?**
A: Scores are calculated as: (Correct Answers ÷ Total Questions) × 100

**Q: Can I print my results?**
A: Use your browser's print function (Ctrl+P) to print the results page.

**Q: Is my data tracked or shared?**
A: No. Everything runs locally. No analytics or data collection.

---

## Support
For issues, questions, or feature requests, contact the developer at **0542410613**.

---

**Made with ❤️ to help GES staff succeed in their promotion exams.**

Last Updated: November 21, 2025
