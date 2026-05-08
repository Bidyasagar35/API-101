# 📚 My API Learning Journey — Sagar Patra

> Started: May 2026 | Language: Python | Tools: Postman, VS Code

---

## Table of Contents

1. [What is an API?](#1-what-is-an-api)
2. [How the Internet Works (Basics)](#2-how-the-internet-works-basics)
3. [Key Concepts Every Beginner Must Know](#3-key-concepts-every-beginner-must-know)
4. [Postman — Testing APIs Without Code](#4-postman--testing-apis-without-code)
5. [Open-Meteo API — My First API (No Auth)](#5-open-meteo-api--my-first-api-no-auth)
6. [TMDB API — APIs With Authentication](#6-tmdb-api--apis-with-authentication)
7. [Python — Calling APIs With Code](#7-python--calling-apis-with-code)
8. [Understanding JSON](#8-understanding-json)
9. [URL Structure — Breaking It Down](#9-url-structure--breaking-it-down)
10. [Project Setup — VS Code + Virtual Environment](#10-project-setup--vs-code--virtual-environment)
11. [Git & GitHub — Saving and Sharing Code](#11-git--github--saving-and-sharing-code)
12. [Common Errors and How to Fix Them](#12-common-errors-and-how-to-fix-them)
13. [What's Next](#13-whats-next)

---

## 1. What is an API?

### Simple Definition
API stands for **Application Programming Interface**.

In plain English: it's a way for **two programs to talk to each other**.

### Real World Analogy — The Restaurant 🍕

Think of ordering food at a restaurant:

```
YOU  →  tell the WAITER what you want  →  KITCHEN makes it  →  WAITER brings it back  →  YOU
```

In tech terms:
```
YOUR APP  →  sends a REQUEST to the API  →  SERVER processes it  →  API sends RESPONSE  →  YOUR APP
```

- **You** = your Python script or Postman
- **Waiter** = the API
- **Kitchen** = the server/database
- **Food** = the data (JSON response)

### More Real World Examples

| Situation | What's happening behind the scenes |
|---|---|
| You check the weather on your phone | Your phone calls a Weather API |
| You log in with Google on any app | The app calls Google's Auth API |
| You pay on Swiggy | Swiggy calls a Payment API (Razorpay) |
| You see a map on Ola | Ola calls Google Maps API |
| You search a movie on Netflix | Netflix calls its own internal API |
| You get an OTP on your phone | The app calls an SMS API (Twilio) |

### Why APIs Exist

- So developers don't have to **build everything from scratch**
- You want weather data? Don't build a weather station — use a Weather API!
- You want movie info? Don't scrape websites — use TMDB API!
- APIs let companies **share data safely** without giving direct database access

---

## 2. How the Internet Works (Basics)

Before using APIs, it helps to understand how data travels on the internet.

### Request → Response Cycle

```
Your Computer                           Server
     |                                     |
     |-------- REQUEST ------------------>|
     |         "GET /movies/popular"       |
     |         Headers: api_key=xxx        |
     |                                     |
     |<-------- RESPONSE -----------------|
     |         Status: 200 OK             |
     |         Body: { "results": [...] } |
     |                                     |
```

### HTTP Methods — The Verbs of the Internet

Think of these like actions you can perform:

| Method | Real World Analogy | What it does |
|---|---|---|
| **GET** | Reading a menu | Fetch/retrieve data |
| **POST** | Placing a new order | Send new data to server |
| **PUT** | Changing your order | Update existing data |
| **DELETE** | Cancelling your order | Remove data |

In this learning journey, we mostly used **GET** (fetching data).

### Status Codes — The Server's Reply

| Code | Meaning | Real World Analogy |
|---|---|---|
| **200** ✅ | OK — Success | "Here's your order!" |
| **201** ✅ | Created — New item made | "Your account is created!" |
| **400** ❌ | Bad Request — You sent wrong data | "We don't have that dish" |
| **401** 🔑 | Unauthorized — Wrong/missing API key | "Members only area" |
| **404** ❌ | Not Found — Doesn't exist | "That page doesn't exist" |
| **429** ⏳ | Too Many Requests — Rate limited | "You've ordered too much, wait!" |
| **500** 💥 | Server Error — Their problem | "Kitchen is on fire!" |

---

## 3. Key Concepts Every Beginner Must Know

### API Key 🔑

A unique password the API gives you to identify who you are.

```
Without API Key:  "Who are you? No access!"
With API Key:     "Welcome Sagar! Here's your data."
```

Real example — TMDB API key looks like:
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

> Always keep your API key **secret** — never share it publicly or push it to GitHub!

### Endpoint 🎯

The specific URL address for a particular piece of data.

```
Base URL:   https://api.themoviedb.org/3
Endpoint:   /search/movie
Full URL:   https://api.themoviedb.org/3/search/movie
```

Think of it like a building address:
- Base URL = the building (`themoviedb.org`)
- Endpoint = the specific room (`/search/movie`)

### Query Parameters 🔍

Extra information you add to the URL to filter or customize your request.

```
https://api.themoviedb.org/3/search/movie?query=Baahubali&language=en-US
                                          ^               ^
                                    first param      second param (separated by &)
```

Real world analogy — like filters on Swiggy:
```
Swiggy: "Pizza" + filter: "under 200" + filter: "4 star and above"
API:     query=pizza  &  max_price=200  &  min_rating=4
```

### Headers 📋

Extra information sent with your request — like metadata on an envelope.

Common headers:
```
Content-Type: application/json    → "I'm sending JSON data"
Authorization: Bearer YOUR_TOKEN  → "Here's my identity proof"
Accept: application/json          → "Please send back JSON"
```

### JSON — The Language of APIs 🗣️

APIs respond in JSON (JavaScript Object Notation). It looks exactly like a Python dictionary.

```json
{
  "name": "Sagar",
  "city": "Hyderabad",
  "skills": ["Python", "API", "Git"],
  "learning": true
}
```

---

## 4. Postman — Testing APIs Without Code

### What is Postman?

A free desktop app that lets you call any API by **clicking buttons** — no coding needed. It's the most popular tool for testing APIs.

Think of Postman as a **remote control for APIs**.

### The 5 Most Important Tabs

#### 1. Params Tab
Add query parameters without manually editing the URL.

```
Key              Value
-----------      ------------------
latitude    →    17.3850
longitude   →    78.4867
city        →    Hyderabad
```

Postman automatically builds:
```
?latitude=17.3850&longitude=78.4867&city=Hyderabad
```

#### 2. Authorization Tab
Add your API key securely.

- Type: **API Key** → adds key to header or params
- Type: **Bearer Token** → for OAuth tokens (advanced)

#### 3. Headers Tab
Add custom headers manually.

```
Key                    Value
-------------------    ---------------------
Content-Type      →    application/json
Accept            →    application/json
```

#### 4. Body Tab
Send data with POST requests (only needed for POST/PUT).

Select **raw** → **JSON** → type your data:
```json
{
  "title": "My Movie Review",
  "rating": 9
}
```

#### 5. Tests Tab
Write checks to verify the response automatically.

```javascript
pm.test("Status is 200", function() {
    pm.response.to.have.status(200);
});
```

### Environments & Variables — Pro Tip 🔥

Instead of pasting your API key in every request:

1. Create an Environment called `My APIs`
2. Add variable: `tmdb_key` = `your_actual_key`
3. Use `{{tmdb_key}}` anywhere in your requests

Benefits:
- Change the key in one place and it updates everywhere
- Never accidentally expose your key in shared collections

### Collections — Organize Your Work 📁

Group related requests into Collections like folders:

```
📁 Weather APIs
   └── 🌤️ Current Weather Hyderabad
   └── 📅 7-Day Forecast
📁 TMDB Movie APIs
   └── 🔍 Search Movie
   └── 🎬 Get Movie Details
   └── 🔥 Trending Today
```

### The Code Button — Bridge to Python 🌉

Once your request works in Postman:
1. Click `</>` icon (right side of the screen)
2. Select **Python - Requests**
3. Copy the generated code directly into your Python file!

---

## 5. Open-Meteo API — My First API (No Auth)

### What is Open-Meteo?

A completely free weather API — no sign-up, no API key needed. Perfect for beginners!

Website: `open-meteo.com`

### The Request I Built

```
GET https://api.open-meteo.com/v1/forecast
    ?latitude=17.3850
    &longitude=78.4867
    &current_weather=true
    &daily=temperature_2m_max,temperature_2m_min
    &forecast_days=7
    &timezone=Asia/Kolkata
```

Breaking down each parameter:

| Parameter | Value | Why |
|---|---|---|
| `latitude` | `17.3850` | Hyderabad's GPS latitude |
| `longitude` | `78.4867` | Hyderabad's GPS longitude |
| `current_weather` | `true` | Include live weather right now |
| `daily` | `temperature_2m_max,temperature_2m_min` | Get max and min temp each day |
| `forecast_days` | `7` | Get 7 days of forecast |
| `timezone` | `Asia/Kolkata` | Return times in IST |

### The Response — Explained

```json
{
  "latitude": 17.375,
  "longitude": 78.5,
  "timezone": "Asia/Kolkata",
  "elevation": 515.0,

  "current_weather": {
    "temperature": 36.2,
    "windspeed": 14.5,
    "winddirection": 230,
    "weathercode": 0,
    "is_day": 1,
    "time": "2026-05-08T14:00"
  },

  "daily_units": {
    "temperature_2m_max": "°C",
    "temperature_2m_min": "°C"
  },

  "daily": {
    "time":               ["2026-05-08", "2026-05-09", "2026-05-10"],
    "temperature_2m_max": [38.1,          39.2,          37.8],
    "temperature_2m_min": [26.3,          27.1,          25.9]
  }
}
```

Key insight — the `daily` arrays are **index-matched**:

```
Index:               0            1            2
time:          2026-05-08   2026-05-09   2026-05-10
max_temp:          38.1         39.2         37.8
min_temp:          26.3         27.1         25.9
```

Think of it like 3 columns in a spreadsheet — same row number = same day!

### Weather Codes Cheat Sheet

| Code | Weather |
|---|---|
| 0 | Clear sky ☀️ |
| 1–3 | Partly cloudy ⛅ |
| 45, 48 | Foggy 🌫️ |
| 61–67 | Rain 🌧️ |
| 80–82 | Rain showers 🌦️ |
| 95 | Thunderstorm ⛈️ |

### What I Learned

- How to find coordinates (latitude/longitude) for any city
- APIs snap your coordinates to the nearest grid point (17.385 → 17.375) — this is normal
- `daily_units` tells you the unit (°C, km/h etc.) — always check this!
- Arrays in responses are often index-matched like spreadsheet columns

---

## 6. TMDB API — APIs With Authentication

### What is TMDB?

The Movie Database — a massive free database of movies, TV shows, actors, and more.

Website: `themoviedb.org`

### Getting Your API Key (Step by Step)

1. Go to `themoviedb.org` → Sign up for free
2. Click profile icon → **Settings** → **API**
3. Click **Create** → choose **Developer**
4. Fill the form (App name: `My Movie App`, Type: Personal)
5. You get two things:

```
API Key (v3):      a1b2c3d4e5f6...   ← 32 characters — use this!
Access Token (v4): eyJhbGci...       ← Very long JWT token (advanced)
```

We use **API Key (v3)** — simpler for beginners.

### Two Ways to Send Your API Key

#### Method 1 — Query Parameter (Easy, good for learning)
```
https://api.themoviedb.org/3/search/movie?api_key=YOUR_KEY&query=Inception
```

#### Method 2 — Authorization Header (Secure, for real projects)
```
Header Key:   Authorization
Header Value: Bearer YOUR_ACCESS_TOKEN
```

> Headers are more secure because URLs get stored in server logs.
> Your key in the URL = visible in those logs!

### Key Endpoints I Learned

#### Search for a Movie
```
GET https://api.themoviedb.org/3/search/movie
    ?api_key={{tmdb_key}}
    &query=Baahubali
    &language=en-US
```

#### Get Full Movie Details by ID
```
GET https://api.themoviedb.org/3/movie/27205
    ?api_key={{tmdb_key}}
```

#### Get Trending Movies Today
```
GET https://api.themoviedb.org/3/trending/movie/day
    ?api_key={{tmdb_key}}
```

#### Get Movie Cast & Crew
```
GET https://api.themoviedb.org/3/movie/27205/credits
    ?api_key={{tmdb_key}}
```

### Understanding the Movie Response

```json
{
  "results": [
    {
      "id": 27205,
      "title": "Inception",
      "overview": "A thief who steals corporate secrets...",
      "release_date": "2010-07-15",
      "vote_average": 8.4,
      "vote_count": 35000,
      "popularity": 98.5,
      "poster_path": "/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"
    }
  ]
}
```

#### Building the Poster Image URL

TMDB gives you a partial path — you must build the full URL yourself:

```
Base image URL:  https://image.tmdb.org/t/p/w500
poster_path:     /9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg

Full URL:        https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg
```

Image size options: `w200`, `w300`, `w500`, `w780`, `original`

### What I Learned

- Always keep API keys secret — never paste raw keys in public code
- Use Postman Environments to store keys as `{{variables}}`
- APIs often give you IDs (like `id: 27205`) that you use in follow-up requests
- Some data needs to be assembled manually (like the poster URL)
- Free tier rate limit: TMDB allows 40 requests per 10 seconds

---

## 7. Python — Calling APIs With Code

### Method 1 — Using Built-in Libraries (No install needed)

```python
import json
from urllib import parse, request

API_KEY = "your_api_key_here"
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(title):
    # Step 1: Define the endpoint
    url = f"{BASE_URL}/search/movie"

    # Step 2: Set up parameters as a dictionary
    params = {
        "api_key": API_KEY,
        "query": title,
        "language": "en-US"
    }

    # Step 3: Build the full URL
    # parse.urlencode converts dict → "api_key=xxx&query=Inception&language=en-US"
    query_string = parse.urlencode(params)
    full_url = f"{url}?{query_string}"

    # Step 4: Make the request
    with request.urlopen(full_url) as response:
        # .read()           → raw bytes (like binary data)
        # .decode("utf-8")  → converts bytes to readable string
        # json.loads()      → converts JSON string to Python dictionary
        data = json.loads(response.read().decode("utf-8"))

    # Step 5: Navigate the response
    movie = data["results"][0]  # First result (most relevant)

    # Step 6: Display results
    print(f"Title   : {movie['title']}")
    print(f"Rating  : {movie['vote_average']}/10")
    print(f"Release : {movie['release_date']}")
    print(f"Overview: {movie['overview'][:150]}...")

search_movie("Baahubali")
```

### Method 2 — Using the `requests` Library (Simpler, most popular)

```bash
pip install requests
```

```python
import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title,
        "language": "en-US"
    }

    # All the urllib complexity in just one line!
    response = requests.get(url, params=params)
    data = response.json()

    movie = data["results"][0]
    print(f"Title   : {movie['title']}")
    print(f"Rating  : {movie['vote_average']}/10")

search_movie("Baahubali")
```

### Side-by-side Comparison

| Step | `urllib` (built-in) | `requests` (library) |
|---|---|---|
| Build URL params | `parse.urlencode(params)` | automatic |
| Make GET request | `request.urlopen(url)` | `requests.get(url, params=params)` |
| Read response bytes | `.read().decode("utf-8")` | automatic |
| Parse JSON | `json.loads(...)` | `.json()` |
| Lines of code | ~8 lines | ~2 lines |
| Needs install | No | `pip install requests` |

> `urllib` shows you what's happening under the hood — great for learning!
> `requests` is used in real projects — simpler and cleaner.

### Viewing the Movie Poster

```python
import webbrowser
import urllib.request
import os

poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"

# Option 1 — Open directly in browser (easiest!)
webbrowser.open(poster_url)

# Option 2 — Download and open in image viewer
urllib.request.urlretrieve(poster_url, "poster.jpg")
os.startfile("poster.jpg")          # Windows
# os.system("open poster.jpg")      # Mac
# os.system("xdg-open poster.jpg")  # Linux
```

---

## 8. Understanding JSON

JSON is the **universal language of APIs**. Every API response comes in JSON format.

### JSON Data Types

```json
{
  "name": "Sagar",                        <- String (text in quotes)
  "age": 25,                              <- Number (no quotes)
  "is_learning": true,                    <- Boolean (true/false)
  "score": null,                          <- Null (empty/unknown)
  "skills": ["Python", "API", "Git"],     <- Array (list of items)
  "address": {                            <- Object (nested dictionary)
    "city": "Hyderabad",
    "country": "India"
  }
}
```

### Accessing JSON in Python

```python
data = response.json()

# Access a string value
name = data["name"]                    # "Sagar"

# Access a nested object
city = data["address"]["city"]         # "Hyderabad"

# Access a specific array item
first_skill = data["skills"][0]        # "Python"
last_skill  = data["skills"][-1]       # "Git"

# Loop through an array
for skill in data["skills"]:
    print(skill)

# Access an array of objects (like TMDB search results)
first_movie = data["results"][0]
title = data["results"][0]["title"]
```

### Real TMDB Example — Step by Step

```python
data = {
    "results": [
        {"title": "Baahubali",   "vote_average": 8.1},
        {"title": "Baahubali 2", "vote_average": 8.2}
    ]
}

# Get first movie title
data["results"][0]["title"]        # "Baahubali"

# Get second movie rating
data["results"][1]["vote_average"] # 8.2

# Print all movie titles
for movie in data["results"]:
    print(movie["title"])
# Output:
# Baahubali
# Baahubali 2
```

---

## 9. URL Structure — Breaking It Down

```
https://api.themoviedb.org/3/search/movie?api_key=abc&query=Inception&language=en
\___/   \__________________/ \___________/ \______________________________________/
scheme        host               path                  query string
```

| Part | Example | Description |
|---|---|---|
| **Scheme** | `https://` | Protocol — always use https (secure) |
| **Host** | `api.themoviedb.org` | The server's address |
| **Path** | `/3/search/movie` | The specific resource you want |
| **?** | `?` | Marks the start of parameters |
| **Parameters** | `api_key=abc&query=Inception` | Key=value pairs joined by `&` |

### Rules to Remember

```
✅ No spaces around = sign:      api_key=abc         correct
❌ Never do this:                api_key = abc       wrong

✅ Use & between params:         ?a=1&b=2            correct
❌ Never do this:                ?a=1 b=2            wrong

✅ First param starts with ?:    ?api_key=abc        correct
❌ Never do this:                &api_key=abc        wrong
```

### How Postman Helps

In Postman's **Params tab**, you just fill in a table — Postman builds the correct URL automatically with all the `?`, `&`, and `=` signs. No chance of typos!

---

## 10. Project Setup — VS Code + Virtual Environment

### What is a Virtual Environment?

A virtual environment (`.venv`) is like a **separate toolbox** for each project.

**Without venv (bad — global mess):**
```
Your Mac
└── Python packages (shared globally)
    ├── requests v2.0   ← Project A needs this old version
    └── requests v3.0   ← Project B needs this new version
                           (these conflict with each other!)
```

**With venv (good — isolated per project):**
```
Your Mac
├── ProjectA/
│   └── .venv/
│       └── requests v2.0   ← Only for Project A
└── ProjectB/
    └── .venv/
        └── requests v3.0   ← Only for Project B
```

### Setting Up a Virtual Environment

```bash
# Step 1: Create the virtual environment
python -m venv .venv

# Step 2: Activate it
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows

# You'll see (.venv) appear — means it's active!
(.venv) sagarpatra@MacBook Python %

# Step 3: Install packages inside the venv
pip install requests

# Step 4: When done, deactivate
deactivate
```

### VS Code Project File Structure

```
PYTHON/
├── .venv/              <- Virtual environment (never edit manually)
│   ├── bin/            <- Python executables
│   ├── lib/            <- Installed packages live here
│   └── pyvenv.cfg      <- Venv configuration file
├── .vscode/            <- VS Code settings (auto-created by VS Code)
│   ├── settings.json   <- Editor preferences, Python interpreter path
│   └── launch.json     <- Debug run configurations
├── .gitignore          <- Tells Git what NOT to track
├── get_request.py      <- Your Python scripts
├── demo.py
└── LEARNINGS.md        <- This file!
```

### VS Code File Status Indicators

| Symbol | Color | Meaning | How to fix |
|---|---|---|---|
| `U` | Green | **Untracked** — Git doesn't know this file | `git add filename` |
| `A` | Green | **Added** — staged, ready to commit | `git commit` |
| `M` | Yellow | **Modified** — changes not yet committed | `git add` then `git commit` |
| `D` | Red | **Deleted** — file was removed | `git add` then `git commit` |
| `●` | Grey | **Unsaved** — file has unsaved changes | `Cmd+S` to save |

### Important: File Naming Rules

```
✅ get_request.py    <- Use underscores between words
❌ get request.py    <- Never use spaces in filenames!
```

Why? Spaces break terminal commands:
```bash
python get request.py    # Terminal reads "get" and "request.py" as two things
python get_request.py    # Works perfectly
```

### Renaming a File in Terminal

```bash
# If file is in current folder
mv "old name.py" new_name.py

# If file is inside a subfolder
mv ".vscode/old name.py" ./new_name.py   # also moves it to current folder
```

---

## 11. Git & GitHub — Saving and Sharing Code

### What is Git?

Git is a **version control system** — it saves snapshots of your code over time so you can go back to any version.

Real world analogy: Like Google Docs version history, but for code. Every `git commit` = a saved version you can return to.

### What is GitHub?

GitHub is a **website** where you store your Git repositories online.

```
Git    = the tool that runs on your laptop
GitHub = the cloud storage on the internet
```

### First Time Setup (Do This Once)

```bash
# Set your identity — appears on all your commits
git config --global user.name "Sagar Patra"
git config --global user.email "your@email.com"
```

### Starting a New Project With Git

```bash
# 1. Initialize git in your project folder
git init

# 2. Create .gitignore file
echo ".venv/"        > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc"        >> .gitignore

# 3. Stage all files
git add .

# 4. Save your first snapshot
git commit -m "initial commit"
```

### Connecting to GitHub & Pushing Code

```bash
# Link your local project to a GitHub repository
git remote add origin https://github.com/yourusername/your-repo.git

# Set branch name to "main"
git branch -M main

# Upload to GitHub for the first time
git push -u origin main
```

### Daily Workflow — Just 3 Commands!

```bash
# After making any changes to your code:
git add .                           # Stage all changes
git commit -m "describe the change" # Save a snapshot
git push                            # Upload to GitHub
```

### What .gitignore Does

The `.gitignore` file tells Git: **"never track these files"**

```
.venv/          <- Virtual environment (too large, OS-specific, reproducible)
__pycache__/    <- Python cache files (auto-generated, not needed)
*.pyc           <- Compiled Python files (auto-generated)
.env            <- Environment files (CONTAINS SECRET API KEYS!)
```

> Never commit your API keys to GitHub! Store them in a `.env` file and add `.env` to `.gitignore`

### Git Commands Cheat Sheet

| Command | What it does |
|---|---|
| `git init` | Start tracking a folder with Git |
| `git status` | See what files have changed |
| `git add .` | Stage all changes |
| `git add filename` | Stage one specific file |
| `git commit -m "msg"` | Save a snapshot with a message |
| `git push` | Upload commits to GitHub |
| `git pull` | Download latest changes from GitHub |
| `git log` | See history of all commits |
| `git diff` | See exactly what lines changed |

---

## 12. Common Errors and How to Fix Them

### Error 1 — "Invalid API key" 🔑

```json
{"status_message": "Invalid API key: You must be granted a valid key."}
```

**Possible causes and fixes:**

| Cause | Fix |
|---|---|
| Key not activated yet | Wait 15-30 minutes after creating it |
| Copied wrong key | Copy `API Key (v3)`, not the long access token |
| Extra spaces in key | Re-copy the key carefully using the copy button |
| Environment not selected in Postman | Check top-right dropdown — select your environment |
| Param name typo | Must be exactly `api_key` (lowercase, underscore) |

### Error 2 — "No such file or directory" 📁

```bash
mv "get [request.py]" get_request.py
# mv: No such file or directory
```

**Fix:** Hyperlinks get embedded when you copy filenames from chat. Always type filenames manually in the terminal.

### Error 3 — "ModuleNotFoundError" 📦

```
ModuleNotFoundError: No module named 'requests'
```

**Fix:** Your venv is not activated, or the package isn't installed:
```bash
source .venv/bin/activate    # activate venv first!
pip install requests          # then install the package
```

### Error 4 — "KeyError: 'results'" 🗝️

```
KeyError: 'results'
```

**Fix:** The API returned an error response instead of real data. Print the full response to see what came back:
```python
print(data)   # See the actual response — usually shows the error message
```

### Error 5 — "IndexError: list index out of range" 📋

```
IndexError: list index out of range
```

**Fix:** The search returned no results — the list is empty and `[0]` doesn't exist:
```python
if data["results"]:                    # Check list is not empty
    movie = data["results"][0]
else:
    print("No movies found! Try a different title.")
```

---

## 13. What's Next

### Short Term Goals
- [ ] Handle API errors properly with try/except blocks
- [ ] Search multiple movies and compare results
- [ ] Build a simple CLI movie search app
- [ ] Save API results to a JSON or CSV file

### Medium Term Goals
- [ ] Learn Pagination — APIs that return results across multiple pages
- [ ] Learn Rate Limiting — how to handle APIs that cap requests
- [ ] POST requests — sending data to create/update things
- [ ] Build a 7-day weather dashboard using Open-Meteo

### Advanced Goals
- [ ] OAuth 2.0 — advanced authentication used by Google, Spotify, Twitter
- [ ] `httpx` — async version of requests (faster for many simultaneous calls)
- [ ] Build your own simple API using FastAPI
- [ ] Deploy your API to the internet (Railway, Render)

### Free APIs to Explore Next

| API | What it does | Auth needed |
|---|---|---|
| Open-Meteo | Real weather data | No |
| RestCountries | Country info, flags, population | No |
| PokeAPI | All Pokémon data | No |
| NASA API | Space images, astronomy | Free key |
| NewsAPI | Latest news headlines | Free key |
| Spotify API | Music, artists, playlists | OAuth |
| GitHub API | Repository and user data | Free token |

---

## Summary — Everything I've Learned

```
APIs & HTTP
  ✅ What APIs are and why they exist
  ✅ How HTTP requests and responses work
  ✅ HTTP methods: GET, POST, PUT, DELETE
  ✅ Status codes: 200, 201, 400, 401, 404, 429, 500
  ✅ Query parameters, headers, API keys, JSON

Postman
  ✅ Making GET and POST requests
  ✅ Params, Auth, Headers, Body tabs
  ✅ Environments and variables ({{tmdb_key}})
  ✅ Collections to organize requests
  ✅ Exporting requests to Python code

APIs I Used
  ✅ Open-Meteo (free, no auth) — weather & forecast
  ✅ TMDB (API key auth) — movies, search, trending

Python
  ✅ urllib — calling APIs with built-in libraries
  ✅ requests library — simpler API calls
  ✅ Parsing JSON responses
  ✅ Viewing images (browser, download)

URL & JSON
  ✅ URL structure: scheme, host, path, query string
  ✅ URL rules: ?, &, = with no spaces
  ✅ JSON data types: string, number, boolean, array, object
  ✅ Navigating nested JSON with Python

Project Setup
  ✅ Virtual environments (.venv)
  ✅ VS Code setup and file indicators (U, A, M, ●)
  ✅ File naming rules (underscores, no spaces)
  ✅ Renaming and moving files in terminal

Git & GitHub
  ✅ git init, add, commit, push
  ✅ Connecting local repo to GitHub
  ✅ .gitignore — what to exclude
  ✅ Daily workflow: add → commit → push

Debugging
  ✅ Common API errors and how to fix them
  ✅ Reading error messages
  ✅ print(data) to debug responses
```

---

*Keep building, keep learning! Every expert was once a beginner. 🚀*

*— Sagar Patra, May 2026*
