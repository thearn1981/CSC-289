# AI-Assisted Wireframing Prompt Log

**CSC-289: Programming Capstone Project**
**Student Name**: Teresa Hearn
**Date**: 04/14/2026

---

## Purpose

This log documents your AI collaboration process during wireframe creation. In CSC-289, you're expected to work WITH AI tools (just like you use Claude Code for development) while maintaining critical thinking and ownership of your design decisions.

**Required**: You must submit this completed prompt log with your wireframe deliverables (Part 1 submission).

**Grading Weight**: 10 points (part of "Annotations & Documentation" rubric category)

---

## Instructions

For each user story you wireframe, document:
1. **Initial Prompts**: What you asked the AI to help with
2. **AI Responses**: Key suggestions or outputs the AI provided
3. **Your Evaluation**: What you accepted, rejected, or modified and WHY
4. **Iterations**: How you refined your prompts to get better results
5. **Final Decisions**: Your ultimate design choices and rationale

**Remember**: The goal is NOT to have AI design everything for you—it's to use AI as a brainstorming partner while YOU make the final design decisions.

---


### Initial Context Prompt

**What I asked the AI**:
```
i need a user story for a putt putt player who wants instead of a paper tally a app that for each hole has what par it is and up to 6 players can be added and the scores added as they go .. also telling those who are not fimilar with the rules the order the putter should go next based on the previous putts
```

**AI Tool Used**: ☑ ChatGPT  ☐ Claude  ☐ Google Gemini  ☐ Other: ___________

---

### AI Response Summary

**Key suggestions the AI provided**:
```
It gave a me user story that did all the things i asked for the putt putt players

Example:

User Story
As a putt-putt player, I want an app that shows the par for each hole, lets me add up to 6 players, and allows scores to be entered as we play, so that I can keep track of the game without using a paper scorecard. I also want the app to explain whose turn is next based on the previous hole’s results, so players who do not know the rules can still play in the correct order.```

---

### Critical Evaluation

**What I accepted and WHY**:
```
[Explain which suggestions you implemented and your reasoning]
Example:
- I liked what it came up with and it was very helpful.
```

**What I rejected or modified and WHY**:
```
Instead of one user story with lots of things I decided to get it broken down into smaller user stories

```

---

### Prompt Iterations

**Follow-up prompts I used to refine the design**:

**Iteration 1**:
```
can we break t hat into 3 user stories?

```

**AI Response**:
```
Instead of one big user story it was broken up into 3 user stories 
```

**Iteration 2**:
```
can you save it in a .md
```
**AI Response**:

it was saved so i could add it to github.
---

### Layout & Component Decisions

**Specific prompts about wireframe components**:

**Prompt**:
```
Example: "What information should be visible on each project card without requiring
the user to click through?"
```

**AI Suggestions**:
```
Example: Project name, course code, status, last updated, quick action buttons
```

**My Decision**:
```
Example: Included all suggested items EXCEPT course code (redundant if filtered by course).
Added a small thumbnail/icon for visual interest.
```

---

### Design Pattern Research

**Prompts used to explore UI patterns**:
```
Example: "What are common patterns for displaying progress indicators in dashboard interfaces?"
Example: "Show me examples of effective status badge designs"
```

**How this influenced my design**:
```
[Explain how AI research shaped your wireframe]
```

---

### Final Design Rationale

**Why my final wireframe looks the way it does**:
```
[Comprehensive explanation of your design decisions - this should be YOUR thinking,
informed by AI but not dictated by it]

Example:
I designed the dashboard with a 3-column grid layout on desktop (2 columns on tablet,
1 on mobile) because:
1. The AI suggested cards, which I validated against real dashboards (GitHub, Trello)
2. I rejected the AI's sidebar idea after considering that users need maximum screen
   space for project cards
3. I added a summary statistics section at the top (not AI-suggested) because users
   need at-a-glance progress awareness
4. Status indicators use icon + color + text label (AI-suggested) for accessibility
```

