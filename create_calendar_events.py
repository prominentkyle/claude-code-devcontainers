#!/usr/bin/env python3
"""
Convert marketing event spreadsheet data to ICS calendar file.
"""

from datetime import datetime
import uuid

# Marketing events data
events_data = """2026-01-12 00:00:00	Mon	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Feed Post	Teaser post (Event + Buy focus)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-12 00:00:00	Mon	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Story	Teaser story (Event preview)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-12 00:00:00	Mon	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Feed Post	Teaser post (Event + Buy focus)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-12 00:00:00	Mon	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Story	Teaser story (Event preview)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-13 00:00:00	Tue	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Feed Post	Buy focus post (We're buying)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-13 00:00:00	Tue	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Feed Post	Buy focus post (We're buying)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-13 00:00:00	Tue	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Paid Ads	Update/refresh Always-On Buy Ad creative (weekly)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-14 00:00:00	Wed	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Email Blast	Email #1: Event details + Buy focus		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-14 00:00:00	Wed	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Feed Post	Event details post (What/When)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-14 00:00:00	Wed	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Story	Countdown/preview story		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-14 00:00:00	Wed	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Feed Post	Event details post (What/When)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-14 00:00:00	Wed	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Story	Countdown/preview story		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-15 00:00:00	Thu	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Story	Reminder story + countdown sticker		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-15 00:00:00	Thu	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Story	Reminder story + countdown sticker		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-15 00:00:00	Thu	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Paid Ads	Launch Event Ad Flight (traffic/reach) – start		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-15 00:00:00	Thu	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Text Message	Text #2: Weekend reminder (Event starts soon)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-16 00:00:00	Fri	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Email Blast	Email #2: Weekend kickoff / New arrivals highlight		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-16 00:00:00	Fri	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Feed Post	Kickoff post (Weekend is here)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-16 00:00:00	Fri	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Story	Kickoff story (show products / buy counter)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-16 00:00:00	Fri	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Feed Post	Kickoff post (Weekend is here)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-16 00:00:00	Fri	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Story	Kickoff story (show products / buy counter)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Feed Post	Last chance post (Final day)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Feed Post	Saturday push (Top picks / bundles)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Story	Last chance story (Final hours)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Story	Saturday story (live shopping + buy)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Feed Post	Last chance post (Final day)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Feed Post	Saturday push (Top picks / bundles)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Story	Last chance story (Final hours)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Story	Saturday story (live shopping + buy)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-17 00:00:00	Sat	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Paid Ads	Event Ad Flight – end		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-18 00:00:00	Sun	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Email Blast	Optional: Post-event thank you + buy call (only if needed)		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-18 00:00:00	Sun	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Facebook Feed Post	Recap/thank you + Next week buy call		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-18 00:00:00	Sun	20 Bodysuits for $10	Sale	Shoes & Accessories (understock)	Instagram Feed Post	Recap/thank you + Next week buy call		2026-01-12 00:00:00	2026-01-16 00:00:00	2026-01-17 00:00:00
2026-01-19 00:00:00	Mon	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Feed Post	Teaser post (Event + Buy focus)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-19 00:00:00	Mon	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Story	Teaser story (Event preview)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-19 00:00:00	Mon	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Feed Post	Teaser post (Event + Buy focus)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-19 00:00:00	Mon	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Story	Teaser story (Event preview)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-20 00:00:00	Tue	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Feed Post	Buy focus post (We're buying)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-20 00:00:00	Tue	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Feed Post	Buy focus post (We're buying)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-20 00:00:00	Tue	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Paid Ads	Update/refresh Always-On Buy Ad creative (weekly)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-21 00:00:00	Wed	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Email Blast	Email #1: Event details + Buy focus		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-21 00:00:00	Wed	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Feed Post	Event details post (What/When)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-21 00:00:00	Wed	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Story	Countdown/preview story		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-21 00:00:00	Wed	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Feed Post	Event details post (What/When)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-21 00:00:00	Wed	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Story	Countdown/preview story		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-22 00:00:00	Thu	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Story	Reminder story + countdown sticker		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-22 00:00:00	Thu	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Story	Reminder story + countdown sticker		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-22 00:00:00	Thu	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Paid Ads	Launch Event Ad Flight (traffic/reach) – start		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-22 00:00:00	Thu	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Text Message	Text #2: Weekend reminder (Event starts soon)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-23 00:00:00	Fri	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Email Blast	Email #2: Weekend kickoff / New arrivals highlight		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-23 00:00:00	Fri	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Feed Post	Kickoff post (Weekend is here)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-23 00:00:00	Fri	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Story	Kickoff story (show products / buy counter)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-23 00:00:00	Fri	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Feed Post	Kickoff post (Weekend is here)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-23 00:00:00	Fri	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Story	Kickoff story (show products / buy counter)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-24 00:00:00	Sat	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Feed Post	Saturday push (Top picks / bundles)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-24 00:00:00	Sat	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Story	Saturday story (live shopping + buy)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-24 00:00:00	Sat	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Feed Post	Saturday push (Top picks / bundles)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-24 00:00:00	Sat	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Story	Saturday story (live shopping + buy)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-25 00:00:00	Sun	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Feed Post	Last chance post (Final day)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-25 00:00:00	Sun	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Story	Last chance story (Final hours)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-25 00:00:00	Sun	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Feed Post	Last chance post (Final day)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-25 00:00:00	Sun	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Story	Last chance story (Final hours)		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-25 00:00:00	Sun	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Paid Ads	Event Ad Flight – end		2026-01-19 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-26 00:00:00	Mon	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Feed Post	Teaser post (Event + Buy focus)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-26 00:00:00	Mon	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Story	Teaser story (Event preview)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-26 00:00:00	Mon	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Feed Post	Teaser post (Event + Buy focus)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-26 00:00:00	Mon	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Story	Teaser story (Event preview)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-26 00:00:00	Mon	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Email Blast	Optional: Post-event thank you + buy call (only if needed)		2026-01-26 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-26 00:00:00	Mon	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Facebook Feed Post	Recap/thank you + Next week buy call		2026-01-26 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-26 00:00:00	Mon	Winter Clearance Weekend	Clearance	Toys & Books (understock)	Instagram Feed Post	Recap/thank you + Next week buy call		2026-01-26 00:00:00	2026-01-23 00:00:00	2026-01-25 00:00:00
2026-01-27 00:00:00	Tue	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Feed Post	Buy focus post (We're buying)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-27 00:00:00	Tue	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Feed Post	Buy focus post (We're buying)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-27 00:00:00	Tue	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Paid Ads	Update/refresh Always-On Buy Ad creative (weekly)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-28 00:00:00	Wed	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Email Blast	Email #1: Event details + Buy focus		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-28 00:00:00	Wed	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Feed Post	Event details post (What/When)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-28 00:00:00	Wed	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Story	Countdown/preview story		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-28 00:00:00	Wed	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Feed Post	Event details post (What/When)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-28 00:00:00	Wed	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Story	Countdown/preview story		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-29 00:00:00	Thu	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Story	Reminder story + countdown sticker		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-29 00:00:00	Thu	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Story	Reminder story + countdown sticker		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-29 00:00:00	Thu	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Paid Ads	Launch Event Ad Flight (traffic/reach) – start		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-29 00:00:00	Thu	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Text Message	Text #2: Weekend reminder (Event starts soon)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-30 00:00:00	Fri	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Email Blast	Email #2: Weekend kickoff / New arrivals highlight		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-30 00:00:00	Fri	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Feed Post	Kickoff post (Weekend is here)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-30 00:00:00	Fri	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Story	Kickoff story (show products / buy counter)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-30 00:00:00	Fri	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Feed Post	Kickoff post (Weekend is here)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-30 00:00:00	Fri	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Story	Kickoff story (show products / buy counter)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Feed Post	Last chance post (Final day)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Feed Post	Saturday push (Top picks / bundles)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Story	Last chance story (Final hours)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Story	Saturday story (live shopping + buy)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Feed Post	Last chance post (Final day)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Feed Post	Saturday push (Top picks / bundles)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Story	Last chance story (Final hours)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Story	Saturday story (live shopping + buy)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-01-31 00:00:00	Sat	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Paid Ads	Event Ad Flight – end		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-02-01 00:00:00	Sun	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Email Blast	Optional: Post-event thank you + buy call (only if needed)		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-02-01 00:00:00	Sun	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Facebook Feed Post	Recap/thank you + Next week buy call		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-02-01 00:00:00	Sun	Western Reveal (Co-op)	Reveal	Boots / Western Wear + Accessories	Instagram Feed Post	Recap/thank you + Next week buy call		2026-01-26 00:00:00	2026-01-31 00:00:00	2026-01-31 00:00:00
2026-02-02 00:00:00	Mon	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Feed Post	Teaser post (Event + Buy focus)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-02 00:00:00	Mon	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Story	Teaser story (Event preview)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-02 00:00:00	Mon	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Feed Post	Teaser post (Event + Buy focus)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-02 00:00:00	Mon	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Story	Teaser story (Event preview)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-03 00:00:00	Tue	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Feed Post	Buy focus post (We're buying)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-03 00:00:00	Tue	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Feed Post	Buy focus post (We're buying)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-03 00:00:00	Tue	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Paid Ads	Update/refresh Always-On Buy Ad creative (weekly)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-04 00:00:00	Wed	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Email Blast	Email #1: Event details + Buy focus		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-04 00:00:00	Wed	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Feed Post	Event details post (What/When)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-04 00:00:00	Wed	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Story	Countdown/preview story		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-04 00:00:00	Wed	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Feed Post	Event details post (What/When)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-04 00:00:00	Wed	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Story	Countdown/preview story		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-05 00:00:00	Thu	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Story	Reminder story + countdown sticker		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-05 00:00:00	Thu	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Story	Reminder story + countdown sticker		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-05 00:00:00	Thu	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Paid Ads	Launch Event Ad Flight (traffic/reach) – start		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-05 00:00:00	Thu	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Text Message	Text #2: Weekend reminder (Event starts soon)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-06 00:00:00	Fri	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Email Blast	Email #2: Weekend kickoff / New arrivals highlight		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-06 00:00:00	Fri	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Feed Post	Kickoff post (Weekend is here)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-06 00:00:00	Fri	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Story	Kickoff story (show products / buy counter)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-06 00:00:00	Fri	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Feed Post	Kickoff post (Weekend is here)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-06 00:00:00	Fri	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Story	Kickoff story (show products / buy counter)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Feed Post	Last chance post (Final day)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Feed Post	Saturday push (Top picks / bundles)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Story	Last chance story (Final hours)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Story	Saturday story (live shopping + buy)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Feed Post	Last chance post (Final day)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Feed Post	Saturday push (Top picks / bundles)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Story	Last chance story (Final hours)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Story	Saturday story (live shopping + buy)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-07 00:00:00	Sat	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Paid Ads	Event Ad Flight – end		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-08 00:00:00	Sun	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Email Blast	Optional: Post-event thank you + buy call (only if needed)		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-08 00:00:00	Sun	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Facebook Feed Post	Recap/thank you + Next week buy call		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00
2026-02-08 00:00:00	Sun	Valentine Mini-Reveal	Reveal	Dresswear + Dress Shoes	Instagram Feed Post	Recap/thank you + Next week buy call		2026-02-02 00:00:00	2026-02-07 00:00:00	2026-02-07 00:00:00"""


