# FaceMax - Product Requirements Document
## Version 1.0 | Preliminary Baseline Build

---

## 1. Executive Summary

### 1.1 Product Vision
FaceMax is a male-focused face maxing app that combines AI-powered facial analysis, guided exercise routines, and community features to help men improve their facial aesthetics through natural, non-surgical techniques. The app creates a safe, encouraging environment for self-improvement with high retention mechanics.

### 1.2 Target Audience
- **Primary**: Men aged 18-35 in India (₹500/month pricing)
- **Secondary**: Men aged 18-35 globally (US/international pricing TBD)
- **Psychographics**: Self-improvement oriented, fitness-conscious, early adopters of wellness tech

### 1.3 Monetization Strategy
| Tier | Price | Features |
|------|-------|----------|
| **Free** | ₹0 | 3-5 daily exercises, basic video recording, limited AI chat (5-10 messages), view leaderboard |
| **Basic** | ₹500/month | 10 daily exercises, full AI coaching, weekly analysis, 7-day tracking, forum access |
| **Premium** | *Future* | 20-30 exercises, custom routines, advanced AI features, longer video storage |

---

## 2. Core Features

### 2.1 Onboarding Flow (Chat-Based)

#### Requirements
- **Format**: Conversational chat interface (not multi-page form)
- **Input Methods**: Text typing, voice recording, pre-built selectors
- **Duration**: Under 2 minutes to complete

#### Data Collection
- Basic profile (name, age, height, weight)
- Current face photo upload (for AI transformation)
- Voice sample (6-10 seconds for future voice cloning)
- Goal setting (what they want to improve)
- Daily routine time preference (9 AM, 10 AM, etc.)

#### AI Motivational Video Generation
- **Trigger**: After photo upload during onboarding
- **Technology**: Veo3/VeoFree with image-to-video
- **Prompt Template**: "Hey, this is you, and this is what you could look like in a couple of months. Ensure that you keep training, keep doing your facial routines, and using FaceMax yourself. Cheers! I'll be here for you and I'm rooting for you."
- **Storage**: Local device + cloud backup

---

### 2.2 Routine System

#### Free Tier
- **Exercise Count**: 3-5 exercises daily
- **Routine Type**: Fixed (cannot customize)
- **Library Access**: View-only, cannot add new exercises
- **Timer**: 24-hour countdown after completion

#### Basic Tier (₹500/month)
- **Exercise Count**: 10 exercises daily
- **Routine Type**: Fixed professional routine
- **Library Access**: 10+ exercises viewable

#### Future Premium Tier
- **Exercise Count**: 20-30 exercises
- **Routine Type**: Fully customizable
- **Library Access**: 30+ exercise library

#### Exercise Recording Flow
1. User clicks "Start Exercise"
2. Camera opens with guided overlay (boundary detection)
3. Real-time AI feedback (Basic tier only, using Gemini Vision)
4. Recording starts automatically
5. **Storage Strategy**:
   - Full video: 720p MP4, stored locally
   - Time-lapse: 10-second compressed version (from 4-minute exercise)
   - Screenshots: Captured at intervals, sent to server for analysis

---

### 2.3 Camera & Recording Features

#### Technical Specifications
- **Resolution**: 720p (camera preview and recording)
- **Format**: MP4
- **Frame Rate**: 30 FPS
- **Overlay**: Guided boundary box for face positioning
- **Storage**: Local device only (encrypted)

#### AI Features (Basic Tier)
- Real-time boundary detection (on-device TensorFlow Lite)
- Optional: Gemini Live feedback for form correction
- Cheating detection (PostNet model to verify actual exercise)

#### Video Processing
- Auto-generate 10-second time-lapse from full exercise
- Screenshot extraction at 0s, 30s, 60s, 90s intervals
- Local gallery with chronological sorting

---

### 2.4 AI Coach / Chat System

#### Free Tier Limitations
- Max 5-10 messages per day
- Text-only responses
- No image analysis capabilities
- Basic exercise advice only

#### Basic Tier Features
- Unlimited messaging
- Image upload and analysis
- Personalized advice based on user data
- Preliminary medical guidance (with disclaimers to see doctors for serious issues)

#### Chat Interface
- Persistent chat history
- Voice input support
- Image attachment capability
- Quick-reply suggestions

---

### 2.5 Weekly Analysis & Tracking

