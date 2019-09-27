# Valhalla Discord Utilities

## Setup

Create a .env file in the same directory as main.py, put your bot token in there

```
# .env
DISCORD_TOKEN={your-bot-token}
DISCORD_GUILD={your-guild-name}
```

Install the dependencies:

```
py -3 -m pip install -U discord.py, python-dotenv
```

## Running 

```
py main.py
```

## Usage

!valhalla {command}

Example:

```
!valhalla list-missing-roles
```