def parse_datetime(dt_str):
    """Parse datetime string to datetime object."""
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")


def format_datetime_ics(dt):
    """Format datetime for ICS file (YYYYMMDDTHHMMSSZ)."""
    return dt.strftime("%Y%m%dT%H%M%SZ")


def escape_ics_text(text):
    """Escape special characters for ICS format."""
    text = text.replace("\\", "\\\\")
    text = text.replace(";", "\\;")
    text = text.replace(",", "\\,")
    text = text.replace("\n", "\\n")
    return text


def create_ics_event(date, event, event_type, buy_focus, channel, asset, notes, event_start, event_end):
    """Create an ICS event string."""
    uid = str(uuid.uuid4())
    dtstamp = format_datetime_ics(datetime.now())
    dtstart = format_datetime_ics(date)

    # Create summary (title)
    summary = f"{channel}: {asset}"

    # Create description with all details
    description = f"Event: {event}\\n"
    description += f"Type: {event_type}\\n"
    description += f"Buy Focus: {buy_focus}\\n"
    description += f"Channel: {channel}\\n"
    description += f"Asset: {asset}\\n"
    if notes:
        description += f"Notes: {notes}\\n"
    description += f"\\nEvent Period: {event_start.strftime('%Y-%m-%d')} to {event_end.strftime('%Y-%m-%d')}"

    # Escape text
    summary = escape_ics_text(summary)
    description = escape_ics_text(description)
    event_name = escape_ics_text(event)

    event_str = f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:{dtstamp}
