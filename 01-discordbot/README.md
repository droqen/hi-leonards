# Leonard Discord Bot

_This readme and significant amounts of code produced using genAI as part of a particular process. I never use this stuff for my 'real' works, but I am for this and similar experiments which are not intended to be released in any official sense._

Welcome to the Leonard Discord Bot repository! This bot is designed to interact with users on Discord with a unique typing effect that simulates natural pauses, making conversations feel more lifelike.

## Features

- **Natural Typing Effect**: Leonard speaks with pauses based on punctuation, creating a more human-like interaction.
- **Custom Messages**: Users can make Leonard say custom phrases using the `!leonard` command followed by their message.

## Commands

- `!leonard [message]`: Makes Leonard speak. If no message is provided, Leonard will say a default greeting. If a message is provided, Leonard will type out the custom text with natural pauses.

## Installation

1. **Clone the Repository**: 
   ```bash
   git clone {pii removed}
   cd {pii removed}
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install discord.py
   ```

3. **Set Up Your Bot Token**:
   - Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy the bot token.
   - Create file `secret.py` with `BOT_TOKEN={your own bot token}`.

4. **Run the Bot**:
   ```bash
   python discord_bot.py
   ```

## Usage

Invite the bot to your Discord server using the invite link generated in the Discord Developer Portal. Once the bot is online, use the `!leonard` command to interact with it.

---
*Leonard is typing...*
