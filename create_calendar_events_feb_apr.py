#!/usr/bin/env python3
"""
Convert marketing event spreadsheet data (Feb-Apr 2026) to ICS calendar file.
"""

from datetime import datetime
import uuid

# Read the events data from file
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
    if event_start and event_end:
        description += f"\\nEvent Period: {event_start.strftime('%Y-%m-%d')} to {event_end.strftime('%Y-%m-%d')}"

    # Escape text
    summary = escape_ics_text(summary)
    description = escape_ics_text(description)

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

# Read from stdin
import sys
events_data = sys.stdin.read()

# Parse events
events = []
lines = events_data.strip().split("\n")

for line in lines:
    parts = line.split("\t")
    if len(parts) >= 9:
        date = parse_datetime(parts[0])
        event = parts[2]
        event_type = parts[3]
        buy_focus = parts[4]
        channel = parts[5]
        asset = parts[6]
        notes = parts[7] if len(parts) > 7 else ""

        # Parse event start/end dates if present
        event_start = None
        event_end = None
        if len(parts) > 9 and parts[9]:
            try:
                event_start = parse_datetime(parts[9])
            except:
                pass
        if len(parts) > 10 and parts[10]:
            try:
                event_end = parse_datetime(parts[10])
            except:
                pass

        events.append((date, event, event_type, buy_focus, channel, asset, notes, event_start, event_end))

# Create ICS file
ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//OUAC Marketing//Marketing Events Calendar Feb-Apr//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:OUAC Marketing Feb-Apr
X-WR-TIMEZONE:UTC
X-WR-CALDESC:Marketing events and tasks for OUAC campaigns (Feb-Apr 2026)
"""

# Add all events
for event_data in events:
    ics_content += create_ics_event(*event_data) + "\n"

ics_content += "END:VCALENDAR\n"

# Write to file
output_file = "ouac_marketing_calendar_feb_apr.ics"
with open(output_file, "w") as f:
    f.write(ics_content)

print(f"✅ Created: {output_file}")
print(f"📅 Events: {len(events)}")