#### Data Collection
- Screenshots from exercise videos (7-day intervals)
- User-submitted photos
- Optional weight/ measurements input

#### AI Analysis (Gemini Vision API)
Metrics to track:
- Face symmetry improvement
- Jawline definition changes
- Cheekbone prominence
- Facial debloating (water retention)
- Skin quality indicators
- Overall progress score

#### Output
- Weekly report with visual comparisons
- Written feedback ("Your cheekbones show improvement")
- Percentage-based progress metrics
- Trend charts over time

---

### 2.6 Tracking Tab (Progress Visualization)

#### Charts & Metrics
- Exercise completion streak
- Points accumulation graph
- Weight tracking (manual input)
- Measurement trends (jaw width, face ratios)
- Before/after photo comparison slider

#### Data Export
- Option to export progress photos/videos
- CSV export for measurements
- Share achievements (optional social sharing)

---

### 2.7 Social Features

#### Points System
- **Per Exercise**: 5 points
- **Daily Completion Bonus**: 10 points
- **Anti-Cheat**: TensorFlow Lite model verifies actual exercise

#### Leaderboard
- Global rankings by points
- Weekly/monthly/all-time views
- User avatars and point totals
- Free users climb slower (fewer exercises available)

#### Forum (Reddit-Style)
- Thread-based discussions
- Upvote/downvote system
- AI-based moderation + report system
- Community agent for engagement
- Delete own comments capability

#### Content Feed ("Doomscrolling" Tab)
- **Initial Database**: 100 videos
- **Daily Uploads**: 20 new videos
- **Source**: Self-hosted CDN
- **Content**: Looks-maxing influencers, tutorials, motivation
- **UX**: "You're all caught up" message when new content exhausted

---

### 2.8 Shop Tab

#### V1 Implementation
- "Coming Soon" placeholder
- Email capture for launch notification

#### Future Implementation
- Affiliate products (Gua Sha tools, mastic gum, skincare)
- Categories: Tools, Supplements, Skincare
- Integration: Razorpay (India), Stripe (Global)

---

### 2.9 Account & Gallery

#### Account Settings
- Profile management
- Subscription status
- Notification preferences
- Privacy settings

#### Gallery
- Chronological video list
- Filter by exercise type
- Before/after comparison tool
- Local storage management (delete old videos)

---

## 3. Technical Architecture

### 3.1 Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | React Native (cross-platform) |
| **Backend** | Firebase (Auth, Firestore, Storage) |
| **AI Model** | Gemini 3 Flash Preview (all text + vision) |
| **On-Device AI** | TensorFlow Lite (face detection, anti-cheat) |
| **Video Recording** | react-native-vision-camera |
| **Video Generation** | Veo3/VeoFree API |
| **Database** | Firestore (NoSQL) |
| **Storage** | Firebase Storage + Local encrypted storage |
| **CDN** | Self-hosted (for content videos) |
| **Payments** | Razorpay (India), Stripe (Global) |

### 3.2 Data Models

#### User Collection
```javascript
{
  uid: string,
  email: string,
  name: string,
  age: number,
  height: number,
  weight: number,
  tier: 'free' | 'basic' | 'premium',
  dailyGoalTime: string, // "09:00"
  voiceSampleUrl: string,
  onboardingComplete: boolean,
  createdAt: timestamp,
  lastActive: timestamp,
  totalPoints: number,
  currentStreak: number,
  longestStreak: number
}
```

#### Routine Collection
```javascript
{
  id: string,
  name: string,
  tier: 'free' | 'basic' | 'premium',
  exercises: [
    {
      id: string,
      name: string,
      duration: number, // seconds
      description: string,
      videoUrl: string,
      targetArea: string
    }
  ],
  estimatedDuration: number // total minutes
}
```

#### Exercise Completion Collection
```javascript
{
  id: string,
  userId: string,
  exerciseId: string,
  routineId: string,
  completedAt: timestamp,
  duration: number,
  videoPath: string, // local storage path
  screenshots: [string], // cloud URLs
  pointsEarned: number,
  aiVerified: boolean
}
```

#### Weekly Analysis Collection
```javascript
{
  id: string,
  userId: string,
  weekNumber: number,
  screenshots: [string],
  analysis: {
    symmetry: number,
    jawline: number,
    cheekbones: number,
    overall: number,
    feedback: string
  },
  createdAt: timestamp
}
```

