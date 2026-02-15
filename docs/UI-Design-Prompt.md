# FaceMax UI Design Prompt
## For AI Designer Agent

---

## Design Philosophy

Create a **premium, masculine fitness app aesthetic** with dark mode as the default. The design should feel:
- **Elite and exclusive** (like a high-end gym or luxury wellness app)
- **Scientific and trustworthy** (clean lines, precise measurements)
- **Motivational but not aggressive** (encouraging tone without toxic masculinity tropes)
- **Modern and tech-forward** (AI-powered features should feel futuristic)

The visual language draws from apps like Oura Ring, Whoop, and Calm—but with a distinctly masculine energy more aligned with fitness apps like Freeletics or Centr.

---

## Color System

### Primary Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-primary` | `#0A0E14` | Main background, deepest layer |
| `--bg-secondary` | `#141B24` | Card backgrounds, elevated surfaces |
| `--bg-tertiary` | `#1E2732` | Input fields, subtle containers |
| `--surface-hover` | `#2A3542` | Hover states, pressed states |

### Accent Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--accent-primary` | `#00D4AA` | Success states, progress indicators, CTA highlights |
| `--accent-secondary` | `#0EA5E9` | AI elements, chat bubbles, informational highlights |
| `--accent-energy` | `#F59E0B` | Streaks, points, achievements, fire icons |
| `--accent-caution` | `#EF4444` | Errors, warnings, missed days |
| `--accent-purple` | `#8B5CF6` | Premium features, exclusive content |

### Text Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--text-primary` | `#FFFFFF` | Headlines, primary text |
| `--text-secondary` | `#94A3B8` | Body text, descriptions |
| `--text-tertiary` | `#64748B` | Timestamps, metadata, hints |
| `--text-inverse` | `#0A0E14` | Text on light/colored backgrounds |

### Semantic Colors
- Success: `#10B981` (green)
- Warning: `#F59E0B` (orange)
- Error: `#EF4444` (red)
- Info: `#0EA5E9` (blue)

---

## Typography System

### Font Family
- **Primary**: `Inter` or `SF Pro Display` (system font)
- **Monospace**: `SF Mono` or `JetBrains Mono` (for numbers, stats)

### Type Scale

| Style | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|--------|-------------|----------------|-------|
| **Display** | 40px | 700 (Bold) | 1.1 | -0.02em | Welcome headlines, large numbers |
| **H1** | 32px | 700 (Bold) | 1.2 | -0.01em | Screen titles |
| **H2** | 24px | 600 (Semibold) | 1.3 | 0 | Section headers |
| **H3** | 20px | 600 (Semibold) | 1.4 | 0 | Card titles |
| **H4** | 18px | 600 (Semibold) | 1.4 | 0 | Subsection titles |
| **Body Large** | 17px | 400 (Regular) | 1.5 | 0 | Primary body text |
| **Body** | 15px | 400 (Regular) | 1.5 | 0 | Standard text |
| **Body Small** | 13px | 400 (Regular) | 1.5 | 0 | Descriptions, captions |
| **Caption** | 12px | 500 (Medium) | 1.4 | 0.02em | Labels, timestamps |
| **Overline** | 11px | 600 (Semibold) | 1.2 | 0.08em | Categories, badges (uppercase) |
| **Button** | 16px | 600 (Semibold) | 1 | 0.02em | Button text |
| **Stat Number** | 48px | 700 (Bold) | 1 | -0.03em | Large statistics (monospace) |

---

## Spacing System

### Base Unit: 4px

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | 4px | Icon padding, tight gaps |
| `space-2` | 8px | Inline spacing, small gaps |
| `space-3` | 12px | Compact padding |
| `space-4` | 16px | Standard padding, card gaps |
| `space-5` | 20px | Section padding |
| `space-6` | 24px | Large gaps, section breaks |
| `space-8` | 32px | Major section spacing |
| `space-10` | 40px | Screen edge padding |
| `space-12` | 48px | Hero section padding |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | 8px | Small buttons, tags |
| `radius-md` | 12px | Cards, inputs |
| `radius-lg` | 16px | Large cards, modals |
| `radius-xl` | 24px | Bottom sheets, hero cards |
| `radius-full` | 9999px | Pills, avatars, circular buttons |

