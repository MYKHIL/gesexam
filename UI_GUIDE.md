# Session History & Leaderboard - UI Guide

## Page Layouts & Visual Flow

### 1. Results Page (Updated)

```
╔═══════════════════════════════════════════════════════════╗
║                    Session Complete!                     ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  ┌───────────┐  ┌───────────┐  ┌───────────┐            ║
║  │   TOTAL   │  │ CORRECT   │  │   SCORE   │            ║
║  │    50     │  │    45     │  │   90%     │            ║
║  └───────────┘  └───────────┘  └───────────┘            ║
║                                                           ║
║  ┌─────────────────────────────────────────────────────┐ ║
║  │ Excellent work! You scored 90%, which is           │ ║
║  │ outstanding. You have demonstrated exceptional    │ ║
║  │ knowledge and mastery of the material.             │ ║
║  └─────────────────────────────────────────────────────┘ ║
║                                                           ║
║  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐      ║
║  │ New Session  │ │Review Qs     │ │View          │      ║
║  │              │ │              │ │Leaderboard ✨│      ║
║  └──────────────┘ └──────────────┘ └──────────────┘      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
                           ↓
                   [Click View Leaderboard]
                           ↓
```

### 2. Leaderboard Page (New)

```
╔═══════════════════════════════════════════════════════════╗
║  Session History              [Back to Home]            ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐      ║
║  │     5        │ │    90%       │ │    90%       │      ║
║  │   Sessions   │ │  Avg Score   │ │ Best Score   │      ║
║  └──────────────┘ └──────────────┘ └──────────────┘      ║
║                                                           ║
║  ┌─────────────────────────────────────────────────────┐ ║
║  │ Session │ Qs │ Correct │ Score │ Date & Time      │ ║
║  ├─────────────────────────────────────────────────────┤ ║
║  │   #5    │50 │   45    │  90%  │Nov 21, 3:45 PM   │ ║
║  │   #4    │50 │   40    │  80%  │Nov 20, 2:30 PM   │ ║
║  │   #3    │50 │   42    │  84%  │Nov 19, 10:15 AM  │ ║
║  │   #2    │50 │   35    │  70%  │Nov 18, 4:20 PM   │ ║
║  │   #1    │50 │   32    │  64%  │Nov 17, 11:00 AM  │ ║
║  └─────────────────────────────────────────────────────┘ ║
║                                                           ║
║         [View Progress Graph Button]                    ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
                           ↓
                 [Click View Progress Graph]
                           ↓
```

### 3. Progress Graph Page (New)

```
╔═══════════════════════════════════════════════════════════╗
║  Performance Progress              [Back to Leaderboard] ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐           ║
║  │  90%   │ │  90%   │ │  64%   │ │ +26%   │           ║
║  │Average │ │  Best  │ │ Worst  │ │ Trend  │           ║
║  └────────┘ └────────┘ └────────┘ └────────┘           ║
║                                                           ║
║  ┌─────────────────────────────────────────────────────┐ ║
║  │  Score Progression Over Time                        │ ║
║  │                                                     │ ║
║  │100% ┤                                              │ ║
║  │    │      ●                                        │ ║
║  │ 90%┤     / \                                       │ ║
║  │    │    /   ●─●──●                                │ ║
║  │ 70%┤   /         \  ●                              │ ║
║  │    │  /                                            │ ║
║  │ 50%┤ ●                                              │ ║
║  │    │                                               │ ║
║  │    └─────────────────────────────────────────     │ ║
║  │      #1  #2  #3  #4  #5                           │ ║
║  │                                                     │ ║
║  └─────────────────────────────────────────────────────┘ ║
║                                                           ║
║  ┌───────────────────┐ ┌───────────────────┐           ║
║  │Back to Leaderboard│ │   Back to Home    │           ║
║  └───────────────────┘ └───────────────────┘           ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

## Color Scheme

### Statistics Cards
- **Total Sessions:** Blue (`bg-blue-50` border `border-blue-500`)
- **Average Score:** Green (`bg-green-50` border `border-green-500`)
- **Best Score:** Purple (`bg-purple-50` border `border-purple-500`)
- **Worst Score:** Red (`bg-red-50` border `border-red-500`)
- **Trend:** Purple (`bg-purple-50` border `border-purple-500`)

### Buttons
- **View Leaderboard:** Indigo (`bg-indigo-600` hover `bg-indigo-700`)
- **View Progress Graph:** Indigo (`bg-indigo-600`)
- **Back Buttons:** Gray (`bg-gray-600` hover `bg-gray-700`)
- **Home/Start:** Green (`bg-green-600` hover `bg-green-700`)

### Table
- **Header:** Blue background (`bg-blue-600`) with white text
- **Rows:** White with hover effect (`hover:bg-gray-100`)
- **Borders:** Gray (`border-gray-300`)

### Chart
- **Line:** Blue (`#3b82f6`)
- **Points:** Blue circles with white border
- **Grid:** Light gray with dashed lines
- **Background:** White