#### Forum Post Collection
```javascript
{
  id: string,
  userId: string,
  title: string,
  content: string,
  upvotes: number,
  downvotes: number,
  commentCount: number,
  createdAt: timestamp,
  tags: [string]
}
```

#### Chat Message Collection
```javascript
{
  id: string,
  userId: string,
  role: 'user' | 'assistant',
  content: string,
  imageUrl: string, // optional
  createdAt: timestamp
}
```

### 3.3 Security & Privacy

#### Data Protection
- AES-256 encryption for local video storage
- Firebase Security Rules for database access
- No facial data sold or used for advertising
- GDPR/CCPA compliant data handling
- Automatic data deletion after account termination

#### Authentication
- Firebase Auth (email/password, Google, Apple)
- JWT token-based session management
- Biometric authentication option (fingerprint/face ID)

---

## 4. UI/UX Specifications

### 4.1 Navigation Structure

#### Bottom Navigation (4 Tabs)
1. **Routine** (Home) - Daily exercises
2. **Track** - Progress charts and analytics
3. **Chat** - AI coach interface
4. **Social** - Leaderboard + Forum

#### Top Navigation Icons
- **Top Left**: Settings/Account
- **Top Right**: Shop (cart icon)

#### Screen Hierarchy
```
App
├── Onboarding (Chat-based)
├── Main App
│   ├── Routine Tab
│   │   ├── Daily Routine List
│   │   ├── Exercise Detail
│   │   └── Camera/Recording
│   ├── Track Tab
│   │   ├── Progress Dashboard
│   │   ├── Gallery
│   │   └── Measurements
│   ├── Chat Tab
│   │   └── AI Coach Interface
│   └── Social Tab
│       ├── Leaderboard
│       ├── Forum
│       └── Content Feed
└── Account
    ├── Profile
    ├── Subscription
    ├── Gallery
    └── Settings
```

### 4.2 Design System

