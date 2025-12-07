# Session History & Leaderboard - User Guide

## Quick Start

### Accessing Session History

1. **After Completing a Quiz:**
   - Results page displays your score and performance appraisal
   - Three buttons appear:
     - "New Session" - Start another quiz
     - "Review Questions" - Review your answers
     - **"View Leaderboard"** - See your session history ⭐ NEW

2. **From Home Screen:**
   - Session history is automatically accessible via the leaderboard feature
   - No special settings or configurations needed

### Viewing Your Leaderboard

**Step 1:** Click "View Leaderboard" button (on results page)

**Step 2:** Review your session history table showing:
- Session number (most recent first)
- Questions attempted
- Correct answers
- Percentage score
- Date and time of quiz

**Step 3:** Review statistics at the top:
- **Total Sessions:** How many quizzes you've completed
- **Average Score:** Your mean performance
- **Best Score:** Your highest score

### Viewing Your Progress Graph

**Step 1:** From the leaderboard, click "View Progress Graph"

**Step 2:** See your performance trend as a line chart:
- Each point represents one quiz session
- Line shows your score progression over time
- Higher line = better performance

**Step 3:** Review key metrics:
- **Average Score:** Overall performance
- **Best Score:** Highest achievement
- **Worst Score:** Lowest score
- **Overall Trend:** Improvement from first to most recent session
  - Positive number = improving
  - Negative number = declining
  - 0 = stable

## Features Explained

### Session Table Columns

| Column | Description |
|--------|-------------|
| **Session** | Sequential number assigned to each quiz (most recent first) |
| **Questions** | Total number of questions in that quiz session |
| **Correct** | Number of questions answered correctly |
| **Score** | Percentage score (0-100%) |
| **Date & Time** | When the quiz was completed (formatted for your region) |

### Example Session Table

```
Session │ Questions │ Correct │ Score │ Date & Time
───────┼───────────┼─────────┼───────┼──────────────────────
   #5  │    50     │   45    │  90%  │ Nov 21, 2025 at 3:45 PM
   #4  │    50     │   40    │  80%  │ Nov 20, 2025 at 2:30 PM
   #3  │    50     │   42    │  84%  │ Nov 19, 2025 at 10:15 AM
   #2  │    50     │   35    │  70%  │ Nov 18, 2025 at 4:20 PM
   #1  │    50     │   32    │  64%  │ Nov 17, 2025 at 11:00 AM
```

### Progress Graph Example

```
Your Performance Progression Over Time

100% ┤
     │     Session #5 (90%)
  90%┤    /
     │   /  Session #4 (80%)
  80%┤  /
     │ /
  70%┤○       Session #3 (84%)
     │ \    /
  60%┤  \  / Session #2 (70%)
     │   \/
     │  Session #1 (64%)
  50%┤
     │
     └─────────────────────────
      #1  #2  #3  #4  #5
    Session Number
```

## Tips & Best Practices

### 1. **Regular Practice**
- Complete multiple quizzes to build up your session history
- Track your improvement over time with the progress graph
- Aim to maintain or improve your average score

### 2. **Interpreting Your Statistics**

- **High Average Score (80%+):** You have strong mastery of the material
- **Improving Trend (Positive):** You're learning and getting better
- **Stable Score:** You've reached a consistent level of performance
- **Declining Trend (Negative):** Material may need review

### 3. **Using Graph Trends**

- **Upward trend:** Continue current study approach - it's working!
- **Plateau:** Try different study methods or materials
- **Downward trend:** Review material more thoroughly
- **Sharp jumps:** Mix of easy and difficult question sets - consistent practice helps

### 4. **Session Planning**

- Use your "Best Score" as a target to hit consistently
- Track which question sets perform better for you
- Focus on areas where your scores are lowest

## Data Management

### Viewing Stored Data (For Advanced Users)

Your session history is stored in your browser's localStorage. To view it:

1. Open browser Developer Tools (F12 or Ctrl+Shift+I)
2. Go to "Storage" or "Application" tab
3. Click "Local Storage"
4. Find your domain
5. Look for key: `gesAdiiSessionHistory`
6. Value contains all your session data

