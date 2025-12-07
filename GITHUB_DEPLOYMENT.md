# GitHub Deployment Guide

## Issues Fixed for GitHub Deployment

### Problem 1: Default Questions Folder Not Found
**Cause**: GitHub repository has case-sensitive paths, and the folder name matters.

**Solution Applied**:
- The app now searches for both `Default questions/` and `default-questions/` folder names
- Added fallback paths for multiple common directory structures
- Added console logging to debug which files are found

**GitHub Setup Instructions**:
1. In your GitHub repository, rename the folder:
   - From: `Default questions`
   - To: `default-questions` (lowercase with hyphen)
   
   OR keep it as `Default questions` if you're on Windows - the code now supports both.

2. Ensure all JSON files (set1.json through set50.json) are in the `default-questions/` folder

3. Make sure the `index.html` file is in the root directory of your repository

### Problem 2: TTS (Text-to-Speech) Not Working
**Cause**: Browser native speech synthesis wasn't being triggered properly.

**Solution Applied**:
- Added explicit `synth.speak(utterance)` call to ensure speech is triggered
- Added console logging for TTS initialization and voice detection
- Added error handling for voice synthesis failures

**Browser Requirements for TTS**:
- Chrome/Chromium: ✅ Full support (recommended)
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Edge: ✅ Full support
- Mobile browsers: ✅ Supported on most (iOS Safari, Chrome Mobile, Firefox Mobile)

**If TTS Still Doesn't Work**:
1. Open browser DevTools (F12)
2. Go to Console tab
3. Look for messages like:
   - "TTS initialized successfully" ✅
   - "Found X English voices available" ✅
   - "Browser Speech Synthesis not supported" ❌
   - "No English voices found" ⚠️

4. Common fixes:
   - Check if browser has English voices installed: `speechSynthesis.getVoices().filter(v => v.lang.startsWith('en'))`
   - Try a different browser
   - Ensure volume is not muted on your device
   - Try enabling TTS and clicking "Test Voice" in Settings

### GitHub Repository Structure

**Recommended folder layout for GitHub**:
```
GES-Promotion-Quiz/
├── index.html                    (main app file)
├── README.md                     (documentation)
├── DESCRIPTION.md                (project description)
├── default-questions/            (lowercase with hyphen)
│   ├── set1.json
│   ├── set2.json
│   ├── set3.json
│   └── ... (up to set50.json)
└── find_duplicates.py            (utility script)
```

### How to Deploy on GitHub Pages

1. **Push your files to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit: GES Promotion Quiz App"
   git push origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository Settings
   - Scroll to "GitHub Pages" section
   - Source: Select "main" branch
   - Click Save

3. **Access your app**:
   - Your app will be available at: `https://yourusername.github.io/your-repo-name/`

### Troubleshooting Checklist

**Questions Not Loading**:
- [ ] Verify folder is named `default-questions` (lowercase, hyphen)
- [ ] Verify JSON files are in the folder
- [ ] Check console (F12) for which files are being loaded
- [ ] Verify JSON files are valid (use online JSON validator)
- [ ] Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)

**TTS Not Working**:
- [ ] Check console for TTS initialization messages
- [ ] Verify browser supports Web Speech API
- [ ] Test voice in Settings tab
- [ ] Check if device volume is muted
- [ ] Try different browser
- [ ] Allow microphone/audio permissions if prompted

**File Structure Issues**:
- [ ] Ensure `index.html` is in repository root
- [ ] Ensure `default-questions/` folder is in repository root
- [ ] No typos in folder or file names
- [ ] Use lowercase for folder names to avoid case sensitivity issues

### Console Debug Commands

Open browser console (F12) and run these to debug:

```javascript
// Check if questions loaded
console.log("Questions loaded:", allQuestions.length);

// Check TTS availability
console.log("TTS available:", window.speechSynthesis ? "Yes" : "No");

// Check available voices
console.log("English voices:", voices.length);
voices.forEach(v => console.log(v.name, v.lang));

// Test TTS directly
const utterance = new SpeechSynthesisUtterance("Hello, this is a test.");
window.speechSynthesis.speak(utterance);
```

### File Size Notes

- Each JSON question file (set1-set20): ~30-50 KB
- Total with all files: ~1-2 MB
- `index.html`: ~50 KB
- Total app size: Minimal, loads very quickly

### Browser Cache Considerations

The app uses cache-busting with timestamps to ensure fresh data:
```javascript
const cacheBuster = `v=${Date.now()}`;
```

This means every refresh will fetch the latest JSON files, so updates to questions will be reflected immediately on GitHub.

### Contact for Issues

If you encounter any problems after GitHub deployment:
1. Check the console for error messages (F12)
2. Verify folder and file structure
3. Contact: **Mr. Michael Darko - 0542410613**

### Success Indicators

✅ **Things should work when**:
- You see "Successfully loaded X questions from: default-questions/set1.json" in console
- The "Start Session" button is clickable
- Questions appear in the quiz
- "Test Voice" button plays audio in Settings
- You can see available voices in the voice dropdown

---

**Last Updated**: November 21, 2025
**Version**: 1.0 - GitHub Deployment Ready
