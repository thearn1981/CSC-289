```markdown
# Design System Document: The Kinetic Fairway

## 1. Overview & Creative North Star
**Creative North Star: "The Tactile Playground"**

This design system moves away from the sterile, data-heavy look of traditional sports trackers and embraces the vibrant, physical joy of mini-golf. We are building an experience that feels as bouncy as a golf ball and as fresh as a manicured green. 

To achieve a premium "Editorial" feel, we reject the rigid, boxy grid. Instead, we utilize **intentional asymmetry**, **overlapping "floating" layers**, and **extreme corner radii** to mimic the winding paths of a putt-putt course. We prioritize sunlight-legibility and "fat-finger" touch targets, ensuring the UI is a companion to the game, not a distraction.

---

## 2. Colors & Surface Soul

The palette is rooted in a lush, organic green, punctuated by high-energy "Pop" colors for player identification.

### The "No-Line" Rule
**Borders are strictly prohibited for sectioning.** We define space through "Tonal Shifts." To separate a scorecard from the header, do not draw a line; instead, transition from `surface` to `surface-container-low`. Boundaries are felt through color-blocking, not outlines.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of acrylic and turf. 
*   **Base Level:** `surface` (#f5f7f5) – The "ground" of your app.
*   **The Course Map:** `surface-container` (#e6e9e7) – Used for large instructional areas.
*   **Active Player Cards:** `surface-container-lowest` (#ffffff) – These sit on top of the green to provide maximum contrast and a "lifted" feel.

### The "Glass & Gradient" Rule
To inject "soul," use subtle 15-degree linear gradients on primary CTAs, transitioning from `primary` (#006a28) to `primary-container` (#5cfd80). For overlays (like a hole-in-one celebration), use **Glassmorphism**: 
*   **Fill:** `surface_container_lowest` at 70% opacity.
*   **Effect:** Backdrop-blur (16px to 24px).
*   **Result:** The "Grass Green" glows through the card, making the UI feel integrated into the environment.

---

## 3. Typography: The Outdoor Boldness

We use **Plus Jakarta Sans** for its geometric clarity and playful energy. 

*   **Display (The Score):** `display-lg` (3.5rem). Use this for the current stroke count. It should be bold and impossible to miss in high-glare outdoor environments.
*   **Headlines (The Hole):** `headline-lg` (2rem). Used for "Hole 14" or "Leaderboard." These are the anchors of the layout.
*   **Body (Instructions):** `body-lg` (1rem). High-contrast `on-surface` (#2c2f2e) ensures readability while walking between obstacles.
*   **Labels (Player Names):** `label-md` (0.75rem). Always uppercase with +5% letter spacing to provide an authoritative, "official tournament" feel.

---

## 4. Elevation & Depth: Tonal Layering

Traditional drop shadows are too "software-standard." We use **Ambient Depth**.

*   **The Layering Principle:** Instead of a shadow, place a `surface-container-highest` element behind a `surface-container-lowest` element. The 4-step jump in lightness creates a natural, clean separation.
*   **Ambient Shadows:** If a floating action button (FAB) requires a shadow, use a blur of 32px and an opacity of 6% using a tinted shadow: `rgba(0, 72, 25, 0.06)`. This creates a soft, mossy glow rather than a harsh grey smudge.
*   **The "Ghost Border":** If a player’s color (e.g., `tertiary`) is too close to the background, use a 1px border of `outline-variant` at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### The "Pebble" Buttons
*   **Primary:** Uses `primary` background with `on-primary` text. Shape: `rounded-full` (9999px). The "pill" shape mimics the curvature of the ball.
*   **Secondary:** `secondary-container` background. Use this for "Add Player" or "View Map."
*   **Interaction:** On press, the button should scale down to 0.95 and increase the `surface-tint` intensity.

### Score Input Chips
*   Forbid the standard "Input Field." Instead, use **Action Chips** in a horizontal carousel.
*   **State:** Unselected chips use `surface-container-high`. The selected score chip scales up and uses `primary-container` with a `primary` label.

### Scorecards (Cards & Lists)
*   **Rule:** No dividers. 
*   Use **Vertical Breathing Room**. A player row is separated from the next by 16dp of `surface` space. 
*   The leading element (Player Avatar) should use the player’s assigned vibrant accent (`secondary` for Player 1, `tertiary` for Player 2).

### The "Pulse" Progress Bar
*   Used for tracking progress through the 18 holes. 
*   A thick, 12dp track using `surface-container-highest` with a rounded `primary` fill that has a subtle inner glow.

---

## 6. Do’s and Don’ts

### Do:
*   **Do** use asymmetrical layouts. Let the "Current Hole" card bleed off the right edge of the screen slightly to suggest momentum.
*   **Do** use `rounded-xl` (3rem) for large containers to maintain the "playful" brand identity.
*   **Do** utilize the `tertiary` (#0055c4) blue for "Water Hazard" or "Reset" actions—it provides a cool contrast to the warm greens.

### Don’t:
*   **Don't** use 1px solid black or grey lines. This kills the "premium" feel immediately.
*   **Don't** use standard Material Design square corners. Every corner must have a minimum radius of `sm` (0.5rem).
*   **Don't** crowd the UI. Mini-golf is played outdoors; give every element a 24dp "safety zone" to prevent accidental taps while moving.

---

## 7. Designer's Note on Polish
When designing the leaderboard, don't just list names. Use a staggered layout where the #1 spot is 20% larger than #2 and #3. Use `secondary-fixed` (#ffc5aa) to highlight the winner, creating a "sunset glow" effect that feels like the end of a perfect day on the course.```