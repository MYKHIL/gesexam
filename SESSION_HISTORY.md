# Session History & Leaderboard Feature Documentation

## Overview

The Session History & Leaderboard feature tracks all quiz attempts across sessions, providing users with persistent performance analytics and visual progress tracking.

## Features

### 1. **Automatic Session Tracking**
- Every quiz completion is automatically saved to browser localStorage
- Sessions persist across browser refreshes and app restarts
- Each session records:
  - Number of correct answers
  - Total questions attempted
  - Percentage score
  - Timestamp (ISO format)

### 2. **Leaderboard View**
- Access via "View Leaderboard" button on results page
- Displays all previous quiz sessions in table format
- **Columns:**
  - Session #: Sequential numbering (most recent first)
  - Questions: Total questions in that session
  - Correct: Number of correct answers
  - Score: Percentage score
  - Date & Time: Formatted date and time of quiz completion

- **Statistics Cards:**
  - Total Sessions: Count of all completed quizzes
  - Average Score: Mean score across all sessions
  - Best Score: Highest score achieved

### 3. **Progress Graph Visualization**
- SVG-based line chart showing score progression
- **Features:**
  - X-axis: Session number (#1, #2, etc.)
  - Y-axis: Score percentage (0-100%)
  - Interactive data points (circles) showing exact score on hover
  - Smooth line connecting all data points

- **Statistics Displayed:**
  - Average Score: Mean across all sessions
  - Best Score: Maximum score
  - Worst Score: Minimum score
  - Overall Trend: Change from first to most recent session (shows improvement/decline)

### 4. **Data Persistence**
- **localStorage Key:** `gesAdiiSessionHistory`
- **Storage Format:** JSON array of session objects
- **Data Structure:**
  ```json
  [
    {
      "correctAnswers": 45,
      "totalQuestions": 50,
      "percentage": 90.0,
      "timestamp": "2025-11-21T15:30:45.123Z"
    }
  ]
  ```

## User Workflow

### Completing a Quiz
1. User completes a quiz and views results
2. System displays performance appraisal and score
3. Session is **automatically saved** to history (no user action needed)
4. Results page shows three action buttons:
   - "New Session" - Start another quiz
   - "Review Questions" - Review answered questions
   - **"View Leaderboard"** - NEW

### Accessing Session History
1. Click "View Leaderboard" button (from results page or home navigation)
2. View all previous sessions in table format
3. See aggregated statistics (total sessions, average score, best score)
4. Click "View Progress Graph" to see visual trend

### Viewing Progress Graph
1. From leaderboard, click "View Progress Graph"
2. See SVG line chart of score progression
3. View key statistics (average, best, worst, trend)
4. Navigate back to leaderboard or home

## Technical Implementation

### Global State Variables
```javascript
const SESSION_HISTORY_KEY = 'gesAdiiSessionHistory';
let sessionHistory = []; // Array of session objects
```

### Key Functions

#### `saveSessionToHistory(correctAnswers, totalQuestions)`
Called automatically after each quiz completion.
- Calculates percentage score
- Creates session object with timestamp
- Appends to sessionHistory array
- Persists to localStorage

#### `loadSessionHistory()`
Called during app initialization (in `loadState()`).
- Retrieves session history from localStorage
- Parses JSON data
- Populates sessionHistory array
- Logs number of sessions loaded

#### `renderLeaderboardView()`
Renders the leaderboard UI with:
- Session history table (reversed, most recent first)
- Statistics cards (total sessions, average, best score)
- "View Progress Graph" button

#### `renderProgressGraphView()`
Renders the progress graph with:
- SVG line chart visualization
- Statistics cards
- Navigation buttons

### View Navigation

Updated `setView()` function handles:
```javascript
if (view === 'leaderboard') {
    renderLeaderboardView();
} else if (view === 'graph') {
    renderProgressGraphView();
}
```

### Integration Points

1. **In `loadState()` after TTS initialization:**
   ```javascript
   loadSessionHistory();
   ```

2. **In `renderResults()` after score calculation:**
   ```javascript
   saveSessionToHistory(result.correct, result.total);
   ```

3. **Results page button additions:**
   ```html
   <button onclick="setView('leaderboard')" 
           class="px-6 py-3 bg-indigo-600 text-white font-bold rounded-lg hover:bg-indigo-700">
       View Leaderboard
   </button>
   ```

## Data Flow

```
Quiz Completion
    ↓
Calculate Score → saveSessionToHistory()
    ↓
Append to sessionHistory array
    ↓
Store in localStorage (gesAdiiSessionHistory)
    ↓
App Startup
    ↓
loadSessionHistory() → Retrieve from localStorage
    ↓
Populate sessionHistory array for display
```

## User Interface

### Leaderboard Page Layout
```
┌─────────────────────────────────┐
│ Session History    [Back Button] │
├─────────────────────────────────┤
│ [Total Sessions] [Avg %] [Best%]│
├─────────────────────────────────┤
│ Session│Qs│Correct│Score│Date   │
├─────────────────────────────────┤
│   #5   │50│  42   │84%  │Nov 21  │
│   #4   │50│  40   │80%  │Nov 20  │
│   #3   │50│  45   │90%  │Nov 19  │
│        ...         │     │        │
├─────────────────────────────────┤
│ [View Progress Graph Button]     │
└─────────────────────────────────┘
```

### Progress Graph Page Layout
```
┌────────────────────────────────────┐
│ Performance Progress  [Back Button] │
├────────────────────────────────────┤
│ [Avg %] [Best %] [Worst %] [Trend] │
├────────────────────────────────────┤
│                                    │
│    100%    ●                       │
│            ╱╲                      │
│    50%    ●  ●─●──●    (Line Chart)│
│         ╱  ╲╱                      │
│    0%   ●                          │
│        #1  #2  #3  #4  #5         │
│                                    │
├────────────────────────────────────┤
│ [Back to Leaderboard] [Back Home]  │
└────────────────────────────────────┘
```

## Browser Compatibility

- **Storage Method:** localStorage (all modern browsers support)
- **Graphics:** SVG (all modern browsers support)
- **Date Formatting:** Intl.DateTimeFormat (all modern browsers support)

## Limitations & Notes

1. **localStorage Quota:** Limited to ~5-10MB per domain. With average session size ~100 bytes, this supports 50,000+ sessions
2. **Session Reversal:** Leaderboard shows most recent sessions first (array is reversed)
3. **Empty State:** Displays message if no sessions exist
4. **Graph Minimum:** Requires at least 1 session to display leaderboard; graph shows empty state message if no data

## Future Enhancement Ideas

1. **Export to CSV:** Allow users to download session history as spreadsheet
2. **Filtering:** Filter sessions by date range or score range
3. **Comparison:** Compare performance across different question sets
4. **Achievements:** Badge system for milestones (100% score, 10 sessions, etc.)
5. **Server Sync:** Sync session history to server for cross-device access
6. **Detailed Analytics:** Time spent per session, categories with highest/lowest scores
7. **Goal Tracking:** Set score targets and track progress toward goals

## Troubleshooting

### Sessions not saving
- Check browser localStorage is enabled
- Verify no errors in browser console
- Try clearing cache and restarting quiz

### Leaderboard shows no data
- Complete at least one full quiz session
- Check localStorage for `gesAdiiSessionHistory` key
- Verify quiz is completing without errors

### Graph not displaying
- Ensure at least one session is recorded
- Check browser console for SVG rendering errors
- Verify SVG dimensions are appropriate for screen size

### Data lost after refresh
- localStorage data should persist
- If lost, check browser privacy settings
- Private/Incognito mode may not persist data between sessions

## Code References

- **Global Constants:** Lines ~172-192
- **Session Functions:** Lines ~1215-1240
- **Leaderboard Rendering:** Lines ~1241-1340
- **Graph Rendering:** Lines ~1341-1450
- **View Router Updates:** Lines ~534-545
- **Results Page Integration:** Lines ~1265
