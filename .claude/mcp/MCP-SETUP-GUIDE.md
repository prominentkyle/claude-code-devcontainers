# MCP Server Setup Guide for Nylas Email and Todoist

This guide explains how to set up Nylas Email and Todoist MCP servers for use with Claude iOS app and Claude Desktop.

## 📋 Overview

This repository includes two MCP server configurations:

1. **Nylas Email MCP** (`nylas-mcp.json`) - Unified email management via Nylas (Gmail, Outlook, iCloud, Yahoo, IMAP)
2. **Todoist MCP** (`todoist-mcp.json`) - Manage Todoist tasks and projects

## 🔧 Setup Instructions

### 1. Nylas Email MCP Server Setup

The Nylas Email MCP server uses `@darinkishore/inbox-mcp` with Nylas API authentication. **Works with Gmail, Outlook, iCloud, Yahoo, and any IMAP email service!**

#### Step 1: Create Nylas Account

1. **Go to [Nylas Dashboard](https://dashboard.nylas.com/)**
2. **Sign up for a free account** (5 free connected email accounts included)
3. **Create a new application** or use the default one

#### Step 2: Connect Your Email Account

1. **In the Nylas Dashboard**, go to the **Grants** section
2. **Click "Add Grant"** to connect your email account
3. **Choose your email provider:**
   - Gmail, Google Workspace
   - Outlook, Office 365
   - iCloud
   - Yahoo
   - Custom IMAP
4. **Follow the OAuth flow** to authorize Nylas to access your email
5. **Note down your Grant ID** (shown in the Grants table after connection)

#### Step 3: Get Your API Credentials

1. **In the Nylas Dashboard sidebar**, click **"API Keys"**
2. **Copy your API Key** (keep this secure!)
3. **You'll need two values:**
   - `NYLAS_ACCESS_TOKEN` (your API key)
   - `NYLAS_GRANT_ID` (from the Grants table)

#### Step 4: Set Environment Variables

**For Claude Desktop:**

Add the configuration from `nylas-mcp.json` to your Claude Desktop config, replacing the placeholders with your actual credentials:

```json
{
  "mcpServers": {
    "nylas-email": {
      "command": "npx",
      "args": ["-y", "@darinkishore/inbox-mcp"],
      "env": {
        "NYLAS_ACCESS_TOKEN": "your_actual_api_key_here",
        "NYLAS_GRANT_ID": "your_actual_grant_id_here"
      }
    }
  }
}
```

**For Claude iOS App:**

Set the environment variables in your development environment:

```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
export NYLAS_ACCESS_TOKEN="your_api_key_here"
export NYLAS_GRANT_ID="your_grant_id_here"
```

**Quick Installation (Alternative):**

Use the interactive installer:

```bash
npx -y @smithery/cli@latest install "@darinkishore/inbox-mcp" --client claude
```

This will prompt you for your credentials and configure automatically.

#### Nylas Email Capabilities

Once configured, you can ask Claude to:
- **Read and search emails** across all connected accounts
- **Send emails** with attachments
- **Batch-triage emails** with natural language
- **Organize and filter** messages
- **Archive and delete** emails
- **Manage drafts** and replies

**Supports multiple email providers:**
- ✅ Gmail / Google Workspace
- ✅ Outlook / Office 365
- ✅ iCloud Mail
- ✅ Yahoo Mail
- ✅ Any IMAP service

**Example prompts:**
- "Show me my unread emails from today"
- "Send an email to john@example.com about the meeting"
- "Search for emails from Sarah containing 'project update'"
- "Archive all emails from newsletters"
- "Create a draft reply to the latest email from my boss"

---

### 2. Todoist MCP Server Setup

The Todoist MCP server uses `@hoffination/mcp-todoist` with API token authentication.

#### Step 1: Get Your Todoist API Token

1. **Log in to [Todoist](https://todoist.com/)**
2. **Go to Settings:**
   - Click your profile picture in the top right
   - Select "Settings"
3. **Find your API token:**
   - Navigate to "Integrations" tab
   - Scroll to "Developer" section
   - Copy your API token (keep this secure!)

#### Step 2: Set Environment Variable

**For Claude Desktop:**

Add the configuration from `todoist-mcp.json` to your Claude Desktop config, replacing `${TODOIST_API_TOKEN}` with your actual token:

```json
{
  "mcpServers": {
    "todoist": {
      "command": "npx",
      "args": ["-y", "@hoffination/mcp-todoist"],
      "env": {
        "TODOIST_API_TOKEN": "your_actual_token_here"
      }
    }
  }
}
```

**For Claude iOS App:**

You'll need to set the environment variable in your development environment or use a secrets manager.

**For local development:**

```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
export TODOIST_API_TOKEN="your_token_here"
```

#### Todoist Capabilities

Once configured, you can ask Claude to:
- Create, read, update, and complete tasks
- Manage projects and sections
- Work with labels and priorities
- Organize subtasks
- Add comments to tasks

**Example prompts:**
- "Create a task to finish the report by Friday"
- "Show me all my high-priority tasks"
- "Mark the 'Review code' task as complete"
- "Create a new project called 'Q1 Planning'"

---

## 📱 Using with Claude iOS App

When using Claude Code on the iOS app:

1. **Ensure this repository is configured** with the MCP JSON files
2. **Environment variables** should be set in your development environment
3. **Authentication** will be handled on first use
4. **Restart the app** if MCP servers don't appear immediately

---

## 🔍 Verifying Setup

### Check MCP Server Status

**In Claude Desktop:**
```
Tools → MCP Servers → Check status of nylas-email and todoist
```

**In Claude conversation:**
```
"What tools do you have available?"
```

Claude should list Nylas Email and Todoist tools if configured correctly.

### Test Commands

**Nylas Email Test:**
```
"List my email tools"
"Show me my recent emails"
```

**Todoist Test:**
```
"List my Todoist tools"
"Show me my tasks for today"
```

---

## 🔒 Security Notes

### Nylas Security
- **Never commit** your API credentials to version control
- Store `NYLAS_ACCESS_TOKEN` and `NYLAS_GRANT_ID` as environment variables
- Revoke access anytime from [Nylas Dashboard](https://dashboard.nylas.com/)
- Free tier includes 5 connected accounts with secure OAuth

### Todoist Security
- **Never commit** your API token to version control
- Use environment variables or secrets managers
- Regenerate your token from Todoist settings if compromised

### Best Practices
1. Always use environment variables for sensitive data (never hardcode)
2. Add `.env` files to `.gitignore`
3. Regularly review authorized applications in Nylas Dashboard
4. Use separate API keys for development and production
5. Monitor API usage in Nylas Dashboard

---

## 🐛 Troubleshooting

### Nylas Email Issues

**Problem:** "Invalid API credentials"
- **Solution:** Verify your `NYLAS_ACCESS_TOKEN` and `NYLAS_GRANT_ID` in Nylas Dashboard

**Problem:** "Grant not found"
- **Solution:** Check that your Grant ID is correct in the Nylas Dashboard → Grants section

**Problem:** "Email account not connected"
- **Solution:** Re-connect your email account in Nylas Dashboard → Grants → Add Grant

**Problem:** "Rate limit exceeded"
- **Solution:** Check your API usage in Nylas Dashboard; free tier has limits

**Problem:** "Authentication expired"
- **Solution:** Reconnect your email account in Nylas Dashboard (OAuth tokens may expire)

### Todoist Issues

**Problem:** "Invalid API token"
- **Solution:** Verify your token in Todoist Settings → Integrations

**Problem:** "Todoist server not responding"
- **Solution:** Check internet connection and Todoist API status

**Problem:** "Environment variable not found"
- **Solution:** Ensure `TODOIST_API_TOKEN` is properly set and exported

### General MCP Issues

**Problem:** "MCP server not found"
- **Solution:** Restart Claude Desktop completely (quit and relaunch)

**Problem:** "npx command not found"
- **Solution:** Install Node.js 18+ from [nodejs.org](https://nodejs.org)

**Problem:** "MCP server crashed"
- **Solution:** Check console logs and ensure all dependencies are installed

---

## 📚 Resources

### Documentation Links
- [Inbox-MCP (Nylas Email)](https://github.com/darinkishore/Inbox-MCP)
- [Official Nylas API MCP](https://github.com/nylas-samples/nylas-api-mcp)
- [Todoist MCP Server (@hoffination)](https://www.npmjs.com/package/@hoffination/mcp-todoist)
- [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- [Claude Code MCP Guide](https://code.claude.com/docs/en/mcp)

### API Documentation
- [Nylas API Documentation](https://developer.nylas.com/)
- [Nylas Dashboard](https://dashboard.nylas.com/)
- [Todoist API](https://developer.todoist.com/rest/v2/)

---

## 🎯 Next Steps

1. ✅ **Configure Nylas Email MCP** following steps above
2. ✅ **Configure Todoist MCP** following steps above
3. ✅ **Connect your email accounts** via Nylas Dashboard (Gmail, Outlook, iCloud, etc.)
4. ✅ **Test both integrations** with sample commands
5. ✅ **Explore capabilities** by asking Claude what it can do
6. ✅ **Integrate into your workflow** for productivity boost

---

**Need help?** Create an issue in this repository or consult the official MCP documentation.

**Last Updated:** 2026-01-07