---

## Component Specifications

### Buttons

#### Primary Button
- Background: `--accent-primary` (#00D4AA)
- Text: `--text-inverse` (#0A0E14)
- Height: 56px
- Border Radius: `radius-full` (pill shape)
- Font: Button style (16px, semibold)
- Icon: Optional, left-aligned, 20px size
- Shadow: `0 4px 14px rgba(0, 212, 170, 0.4)`
- Pressed State: Scale to 0.98, darken background 10%

#### Secondary Button
- Background: `--bg-tertiary` (#1E2732)
- Text: `--text-primary` (#FFFFFF)
- Border: 1px solid `--surface-hover`
- Height: 56px
- Border Radius: `radius-full`

#### Tertiary Button (Ghost)
- Background: Transparent
- Text: `--accent-primary`
- Height: 48px
- Border Radius: `radius-md`

#### Icon Button
- Size: 48px x 48px
- Background: `--bg-secondary`
- Icon: 24px, `--text-primary`
- Border Radius: `radius-full`

### Cards

#### Standard Card
- Background: `--bg-secondary` (#141B24)
- Border Radius: `radius-lg` (16px)
- Padding: `space-5` (20px)
- Border: 1px solid rgba(255,255,255,0.05)

#### Exercise Card
- Background: `--bg-secondary`
- Border Radius: `radius-lg`
- Padding: `space-4` (16px)
- Layout: Horizontal
  - Left: Exercise thumbnail (80x80px, `radius-md`)
  - Middle: Title (H4) + Duration caption + Progress indicator
  - Right: Status icon (checkmark or play)

#### Progress Card
- Background: Gradient from `--bg-secondary` to `--bg-tertiary`
- Border Radius: `radius-xl` (24px)
- Padding: `space-6` (24px)
- Contains: Large stat number, label, mini chart

### Input Fields

#### Text Input
- Background: `--bg-tertiary` (#1E2732)
- Border: 1px solid transparent
- Border Radius: `radius-md` (12px)
- Height: 52px
- Padding: 0 `space-4`
- Font: Body Large (17px)
- Placeholder: `--text-tertiary`
- Focus: Border color `--accent-primary`

#### Chat Input
- Background: `--bg-tertiary`
- Border Radius: `radius-full`
- Height: 48px
- Right side: Send button (circular, `--accent-primary`)
- Left side: Attachment icon

### Progress Indicators

#### Circular Progress
- Size: 64px
- Stroke Width: 4px
- Background Track: `--bg-tertiary`
- Progress Color: `--accent-primary`
- Center: Percentage text (Caption style)

#### Linear Progress
- Height: 6px
- Border Radius: `radius-full`
- Background Track: `--bg-tertiary`
- Progress: Gradient from `--accent-primary` to `--accent-secondary`

#### Streak Indicator
- Icon: Flame icon (🔥) in `--accent-energy`
- Number: Display style (40px), `--accent-energy`
- Label: "day streak" in `--text-secondary`

### Badges

#### Tier Badge
- Free: Gray background, "FREE" text
- Basic: `--accent-primary` background, "BASIC" text
- Premium: `--accent-purple` background, "PRO" text
- Border Radius: `radius-sm`
- Padding: 4px 10px
- Font: Overline style

#### Achievement Badge
- Circular: 32px diameter
- Background: Gradient
- Icon: Centered, 16px

---

## Screen Specifications

### 1. Splash / Launch Screen

**Layout:**
- Full screen `--bg-primary`
- Center: App logo (stylized "FM" monogram or face silhouette)
- Logo animation: Subtle pulse or glow effect
- Below logo: "FaceMax" wordmark (H1, white)
- Tagline: "Unlock Your Potential" (Body, `--text-secondary`)
- Bottom: Loading indicator (dots or spinner in `--accent-primary`)

**Requirements:**
- Duration: 2-3 seconds
- Transition: Fade to onboarding or main app

---

### 2. Onboarding - Chat Interface

**Layout:**
- Full screen chat interface (like iMessage or WhatsApp)
- Background: `--bg-primary`
- Top: Minimal header with back button (if not first screen) and progress dots
- Main area: Scrollable chat history
- Bottom: Input area fixed at bottom

**Chat Bubble - Agent:**
- Background: `--bg-secondary`
- Text: `--text-primary`
- Border Radius: 16px top-left, 16px top-right, 16px bottom-right, 4px bottom-left
- Padding: 12px 16px
- Max Width: 80%
- Left-aligned
- Avatar: Small circular agent icon (left of bubble)

**Chat Bubble - User:**
- Background: `--accent-primary`
- Text: `--text-inverse`
- Border Radius: 16px top-left, 16px top-right, 4px bottom-left, 16px bottom-right
- Padding: 12px 16px
- Max Width: 80%
- Right-aligned

**Input Area:**
- Background: `--bg-secondary` with top border
- Padding: 12px 16px
- Text input: `--bg-tertiary`, rounded, placeholder "Type or hold to speak..."
- Voice button: Microphone icon, circular, `--accent-secondary`
- Send button: Arrow icon, appears when text entered

**Quick Reply Options:**
- Horizontal scrollable row above input
- Pills with `--bg-tertiary` background
- Text: `--text-primary`
- Selected state: `--accent-primary` background

**Special Messages:**
- Photo request: Show camera icon with "Tap to upload" area
- Date/Height selectors: Inline picker wheels or dropdowns
- Success states: Green checkmark animation

---

### 3. AI Video Generation Screen

**Layout:**
- Full screen `--bg-primary`
- Center: Large video preview container (16:9 aspect ratio)
- Video container: `--bg-secondary` background with `radius-lg`
- While generating: Loading spinner with "Creating your future self..." text
- Progress bar below video

**After Generation:**
- Video auto-plays (muted, looping)
- Below video: "This could be you in 90 days" (H3, center)
- Subtext: "Follow your daily routine to make it real" (Body, `--text-secondary`)
- Primary CTA: "Start My Journey" (full width, bottom)
- Secondary: "Replay" button

**Background Effect:**
- Subtle gradient glow behind video using `--accent-primary` at 20% opacity
- Animated particles or subtle motion

---

### 4. Main App - Routine Tab (Home)

**Header:**
- Height: 120px
- Background: Gradient from `--bg-primary` to `--bg-secondary`
- Left: Greeting "Good morning, [Name]" (H3)
- Right: Settings icon button (top left area actually - see nav)
- Below greeting: Date and streak indicator
  - Flame icon + number + "day streak"

**Daily Progress Card:**
- Full width, `--bg-secondary`
- Border Radius: `radius-xl`
- Padding: 24px
- Top row: "Today's Progress" (H4) + percentage complete
- Progress bar: Linear, showing 3/5 or 5/10 exercises complete
- Bottom: Estimated time remaining

**Exercises List:**
- Vertical scrollable list
- Gap between items: 12px
- Each Exercise Card:
  - Background: `--bg-secondary` (or `--bg-tertiary` if completed)
  - Height: ~100px
  - Left: Thumbnail image (exercise preview, 80x80, `radius-md`)
  - Middle:
    - Exercise name (H4)
    - Duration + difficulty (Caption, `--text-secondary`)
    - If completed: Green checkmark + "Completed" text
  - Right:
    - Play icon (circular button) if not started
    - Checkmark in circle if completed

**Next Session Timer:**
- Fixed card at bottom if all exercises complete
- Background: `--bg-tertiary`
- Text: "Next session in 14:32:18" (monospace numbers)

**Floating Action:**
- If mid-routine: "Continue Routine" floating button at bottom

---

### 5. Exercise Detail / Recording Screen

**Header:**
- Transparent background
- Left: Back arrow
- Center: Exercise name (H4)
- Right: Info icon (shows instructions modal)

**Video Preview Area:**
- Takes up top 60% of screen
- Shows exercise demonstration video (auto-playing, muted, looping)
- Overlay: "Watch first, then practice" badge

**Instructions Section:**
- Background: `--bg-secondary`
- Border Radius: `radius-xl` (top corners only, sheet style)
- Padding: 24px
- Pull handle at top (centered line)
- Steps list:
  - Numbered items (1, 2, 3...)
  - Each: Step title (H4) + description (Body)
  - Icons for each step

**CTA:**
- Fixed at bottom
- "Start Recording" button (Primary, full width)
- Height: 80px from bottom edge

---

### 6. Camera / Recording Screen

**Camera View:**
- Full screen camera feed
- Overlay: Semi-transparent guide frame
  - Rectangular outline showing where face should be
  - Corner brackets at each corner
  - Color: `--accent-primary` at 60% opacity

**Top Bar (overlay on camera):**
- Left: Close/X button
- Center: Exercise name + timer
- Right: Flip camera button

**Timer Display:**
- Large numbers in center-top
- Format: "03:45" (minutes:seconds)
- Font: Monospace, 48px, white with dark shadow

**AI Feedback Area:**
- Bottom third of screen
- Chat bubble style messages appearing
- Background: Semi-transparent `--bg-secondary`
- Text: Tips like "Move slightly to the left" or "Great form!"
- Disappears after 3 seconds

**Recording Controls:**
- Bottom center: Large circular record button
  - Idle: Red circle outline, 80px diameter
  - Recording: Solid red with pulse animation
- Bottom left: Timer toggle
- Bottom right: Flash toggle

**Recording Complete:**
- Modal slides up
- Preview thumbnail of recording
- Options: Retake, Save, Play

---

### 7. Track Tab (Progress)

**Header:**
- "Your Progress" (H2)
- Date range selector (This Week | This Month | All Time)

**Stats Grid:**
- 2x2 grid of stat cards
- Each card:
  - Background: `--bg-secondary`
  - Border Radius: `radius-lg`
  - Icon top-left (small, colored)
  - Large number center (Stat Number style)
  - Label bottom (Caption)
- Stats to show:
  - Total exercises completed
  - Current streak
  - Days tracked
  - Points earned

**Progress Chart:**
- Full width card
- Background: `--bg-secondary`
- Title: "Exercise Consistency" (H4)
- Line chart showing last 7 days
- X-axis: Days (Mon, Tue...)
- Y-axis: Exercises completed
- Line color: `--accent-primary`
- Fill: Gradient fade below line

**Measurements Section:**
- Collapsible cards for each measurement:
  - Face symmetry score
  - Jawline definition
  - Weight (if tracked)
- Each shows:
  - Current value
  - Change from last week (green/red indicator)
  - Mini sparkline

**Gallery Preview:**
- Horizontal scroll of recent video thumbnails
- "View All" link to full gallery

---

### 8. Gallery Screen

**Header:**
- Back button
- "Your Recordings" (H2)
- Filter icon (right)

**Filter Options:**
- Horizontal scroll pills
- All | Week 1 | Week 2 | By Exercise Type

**Video Grid:**
- 2-column grid
- Gap: 12px
- Each cell:
  - Aspect ratio: 9:16 (vertical video thumbnail)
  - Border Radius: `radius-md`
  - Overlay: Play icon centered
  - Bottom overlay: Date + exercise name
  - Duration badge (top right)

**Video Player (Modal):**
- Full screen modal
- Vertical video centered
- Background: Black
- Controls: Play/pause, scrubber, close

---

### 9. Chat Tab (AI Coach)

**Header:**
- "FaceMax Coach" (H2)
- Right: Info icon (explains AI capabilities)
- Below: Status indicator "Online" with green dot

**Chat History:**
- Same bubble style as onboarding
- Agent avatar: Professional but friendly male face or abstract AI icon
- Agent name: "Max" above first message in group
- Timestamp below each message (Caption style)

**Image Messages:**
- User can upload photos
- Show as preview thumbnail in chat
- Tap to expand

**Quick Actions:**
- Horizontal scroll above input
- Suggestions like:
  - "Analyze my progress"
  - "Today's routine tips"
  - "Form check help"

**Input Area:**
- Same as onboarding
- Plus: Camera icon for quick photo upload
- Send button activates when text present

**Typing Indicator:**
- Three dots animation when AI is responding
- "Max is typing..." text

---

### 10. Weekly Analysis Screen

**Header:**
- "Week 4 Analysis" (H2)
- Date range subtitle

**Overall Score Card:**
- Large circular progress in center
- Score out of 100
- Text: "Great progress!" or similar based on score
- Background: Gradient card

**Comparison Section:**
- Side-by-side images (Before | After)
- Labels below each
- Slider to compare (optional)

**Breakdown List:**
- Each metric as a row:
  - Metric name (left)
  - Progress bar (center)
  - Score/change (right)
- Metrics:
  - Face Symmetry
  - Jawline Definition
  - Cheekbone Prominence
  - Skin Clarity
  - Overall Balance

**AI Insights:**
- Quote-style card with agent avatar
- 2-3 sentences of personalized feedback
- Background: `--bg-tertiary`

**CTA:**
- "View Full Report" button
- Share button (optional)

---

### 11. Social Tab

**Segmented Control (Top):**
- Leaderboard | Forum | Discover
- Style: Pill selector, `--bg-secondary` background

#### Leaderboard View

**Your Rank Card:**
- Full width, highlighted background (`--accent-primary` at 10%)
- Shows: Your avatar, rank number, name, points
- "You're in top 15%" badge

**Top 3 Podium:**
- Visual podium graphic
- 1st place: Center, tallest, gold accent
- 2nd place: Left, silver
- 3rd place: Right, bronze
- Shows avatar, name, points for each

**Ranking List:**
- Below podium
- Vertical list
- Each row:
  - Rank number
  - Avatar (40px circle)
  - Name + tier badge
  - Points (right aligned, monospace)
- Highlight current user row

#### Forum View

**Create Post Button:**
- Floating button or top right
- "+ New Discussion"

**Post List:**
- Card-based layout
- Each post card:
  - Author row: Avatar + name + time
  - Title (H4)
  - Preview text (2 lines, truncated)
  - Bottom row: Upvote count + comment count + share
- Upvote button: Arrow up icon, number below

**Post Detail (Tap to open):**
- Full post content
- Comment section below
- Nested replies (threaded)
- Input at bottom for commenting

#### Discover View (Doomscrolling)

**Video Feed:**
- Vertical scroll (TikTok style)
- Each video:
  - Full screen video (9:16)
  - Overlay gradient at bottom for text readability
  - Creator name + description
  - Like button (heart icon)
  - Save button
  - Share button
- Swipe up for next video

**Caught Up State:**
- When all new videos viewed
- Icon: Checkmark in circle
- Text: "You're all caught up!"
- Subtext: "You've seen all new content. Keep scrolling for previous days."

---

### 12. Shop Tab (Coming Soon)

**Placeholder Design:**
- Large illustration (face tools, products)
- Heading: "Shop Coming Soon" (H2)
- Subtext: "We're curating the best products for your face maxing journey"
- Email input: "Get notified when we launch"
- Submit button
- Preview categories below (non-clickable):
  - Gua Sha Tools
  - Mastic Gum
  - Skincare
  - Supplements

---

### 13. Account / Settings

**Header:**
- "Account" (H2)

**Profile Card:**
- Avatar (large, 80px)
- Name (H3)
- Email (Body, `--text-secondary`)
- Tier badge below

**Menu List:**
- Standard iOS-style settings list
- Each row:
  - Icon (left, 24px, colored)
  - Label (Body Large)
  - Value or chevron (right)
- Sections:
  - Profile Settings
  - Subscription (show current plan)
  - Gallery
  - Notifications
  - Privacy & Security
  - Help & Support
  - About

**Subscription Row:**
- Special highlight
- Show: Current plan name
- "Manage" button if active

---

### 14. Paywall / Upgrade Screen

**Hero Section:**
- Large illustration or animated graphic
- "Unlock Your Full Potential" (Display style)
- Subtext explaining premium benefits

**Pricing Cards:**
- Side by side or stacked
- Monthly vs Annual (annual has "Save 20%" badge)
- Price large (₹500/month)
- Feature list with checkmarks

**Feature Comparison:**
- Table showing Free vs Basic
- Checkmarks and X marks
- Sticky CTA at bottom

**CTA:**
- "Upgrade Now" primary button
- "Restore Purchases" link below
- "Maybe Later" close button

---

## Animation Specifications

### Micro-interactions

#### Button Press
- Duration: 100ms
- Scale: 1.0 → 0.97 → 1.0
- Easing: ease-out

#### Card Tap
- Duration: 150ms
- Background: Lighten 5%
- Scale: 0.99

#### Page Transitions
- Type: Slide from right (iOS style)
- Duration: 300ms
- Easing: ease-in-out

#### Progress Animations
- Duration: 1000ms
- Easing: cubic-bezier(0.4, 0, 0.2, 1)
- Fill mode: forwards

#### Chat Message Entry
- Duration: 300ms
- Transform: translateY(20px) → translateY(0)
- Opacity: 0 → 1
- Stagger: 50ms between messages

#### Streak Flame
- Continuous subtle pulse
- Scale: 1.0 → 1.1 → 1.0
- Duration: 2000ms
- Loop: infinite

#### Recording Timer
- Number change: fade transition
- Millisecond feel: Subtle vibration on each second tick

---

## Empty States

### No Exercises Completed
- Icon: Dumbbell or face outline
- Title: "Start Your Journey"
- Subtext: "Complete your first exercise to see progress"
- CTA: "View Today's Routine"

### No Chat History
- Icon: Chat bubble
- Title: "Meet Your Coach"
- Subtext: "Ask Max anything about face maxing"
- Suggested prompts below

### No Videos Recorded
- Icon: Video camera
- Title: "No Recordings Yet"
- Subtext: "Complete exercises to build your progress gallery"

### Forum Empty
- Icon: People
- Title: "Be the First"
- Subtext: "Start a conversation in the community"
- CTA: "Create Post"

---

## Error States

### Network Error
- Icon: Cloud with X
- Title: "Connection Lost"
- Subtext: "Check your internet and try again"
- CTA: "Retry"

### Camera Permission Denied
- Icon: Camera with slash
- Title: "Camera Access Needed"
- Subtext: "Allow camera access to record your exercises"
- CTA: "Open Settings"

### AI Service Unavailable
- Icon: Robot with warning
- Title: "Coach is Resting"
- Subtext: "AI service temporarily unavailable. Try again soon."
- Fallback: Show cached responses or basic tips

---

## Accessibility Considerations

### Color Contrast
- All text meets WCAG AA (4.5:1 ratio)
- Interactive elements have clear focus states
- Don't rely on color alone for status (use icons + text)

### Touch Targets
- Minimum 44x44px for all interactive elements
- Adequate spacing between buttons

### Screen Reader Support
- All icons have descriptive labels
- Images have alt text
- Progress announcements for screen readers

### Motion
- Respect `prefers-reduced-motion`
- Provide static alternatives for animated content

---

## Responsive Notes (Phone Only)

This is a mobile-first app. Design for:
- **Primary**: 375px - 428px width (iPhone 12-15 Pro range)
- **Safe Areas**: Account for notch and home indicator
- **Thumb Zones**: Primary actions in bottom 25% of screen
- **Status Bar**: Dark style (white icons on dark background)

---

## Image Asset Requirements

### Icons (24px default, SVG)
- Home / Routine
- Chart / Track
- Chat / Message
- Users / Social
- Settings
- Camera
- Play / Pause
- Checkmark
- Chevron (left, right, up, down)
- Plus / Minus
- Flame (streak)
- Trophy / Medal
- Gift / Shop
- Bell (notifications)
- Lock / Unlock
- Share
- Heart / Like
- Comment / Chat bubble
- More (three dots)
- Close / X
- Info
- Warning
- Microphone (voice input)
- Send
- Attachment / Paperclip
- Filter
- Search
- Flip camera
- Flash

### Illustrations
- Onboarding welcome (man looking at reflection)
- AI Coach character (friendly, professional)
- Empty states (various scenes)
- Success celebration
- Achievement unlock
- Weekly analysis report

### Exercise Thumbnails
- Category icons for each exercise type
- Form demonstration images

---

## Final Notes for Designer

1. **Dark mode is default** - There is no light mode in v1
2. **Green is success/growth** - Use `--accent-primary` liberally for positive reinforcement
3. **Masculine but not aggressive** - Avoid overly sharp edges, military fonts, or aggressive imagery
4. **Scientific credibility** - Clean layouts, precise alignments, data visualization
5. **AI feels magical** - Subtle glows, smooth animations, futuristic touches without being sci-fi
6. **Privacy is premium** - Secure feel, locked icons, local-first messaging
7. **Community is warm** - Forum feels like a club, not a comment section

The overall feel should be: "This is a serious tool for serious improvement, but it doesn't take itself too seriously."