---

## User Story #1: ## 🧍 User Story 1 – Player Setup
As a putt-putt player, I want to add up to 6 players before the game starts so that everyone in my group can be included in the score tracking.

### ✅ Acceptance Criteria
- User can add between 1 and 6 players
- Each player has a two letter initial

### Initial Context Prompt

**What I asked the AI**:
```
I asked it to give me something like this:
User Story 1 – Player Setup
As a putt-putt player, I want to add up to 6 players before the game starts so that everyone in my group can be included in the score tracking.
- User can add between 1 and 6 players
- Each player has a two letter initial
```

**AI Tool Used**: ChatGPT  

---

### AI Response Summary

**Key suggestions the AI provided**:
```
It gave me a setup screen that felt more like for golf then putt putt.  

```

---

### Critical Evaluation

**What I accepted and WHY**:
```
the label for the players was good.
```

**What I rejected or modified and WHY**:
```
it added a handicap mode for auto levels scores based on previous performance.
```

---

### Prompt Iterations

**Follow-up prompts I used to refine the design**:

**Iteration 1**:
```
I want it to be more fun its putt putt
```

**AI Response**:
```
I've redesigned the Player Setup screen to embrace the "Putt Putt Adventures" spirit!

I went with a "Character Selection" vibe to make it feel more like a game right from the start. Each player now feels like a hero joining the quest, and I've used the high-energy colors and rounded forms of the Neon Fairway system to keep things fun and inviting.
```

---

### Final Design Rationale

**Why my final wireframe looks the way it does**:
```
I wanted it to feel more fun like most putt putt courses are some sort of different adventures you must get your ball through.
Had to adjust the size of the hero setup to accommadate up to 6 players.

```

---

## User Story #2: Score Tracking
As a putt-putt player, I want to see the par for each hole and enter scores as we play so that I can keep track of the game without using a paper scorecard.

### ✅ Acceptance Criteria
- each course can have up to 18 holes 
- Each hole displays its par
- User can enter scores for each player per hole
- Scores are saved as the game progresses
- The app shows a running total for each player

### Initial Context Prompt

 next: 
As a putt-putt player, I want to see the par for each hole and enter scores as we play so that I can keep track of the game without using a paper scorecard.
- each course can have up to 18 holes 
- Each hole displays its par
- User can enter scores for each player per hole
- Scores are saved as the game progresses
```

```

**AI Tool Used**: ChatGPT  
---

### AI Response Summary

**Key suggestions the AI provided**:
```
It generated a wireframe a hole showing the name and then progress of course as well as the players name and score


```

---

### Critical Evaluation

**What I accepted and WHY**:
```
It looked like it was on a good track of keeping the score as i would like.
```

**What I rejected or modified and WHY**:
```
the bubbles were to big and would of lead to much scrolling.
```

---

### Prompt Iterations

**Follow-up prompts I used to refine the design**:

**Iteration 1**:
```
the bubbles for each player are to big for up to 6 players
```

**AI Response**:
```
I've updated the scorecard to be more compact, making it much easier to track scores for a full group of up to 6 players.

I've moved to a horizontal row layout for each player, which significantly reduces the vertical space each one takes up while keeping the buttons large enough for easy tapping. This ensures the "Compact Adventure Scorecard" stays fun and functional even with a big group!
```

---

### Final Design Rationale

**Why my final wireframe looks the way it does**:
```
It fits all 6 players on one screen no scrolling its easy to add points.
```

---

## Google Stitch + AI Integration

### Using AI to Learn Google Stitch

**Prompts I used to learn Google Stitch features**:
```
Example: "How do I add annotations to wireframes in Google Stitch?"
Example: "What's the best way to show interaction flows in Google Stitch?"
```

**Most helpful AI guidance about the tool**:
```
It helped alot in the iteration of the prompts to finally get me close to what i was looking for.
```

