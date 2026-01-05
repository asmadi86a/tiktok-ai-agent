# 🤖 TikTok AI Agent

**Automated TikTok Content Generation & Management System**

Built for [@viralfindsnoww (HotPickVault)](https://www.tiktok.com/@viralfindsnoww)

---

## 🔥 What This Does

This AI agent automatically:
- 🔍 **Researches trending topics** on TikTok daily
- 💡 **Generates viral content ideas** using Google Gemini AI
- 📝 **Creates detailed video scripts** with hooks, shots, and CTAs
- 📅 **Plans optimal posting schedules** (2 posts/day at peak times)
- 📊 **Tracks analytics** and adjusts strategy
- 💾 **Exports content calendars** for easy execution

### Target: Get 10K+ followers → Qualify for TikTok Creator Rewards 💰

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

```bash
export GEMINI_API_KEY='your-gemini-api-key-here'
```

Get your free Gemini API key: https://makersuite.google.com/app/apikey

### 3. Run the Agent

```bash
python tiktok_agent.py
```

---

## 📊 How It Works

### Daily Automation Workflow

```
🌅 Morning (runs automatically):
  │
  ├─ 1. Research Trends
  │    └─ Scrape trending hashtags (#tiktokmademebuyit, #fyp, etc.)
  │    └─ Identify viral content formats
  │
  ├─ 2. Generate 5 Content Ideas
  │    └─ Product reviews (Amazon finds, smart home)
  │    └─ Before/after transformations
  │    └─ "Things that just make sense" format
  │    └─ Life hacks & organization tips
  │
  ├─ 3. Create Video Scripts
  │    └─ Hook (first 2 seconds to grab attention)
  │    └─ Shot-by-shot breakdown (5-8 shots)
  │    └─ Voiceover text
  │    └─ On-screen text overlays
  │    └─ Trending sound suggestions
  │
  ├─ 4. Schedule Posts
  │    └─ Morning: 9 AM EST
  │    └─ Evening: 5 PM EST or 9 PM EST
  │
  └─ 5. Save Content Calendar
       └─ content_calendar.json (all ideas & schedules)
```

---

## 📝 Output Files

After running, you'll get:

### `content_calendar.json`
Complete 7-day content plan with:
- 5 video ideas per day
- Full scripts with hooks
- Trending hashtags to use
- Optimal posting times
- CTAs and captions

### Daily Report
```
╔══════════════════════════════════════════════════════════╗
║        TikTok AI Agent - Daily Report                     ║
║        Account: @viralfindsnoww (HotPickVault)           ║
╠══════════════════════════════════════════════════════════╣
║ CONTENT GENERATION:                                      ║
║  • Ideas Generated: 5                                   ║
║  • Scripts Created: 5                                   ║
║  • Ready to Post: 2                                     ║
╠══════════════════════════════════════════════════════════╣
║ POSTING SCHEDULE:                                        ║
║  • Posts Scheduled: 14                                  ║
║  • Posts Today: 2                                       ║
║  • Next Post: Morning (9 AM)                           ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🎯 Content Strategy

### Trending Niches (January 2026)

1. **#tiktokmademebuyit** (180B+ views)
   - Amazon finds
   - Viral products
   - "I bought it so you don't have to"

2. **Smart Home & Organization** (50B+ views)
   - Kitchen gadgets
   - Organization hacks
   - Home transformation

3. **Before/After Transformations** (95B+ views)
   - Room makeovers
   - Product comparisons
   - Life hacks in action

### Proven Viral Formats

- ✅ **Product Reviews**: "TikTok made me buy this and..."
- ✅ **Quick Hacks**: "3 things you didn't know about..."
- ✅ **GRWM** (Get Ready With Me): Multi-tasking with products
- ✅ **Fit Check**: Showing off finds/organization
- ✅ **"Things That Just Make Sense"**: Life hack compilations

---

## 💰 Monetization Path

### Phase 1: Build Audience (0-10K followers)
- Post 2x daily (morning + evening)
- Use trending sounds & hashtags
- Engage with comments within 1 hour
- Cross-post to Instagram Reels

### Phase 2: Qualify for Creator Rewards (10K+ followers)
**Requirements:**
- 10,000+ followers
- 100,000+ valid views in last 30 days
- Videos must be 60+ seconds
- Original content only

**Estimated Earnings:** $20-50 per 100K views

### Phase 3: Add Affiliate Revenue
- Amazon Associates links in bio
- TikTok Shop product links
- Brand deals (once you hit 50K+ followers)

---

## ⚙️ Configuration

Edit `config.json` to customize:

```json
{
  "content_strategy": {
    "posts_per_day": 2,
    "optimal_times": ["09:00", "17:00", "21:00"],
    "content_types": [
      "product_reviews",
      "before_after",
      "life_hacks"
    ]
  },
  "trending_categories": [
    "smart_home",
    "kitchen_gadgets",
    "organization",
    "beauty"
  ]
}
```

---

## 🛠️ Next Steps After Generation

1. **Review** `content_calendar.json` for all 5 video ideas
2. **Film videos** using the scripts:
   - Use your phone camera
   - CapCut for editing (free, has trending templates)
   - Add trending sounds from TikTok's Creative Center
3. **Schedule posts** using:
   - TikTok's built-in scheduler (Business accounts)
   - Or post manually at optimal times
4. **Monitor analytics** daily:
   - Views, likes, shares
   - Watch time % (aim for 70%+)
   - Follower growth

---

## 📚 Resources

- [TikTok Creator Portal](https://www.tiktok.com/creators/)
- [TikTok Creator Rewards Eligibility](https://support.tiktok.com/en/using-tiktok/creator-tools)
- [Trending Sounds](https://ads.tiktok.com/business/creativecenter/)
- [CapCut Video Editor](https://www.capcut.com/)
- [Gemini API Docs](https://ai.google.dev/)

---

## ⚠️ Important Notes

### Compliance
- ❌ **Never** use bots to auto-like, auto-follow, or inflate engagement
- ✅ **Do** use this for content ideation and scheduling only
- ✅ **Always** manually review and post content yourself
- ✅ Use TikTok's official Content Posting API (requires developer approval)

### Content Guidelines
- Videos must be **60+ seconds** for Creator Rewards
- Must be **original content** (no duets/stitches for monetization)
- Follow TikTok Community Guidelines
- Disclose affiliate links and sponsored content

---

## 💬 Need Help?

For questions or improvements:
1. Open an issue on GitHub
2. Check TikTok's Creator Support
3. Join creator communities on Reddit r/TikTokMarketing

---

## 🚀 Roadmap

- [ ] Auto-upload videos via TikTok API
- [ ] Analytics dashboard with performance tracking
- [ ] A/B testing for hooks and captions
- [ ] Integration with video generation AI (Runway, Pika)
- [ ] Multi-account management
- [ ] Competitor analysis automation

---

**Built with ❤️ using Google Gemini AI**

License: MIT