## Interactive Elements

### Leaderboard Table
- Hoverable rows show background change
- All data fields are read-only (no editing)
- Sessions sorted by most recent first
- Responsive layout on mobile devices

### Progress Graph
- Interactive data points show exact percentage on hover
- SVG rendering (scalable to any screen size)
- Responsive viewBox for different screen sizes
- Y-axis shows percentage scale (0-100%)
- X-axis shows session numbers

### Navigation
```
Results Page
    ↓ [View Leaderboard]
Leaderboard Page
    ↓ [View Progress Graph]
Progress Graph Page
    ↓ [Back to Leaderboard] or [Back to Home]
```

## Responsive Design

### Desktop (1024px+)
- Full-width tables and charts
- Grid layout for statistics (3-4 columns)
- Side-by-side buttons

### Tablet (768px - 1023px)
- Tables may wrap on narrow screens
- Grid layout for statistics (2-3 columns)
- Stacked buttons

### Mobile (< 768px)
- Single-column layout
- Grid layout for statistics (2 columns)
- Full-width buttons
- Touch-friendly sizes
- Horizontal scrolling for tables if needed

## Accessibility Features

### Color Contrast
- All text meets WCAG AA standards
- Statistics cards use distinct border colors for differentiation
- Chart elements use high-contrast blue

### Interactive Elements
- All buttons have clear hover states
- Focus states visible for keyboard navigation
- Button text clearly describes action

### Data Presentation
- Table headers clearly labeled
- Chart axes labeled
- Statistics cards clearly titled
- Date format human-readable

## Dark Mode Consideration (Future)

Current implementation uses light theme. For dark mode support:
- Invert colors (light backgrounds → dark)
- Adjust text colors for contrast
- Use inverted chart colors

## Print View

Pages are designed to be printable:
- Charts render as static SVG
- Tables print with proper formatting
- Page breaks handled by browser

## Mobile Touch Optimization

- Buttons are minimum 44px height for touch
- Spacing between interactive elements for easy tapping
- Horizontal scrolling for wide tables if needed
- Touch-friendly hover states

## Accessibility Attributes

### Semantic HTML
```html
<table> - For leaderboard table
<thead> - Table headers
<tbody> - Table data
<svg> - For chart
<div role="region"> - Landmark regions
```

### ARIA Labels (where applicable)
- Button descriptions for screen readers
- Chart title for context
- Table summary for complex data

---

## Example Color Values

| Element | Light | Hover | Border |
|---------|-------|-------|--------|
| Primary Button | `bg-indigo-600` | `bg-indigo-700` | N/A |
| Secondary Button | `bg-gray-600` | `bg-gray-700` | N/A |
| Blue Stat Card | `bg-blue-50` | N/A | `border-blue-500` |
| Green Stat Card | `bg-green-50` | N/A | `border-green-500` |
| Chart Line | `#3b82f6` | N/A | N/A |
| Table Header | `bg-blue-600` | N/A | N/A |
| Table Row Hover | `bg-white` | `hover:bg-gray-100` | N/A |

---

**Last Updated:** November 2025
**UI Version:** 1.0
**Framework:** Tailwind CSS + Vanilla JavaScript
