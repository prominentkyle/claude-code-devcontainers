# MCP Server Setup Guide for Gmail and Todoist

This guide explains how to set up Gmail and Todoist MCP servers for use with Claude iOS app and Claude Desktop.

## 📋 Overview

This repository includes two MCP server configurations:

1. **Gmail MCP** (`gmail-mcp.json`) - Manage Gmail through natural language
2. **Todoist MCP** (`todoist-mcp.json`) - Manage Todoist tasks and projects

## 🔧 Setup Instructions

### 1. Gmail MCP Server Setup

The Gmail MCP server uses `@gongrzhe/server-gmail-autoauth-mcp` with OAuth 2.0 authentication.

#### Step 1: Google Cloud Console Setup

1. **Go to [Google Cloud Console](https://console.cloud.google.com/)**
2. **Create a new project or select an existing one**
3. **Enable Gmail API:**
   - Navigate to "API & Services" → "Library"
   - Search for "Gmail API" and click "Enable"
4. **Create OAuth 2.0 Credentials:**
   - Go to "API & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth 2.0 Client ID"
   - Choose "Desktop app" as the application type
   - Click "Create" and download the JSON credentials file

#### Step 2: Local Configuration

```bash
# Create the Gmail MCP directory
mkdir -p ~/.gmail-mcp

# Rename and move your downloaded credentials
mv ~/Downloads/client_secret_*.json ~/.gmail-mcp/gcp-oauth.keys.json
```

#### Step 3: Activate in Claude

**For Claude Desktop:**

Copy the content of `gmail-mcp.json` to your Claude Desktop config file:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

**For Claude iOS App:**

The Gmail MCP server will be available when you use Claude Code on the iOS app with this repository.

#### Step 4: First-Time Authentication

The first time you use Gmail features:
1. Claude will prompt you to authenticate
2. A browser window will open
3. Sign in to your Google account
4. Grant the requested permissions
5. Authentication token will be saved automatically

#### Gmail Capabilities

Once configured, you can ask Claude to:
- Read and search emails
- Send emails
- Manage labels and filters
- Archive and delete messages
- Handle attachments

**Example prompts:**
- "Show me my unread emails from today"
- "Send an email to john@example.com about the meeting"
- "Search for emails from Sarah containing 'project update'"

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
Tools → MCP Servers → Check status of gmail and todoist
```

**In Claude conversation:**
```
"What tools do you have available?"
```

Claude should list Gmail and Todoist tools if configured correctly.

### Test Commands

**Gmail Test:**
```
"List my Gmail tools"
"Show me my recent emails"
```

**Todoist Test:**
```
"List my Todoist tools"
"Show me my tasks for today"
```

---

## 🔒 Security Notes

### Gmail Security
- **Never commit** `gcp-oauth.keys.json` to version control
- The OAuth token is stored locally and encrypted
- Revoke access anytime from [Google Account Settings](https://myaccount.google.com/permissions)

### Todoist Security
- **Never commit** your API token to version control
- Use environment variables or secrets managers
- Regenerate your token from Todoist settings if compromised

### Best Practices
1. Add `gcp-oauth.keys.json` to `.gitignore`
2. Use environment variables for sensitive data
3. Regularly review authorized applications
4. Use separate tokens for development and production

---

## 🐛 Troubleshooting

### Gmail Issues

**Problem:** "Authentication failed"
- **Solution:** Delete `~/.gmail-mcp/credentials.json` and re-authenticate

**Problem:** "Gmail API not enabled"
- **Solution:** Verify Gmail API is enabled in Google Cloud Console

**Problem:** "Invalid credentials"
- **Solution:** Re-download OAuth credentials from Google Cloud Console

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
- [Gmail MCP Server (GongRzhe)](https://github.com/GongRzhe/Gmail-MCP-Server)
- [Todoist MCP Server (@hoffination)](https://www.npmjs.com/package/@hoffination/mcp-todoist)
- [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- [Claude Code MCP Guide](https://code.claude.com/docs/en/mcp)

### API Documentation
- [Gmail API](https://developers.google.com/gmail/api)
- [Todoist API](https://developer.todoist.com/rest/v2/)

---

## 🎯 Next Steps

1. ✅ **Configure Gmail MCP** following steps above
2. ✅ **Configure Todoist MCP** following steps above
3. ✅ **Test both integrations** with sample commands
4. ✅ **Explore capabilities** by asking Claude what it can do
5. ✅ **Integrate into your workflow** for productivity boost

---

**Need help?** Create an issue in this repository or consult the official MCP documentation.

**Last Updated:** 2026-01-07