### Clearing Session History (If Needed)

1. Open browser Developer Tools
2. Go to "Storage" → "Local Storage"
3. Right-click the domain and select "Delete All"
4. Or use "Clear Browsing Data" in browser settings

**Warning:** This will clear all stored data including quiz settings and session history.

### Backup Your Data

To save your session history:

1. Open Developer Tools → Storage → Local Storage
2. Select the `gesAdiiSessionHistory` value
3. Copy the entire JSON string
4. Paste into a text editor and save as `.json` file
5. Keep as backup on your computer

## Troubleshooting

### Problem: "No sessions yet" message

**Solution:** 
- Complete at least one full quiz to create a session
- Make sure to complete the entire quiz (don't quit midway)

### Problem: Sessions are missing after browser update

**Solution:**
- Browser updates may clear localStorage
- Private/Incognito mode doesn't persist data
- Use normal browsing mode for persistent storage
- Try backing up data (see above)

### Problem: Graph looks empty

**Solution:**
- You need at least one completed session
- Complete another quiz to see the graph appear

### Problem: Dates look strange

**Solution:**
- Date format depends on your browser's locale settings
- Format is: Month Day, Year at Time (12-hour)
- Example: "Nov 21, 2025 at 3:45 PM"

## Performance Metrics Guide

### Understanding Your Scores

```
95-100%  ─ Outstanding mastery. Ready for certification!
85-94%   ─ Excellent understanding. Minor gaps to address
75-84%   ─ Good comprehension. Review weak areas
65-74%   ─ Decent understanding. More practice needed
55-64%   ─ Basic comprehension. Focus on fundamentals
<55%     ─ Need improvement. Thorough review recommended
```

### Tracking Progress

- **1st Session:** Baseline to measure improvement from
- **Sessions 2-5:** Building consistency
- **Sessions 5+:** Identifying patterns and stable performance level

## Navigation Guide

### From Results Page
```
Results Page
├── [New Session] ─→ Start another quiz
├── [Review Questions] ─→ Review your answers
└── [View Leaderboard] ─→ See all sessions & statistics ⭐
```

### From Leaderboard Page
```
Leaderboard
├── [Back to Home] ─→ Return to quiz home
└── [View Progress Graph] ─→ See visual score trend ⭐
```

### From Progress Graph Page
```
Progress Graph
├── [Back to Leaderboard] ─→ Return to session list
└── [Back to Home] ─→ Return to quiz home
```

## Frequently Asked Questions

**Q: Does my history sync across devices?**
A: No, currently history is stored only in your browser's localStorage. To access on another device, you would need to manually backup and transfer the data.

**Q: Can I export my session history?**
A: Currently not built-in, but you can manually copy your data from localStorage (see "Backup Your Data" section above).

**Q: How long is my history saved?**
A: Until you clear your browser's localStorage or switch to a different browser/device. Data persists across normal browser sessions and restarts.

**Q: Will sessions be deleted if I clear cache?**
A: Yes, if you select "Clear browsing data" including localStorage. Regular cache clearing (without localStorage) won't affect your session history.

**Q: Can I manually add sessions?**
A: Not through the UI. Sessions are automatically created when you complete quizzes. To manually add data, you would need to edit localStorage directly (advanced).

**Q: What if the graph shows a declining trend?**
A: This may indicate:
- Fatigue during later sessions
- Increasingly difficult question sets
- Need for more focused study
- Consider reviewing study materials or taking breaks

**Q: Why are sessions numbered in reverse order?**
A: Most recent sessions appear first, similar to an email inbox or messaging app. This makes it easy to see your latest performance.

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Developer Tools | F12 or Ctrl+Shift+I |
| Access Browser Storage | F12 → Storage/Application tab |

## Need Help?

If you experience issues:

1. Check browser Developer Tools for errors (F12)
2. Ensure JavaScript is enabled in browser
3. Try a different browser to isolate issues
4. Clear cache and try again
5. Ensure you're using a modern browser (Chrome, Firefox, Safari, Edge)

---

**Last Updated:** November 2025
**Feature Version:** 1.0
**Browser Support:** All modern browsers with localStorage support