---

## Reflection on AI-Assisted Design Process

### What Worked Well

```
It gave you a way of visualizing how the wireframe would look and tweak it so that 
it looks close to what you had in mind.
- I was able to quickly explore different layout options and narrow down which one
would work best and limit the scrolling for the user.

```

### What Was Challenging

```
The initial verison was sometimes out there and there were a few iteration prompts
that needed to be made to get it closer to what you had in mind.

- the bubbles for the name were always to big making it where the user would have to scroll.
- Needed multiple iterations to get specific enough answers
```

### How AI Influenced My Final Designs

```
Actually seeing something on the screen helped in deciding if it would look ok or needed to be
tweaked more. 

AI provided about 40% of initial ideas, but I modified/rejected about half of those.

```

---

## Prompt Engineering Lessons Learned

**Best prompts I wrote** (that got the most useful responses):
```
1. bubbles need to be smaller for players.
2. [Example of an effective prompt]
3. [Example of an effective prompt]
```

**Ineffective prompts** (that I had to refine):
```
1. ## 🧍 User Story 1 – Player Setup
As a putt-putt player, I want to add up to 6 players before the game starts so that everyone in my group can be included in the score tracking.

### ✅ Acceptance Criteria
- User can add between 1 and 6 players
- Each player has a two letter initial
   - Why it failed: needed to be more specific as what i was looking for
   - How I improved it: added a prompt that said needed to be smaller  bubbles for up to 6 players so less scrolling.
```

---

## Self-Assessment

### AI Collaboration Documentation Quality

Rate your prompt log documentation (1-5 scale):

- **Completeness**: Did I document all significant AI interactions?
  - ☐ 1 (Minimal) ☐ 2 ☑3 (Adequate) ☐ 4 ☐ 5 (Comprehensive)

- **Critical Thinking**: Did I evaluate AI suggestions rather than blindly accepting them?
  - ☐ 1 (Minimal) ☐ 2 ☑ 3 (Adequate) ☐ 4 ☐ 5 (Strong evaluation)

- **Prompt Quality**: Did I use effective, specific prompts?
  - ☐ 1 (Minimal) ☑ 2 ☐ 3 (Adequate) ☐ 4 ☐ 5 (Well-crafted)

- **Design Ownership**: Are my final designs MY work (informed by but not dictated by AI)?
  - ☐ 1 (Minimal) ☐ 2 ☑ 3 (Adequate) ☐ 4 ☐ 5 (Strong ownership)

---

## Submission Checklist

Before submitting your prompt log:

- [ ] Documented prompts for all 3 user stories
- [ ] Included both initial and iteration prompts
- [ ] Explained what I accepted vs. rejected from AI suggestions
- [ ] Provided clear design rationale grounded in MY thinking
- [ ] Reflected on AI collaboration process honestly
- [ ] Completed self-assessment section
- [ ] Proofread for clarity and completeness

---

**Instructor Use Only**

| Criterion | Points | Notes |
|-----------|--------|-------|
| Prompt documentation completeness | __/3 | |
| Critical evaluation of AI suggestions | __/3 | |
| Design rationale clarity | __/2 | |
| Reflection quality | __/2 | |
| **Total** | __/10 | |

---

## Tips for Effective AI-Assisted Wireframing

1. **Start with context**: Give AI the full user story + acceptance criteria
2. **Ask for principles, not solutions**: "What makes a good dashboard?" vs. "Design my dashboard"
3. **Iterate iteratively**: Refine prompts based on initial responses
4. **Always evaluate**: Don't accept AI suggestions without considering alternatives
5. **Document as you go**: Don't try to recreate your AI conversations after the fact
6. **Own your decisions**: AI can inform, but YOU are the designer

---

**Questions about AI-assisted design or prompt documentation?**
Post in the Canvas discussion or attend office hours.
