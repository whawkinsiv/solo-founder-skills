# Claude Code Prompt Improver

A simple tool that helps you write better prompts for Claude Code. Instead of vague requests like "add login," it transforms them into detailed, specific instructions that get better results.

## What This Does

When you type a quick, rough idea like:

> "add user auth"

The prompt improver rewrites it into something Claude Code can execute much more effectively:

> "Add email/password authentication with the following:
> - Create login and register routes using the existing patterns in routes/
> - Use bcrypt for password hashing
> - Add session middleware for persistent login
> - Protect the /dashboard route to require authentication
> - Think hard about the security approach before implementing
> - Test by creating a user, logging in, and verifying protected routes work
> - Commit when complete"

## Installation

### Step 1: Open Your Project in the Terminal

First, navigate to your project folder. This is the folder where your code lives.

**On Mac:**
1. Open the Terminal app (search for "Terminal" in Spotlight)
2. Type `cd ` (with a space after it)
3. Drag your project folder from Finder into the Terminal window
4. Press Enter

**On Windows:**
1. Open your project folder in File Explorer
2. Click in the address bar at the top
3. Type `cmd` and press Enter
4. A command prompt will open in that folder

**In Replit:**
1. Open your Repl
2. Click the "Shell" tab at the bottom (not "Console")

### Step 2: Create the Commands Folder

Copy and paste this entire command, then press Enter:

```bash
mkdir -p .claude/commands
```

This creates a hidden folder where Claude Code looks for custom commands.

> **Note:** You won't see this folder in your regular file browser because it starts with a dot (.) which makes it hidden. That's normal!

### Step 3: Download the Command Files

You have two options:

**Option A: Copy-Paste Method (Easiest)**

1. Create a new file called `improve-prompt.md` inside the `.claude/commands` folder
2. Copy the contents from the `improve-prompt.md` file provided with this README
3. Save the file

To create the file from the terminal:

```bash
nano .claude/commands/improve-prompt.md
```

Then paste the contents, press `Ctrl+O` to save, and `Ctrl+X` to exit.

**Option B: If You Downloaded This as a Zip**

If you downloaded these files as a folder, copy them to the right place:

```bash
cp improve-prompt.md .claude/commands/
cp p.md .claude/commands/
```

### Step 4: Verify It Worked

Start Claude Code in your project:

```bash
claude
```

Then type `/` and you should see `/project:improve-prompt` in the list.

If you see it, you're all set! 🎉

## How to Use

### Basic Usage

1. Start Claude Code in your project folder:
   ```bash
   claude
   ```

2. Instead of typing your rough prompt directly, use the improver:
   ```
   /project:improve-prompt add a contact form that sends emails
   ```

3. Claude will output an improved, detailed version of your prompt

4. Copy that improved prompt and use it (or just continue—Claude will execute the improved version)

### Examples

| You Type | What Happens |
|----------|--------------|
| `/project:improve-prompt add dark mode` | Gets improved to specify toggle location, color variables, persistence method, etc. |
| `/project:improve-prompt build a todo app` | Gets improved with specific components, data structure, CRUD operations, and testing steps |
| `/project:improve-prompt make it faster` | Gets improved to specify profiling steps, metrics to measure, and optimization techniques |

## Making Commands Available in All Projects

By default, these commands only work in the project where you installed them. To make them available everywhere:

### Step 1: Create the Global Commands Folder

```bash
mkdir -p ~/.claude/commands
```

### Step 2: Copy the File There

```bash
cp .claude/commands/improve-prompt.md ~/.claude/commands/
```

### Step 3: Use with `/user:` Prefix

Now in any project, you can use:
```
/user:improve-prompt your rough prompt here
```

## Troubleshooting

### "Command not found" when typing `/project:improve-prompt`

- Make sure you created the folder in the right place. It should be `.claude/commands/` inside your project folder (note the dot at the start)
- Make sure the file is named exactly `improve-prompt.md` (not `improve-prompt.md.txt` or similar)
- Try restarting Claude Code

### "I can't see the .claude folder"

That's normal! Folders starting with a dot are hidden by default.

**To see hidden folders on Mac:**
- In Finder, press `Cmd + Shift + .` (period)

**To see hidden folders on Windows:**
- In File Explorer, click View → Show → Hidden items

**In Replit:**
- Click the three dots menu in the Files panel
- Select "Show hidden files"

### "The improved prompt isn't very good"

The prompt improver works best when you give it some context. Instead of:
- ❌ `fix bug`

Try:
- ✅ `fix bug where form doesn't submit`
- ✅ `fix the login button not working on mobile`

The more context you provide, the better the improvement.

## Customizing the Commands

Feel free to edit the `.md` files to match your preferences! For example, you might want to:

- Add your preferred frameworks or libraries
- Include your team's coding conventions
- Add project-specific patterns

Just edit the files in `.claude/commands/` and the changes take effect immediately.

## What's Included

| File | Purpose |
|------|---------|
| `improve-prompt.md` | The prompt improver command |
| `README.md` | This guide |

## Need Help?

If you're stuck, you can ask Claude Code itself for help:

```
How do I set up custom slash commands?
```

Or check the official Claude Code documentation at [docs.anthropic.com](https://docs.anthropic.com).