#### Color Palette (Suggestion)
- **Primary**: Deep Blue (#1E3A5F) - Masculine, trustworthy
- **Secondary**: Teal (#2ECC71) - Growth, health
- **Accent**: Orange (#FF6B35) - Energy, motivation
- **Background**: Dark (#0F1419) - Reduces eye strain, premium feel
- **Surface**: Dark Gray (#1A1F26) - Card backgrounds
- **Text**: White (#FFFFFF) / Gray (#B0B8C1)

#### Typography
- **Headings**: Inter Bold / Roboto Bold
- **Body**: Inter Regular / Roboto Regular
- **Size Scale**: 12, 14, 16, 20, 24, 32, 40

#### Components
- Cards with subtle border radius (8px)
- Primary buttons: Full width, rounded (12px)
- Secondary buttons: Outlined
- Progress indicators: Circular for exercises, linear for streaks

---

## 5. Feature Gating Matrix

| Feature | Free | Basic ₹500 | Premium (Future) |
|---------|------|------------|------------------|
| Daily Exercises | 3-5 fixed | 10 fixed | 20-30 customizable |
| Exercise Library | View 3-5 | View 10+ | Full library (30+) |
| Video Recording | Yes (local) | Yes + screenshots | Yes + full analysis |
| AI Real-time Feedback | No | Yes (Gemini) | Yes (advanced) |
| Weekly Analysis | No | Yes | Yes (detailed) |
| AI Coach Messages | 5-10/day | Unlimited | Unlimited |
| Image Analysis in Chat | No | Yes | Yes |
| Forum Access | Read-only | Full access | Full access + badges |
| Leaderboard | View only | Participate | Premium badge |
| Point Multiplier | 1x | 1x | 2x |
| Video Storage | 7 days local | 30 days local | Unlimited cloud |
| Custom Reminders | No | Yes | Yes |
| Export Data | No | Yes | Yes |

---

## 6. Development Phases

### Phase 1: MVP (Weeks 1-4)
- [ ] Project setup (React Native + Firebase)
- [ ] Onboarding flow (chat-based)
- [ ] Basic routine display (3-5 exercises)
- [ ] Camera integration with recording
- [ ] Local video storage
- [ ] Basic AI coach (limited messages)
- [ ] Free tier only

### Phase 2: Basic Tier Launch (Weeks 5-8)
- [ ] Payment integration (Razorpay)
- [ ] Full routine system (10 exercises)
- [ ] Gemini Vision integration for analysis
- [ ] Weekly analysis reports
- [ ] Points system with anti-cheat
- [ ] Social leaderboard
- [ ] Forum basic functionality

### Phase 3: Polish & Scale (Weeks 9-12)
- [ ] AI motivational video generation
- [ ] Content feed (doomscrolling)
- [ ] Advanced tracking charts
- [ ] Performance optimization
- [ ] Beta testing
- [ ] App store submission

### Phase 4: Post-Launch (Future)
- [ ] Premium tier development
- [ ] Shop implementation
- [ ] Advanced AI features
- [ ] International expansion
- [ ] iOS optimization

---

## 7. API Integration Details

### 7.1 Gemini 3 Flash Preview

#### Text Generation
```javascript
// Chat responses
const response = await genAI.generateText({
  model: 'gemini-3-flash-preview',
  prompt: userMessage,
  context: chatHistory,
  maxTokens: 500
});
```

#### Vision Analysis
```javascript
// Weekly facial analysis
const analysis = await genAI.generateContent({
  model: 'gemini-3-flash-preview',
  contents: [
    { text: "Analyze these facial images for symmetry, jawline definition, and cheekbone prominence. Provide a score 0-100 for each metric." },
    { inlineData: { mimeType: "image/jpeg", data: base64Image1 } },
    { inlineData: { mimeType: "image/jpeg", data: base64Image2 } }
  ]
});
```

### 7.2 Video Generation (Veo3)

```javascript
// AI motivational video
const video = await veo.generate({
  image: userPhotoBase64,
  prompt: "Person speaking confidently, face glowing with health, subtle transformation showing improvement, motivational tone",
  duration: "8s"
});
```

---

## 8. Success Metrics

### 8.1 North Star Metrics
- **Daily Active Users (DAU)**
- **Retention Rate** (Day 1, Day 7, Day 30)
- **Conversion Rate** (Free → Basic)
- **Average Session Duration**

### 8.2 Secondary Metrics
- Exercise completion rate
- Streak maintenance (7+ days)
- Chat engagement (messages per user)
- Social feature engagement
- Video recording completion rate

### 8.3 Technical Metrics
- App crash rate (< 1%)
- Video processing time (< 30s)
- AI response latency (< 2s)
- API costs per user

---

## 9. Risk Mitigation

### 9.1 Privacy Risks
- **Risk**: User concerns about facial data
- **Mitigation**: On-device processing, clear privacy policy, no data selling

### 9.2 Technical Risks
- **Risk**: AI analysis accuracy
- **Mitigation**: Set realistic expectations, position as "estimates not medical advice"

### 9.3 Content Risks
- **Risk**: Misinformation about exercises
- **Mitigation**: Partner with professionals, disclaimers, encourage doctor consultation

### 9.4 Business Risks
- **Risk**: Low conversion from free to paid
- **Mitigation**: Strong value demonstration in free tier, limited but useful AI features

---

## 10. Open Questions & Future Considerations

### 10.1 To Be Determined
1. Exact exercise list for each tier (pending professional consultation)
2. International pricing strategy
3. Gemini Live integration feasibility and cost
4. Voice cloning provider selection
5. CDN capacity planning for 100+ videos

### 10.2 Future Enhancements
- Wearable integration (Apple Watch, Fitbit)
- Nutrition tracking for face debloating
- Sleep tracking correlation
- AR mirror for real-time form checking
- Community challenges and competitions
- Professional consultation marketplace

---

## 11. Appendix

### 11.1 Exercise Database Schema
```javascript
{
  id: string,
  name: string,
  category: 'mewing' | 'gua_sha' | 'cheekbone' | 'jawline' | 'face_yoga' | 'cold_therapy',
  description: string,
  instructions: [string],
  duration: number, // recommended seconds
  difficulty: 'beginner' | 'intermediate' | 'advanced',
  targetAreas: [string],
  videoUrl: string,
  thumbnailUrl: string,
  caloriesBurned: number,
  equipment: [string] // optional
}
```

### 11.2 Anti-Cheat Detection Logic
- Face must be present in frame (TensorFlow Lite face detection)
- Movement patterns must match exercise type (PostNet pose estimation)
- Duration must match claimed completion time
- Random spot checks on submissions

---

**Document Owner**: Product Team
**Last Updated**: February 2026
**Status**: Preliminary Baseline Approved
