# 🎯 Putt-Putt Score Tracker – User Stories

---

## 🧍 User Story 1 – Player Setup
As a putt-putt player, I want to add up to 6 players before the game starts so that everyone in my group can be included in the score tracking.

### ✅ Acceptance Criteria
- User can add between 1 and 6 players
- Each player has a two letter initial


---

## ⛳ User Story 2 – Score Tracking
As a putt-putt player, I want to see the par for each hole and enter scores as we play so that I can keep track of the game without using a paper scorecard.

### ✅ Acceptance Criteria
- each course can have up to 18 holes 
- Each hole displays its par
- User can enter scores for each player per hole
- Scores are saved as the game progresses
- The app shows a running total for each player

---

## 🔄 User Story 3 – Turn Order Guidance
As a putt-putt player, I want the app to show who goes next based on previous hole results so that players who are not familiar with the rules can still play in the correct order.

### ✅ Acceptance Criteria
- The app determines turn order after each hole
- The player with the best score goes first on the next hole
- The app clearly displays whose turn is next
- The app includes a simple explanation of how turn order works

---

## 🗺️ User Story 4 – Course Setup & Save

As a putt-putt player, I want to enter the number of holes and the par for each hole and save that course so that I do not have to re-enter the information every time I play.

### ✅ Acceptance Criteria
- User can enter the total number of holes for a course
- User can input the par value for each hole
- User can name and save the course
- Saved courses can be selected for future games
- Course data persists (saved locally or in database)
- User can view a list of previously saved courses

---

## 🏆 User Story 5 – Final Score Ranking

As a putt-putt player, I want to see all player scores ranked in order after the last hole so that I can easily determine the winner and final standings.

### ✅ Acceptance Criteria
- The app displays all players after the final hole is completed
- Players are sorted by lowest total score (best score first)
- The winner is clearly highlighted
- Ties are handled correctly (players with same score share position)
- Each player’s total score is displayed