DTSTART:{dtstart}
SUMMARY:{summary}
DESCRIPTION:{description}
CATEGORIES:OUAC Marketing,{event_type},{channel}
STATUS:CONFIRMED
TRANSP:TRANSPARENT
END:VEVENT"""

    return event_str


def main():
    """Generate ICS file from events data."""
    # Parse events
    events = []
    lines = events_data.strip().split("\n")

    for line in lines:
        parts = line.split("\t")
        if len(parts) >= 11:
            date = parse_datetime(parts[0])
            day = parts[1]
            event = parts[2]
            event_type = parts[3]
            buy_focus = parts[4]
            channel = parts[5]
            asset = parts[6]
            notes = parts[7]
            event_start = parse_datetime(parts[9])
            event_end = parse_datetime(parts[10])

            events.append((date, event, event_type, buy_focus, channel, asset, notes, event_start, event_end))

    # Create ICS file
    ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//OUAC Marketing//Marketing Events Calendar//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:OUAC Marketing
X-WR-TIMEZONE:UTC
X-WR-CALDESC:Marketing events and tasks for OUAC campaigns
"""

    # Add all events
    for event_data in events:
        ics_content += create_ics_event(*event_data) + "\n"

    ics_content += "END:VCALENDAR\n"

    # Write to file
    output_file = "ouac_marketing_calendar.ics"
    with open(output_file, "w") as f:
        f.write(ics_content)

    print(f"✅ Created calendar file: {output_file}")
    print(f"📅 Total events: {len(events)}")
    print(f"\n📋 Next steps:")
    print(f"1. Open your calendar application (Google Calendar, Apple Calendar, Outlook, etc.)")
    print(f"2. Import the file '{output_file}'")
    print(f"3. Select or create the 'OUAC Marketing' calendar")
    print(f"\nFor Google Calendar:")
    print(f"   • Go to calendar.google.com")
    print(f"   • Click the '+' next to 'Other calendars'")
    print(f"   • Select 'Import'")
    print(f"   • Choose '{output_file}'")
    print(f"   • Select 'OUAC Marketing' as the destination calendar (or create it)")


if __name__ == "__main__":
    main()
