# 🌐 Deploying SSE Learning Bot on Render (via GitHub)

A complete, step-by-step guide for students to deploy the **SSE Learning Bot** application on [Render](https://render.com) by connecting their GitHub repository.

---

## 📋 Table of Contents
1. [Prerequisites](#1-prerequisites)
2. [Step 1: Push Your Code to GitHub](#step-1-push-your-code-to-github)
3. [Step 2: Create a New Web Service on Render](#step-2-create-a-new-web-service-on-render)
4. [Step 3: Configure Web Service Settings](#step-3-configure-web-service-settings)
5. [Step 4: Configure Environment Variables](#step-4-configure-environment-variables)
6. [Step 5: Deploy & Verify Application](#step-5-deploy--verify-application)
7. [Post-Deployment: How Auto-Deploy Works](#post-deployment-how-auto-deploy-works)
8. [Important Free Tier Notes & FAQs](#important-free-tier-notes--faqs)
9. [Troubleshooting Common Issues](#troubleshooting-common-issues)

---

## 1. Prerequisites

Before starting the deployment, make sure you have:
1. **A GitHub Account**: [Sign up on GitHub](https://github.com/signup) if you don't have one.
2. **A Render Account**: [Sign up on Render](https://dashboard.render.com/register) using your GitHub account for seamless integration.
3. **Required API Keys**:
   - 🔑 **Google Gemini API Key**: [Get key from Google AI Studio](https://aistudio.google.com/app/apikey) (*Powers AI Professor explanations & quizzes*).
   - 🔑 **Deepgram API Key**: [Get key from Deepgram Console](https://console.deepgram.com/signup) (*Powers voice speech-to-text and avatar voice synthesis*).
   - *(Optional)* **Tavily API Key**: [Get key from Tavily](https://tavily.com) (*For live web topic search*).
   - *(Optional)* **OpenRouter API Key**: [Get key from OpenRouter](https://openrouter.ai/keys) (*For topic synthesis*).

---

## Step 1: Push Your Code to GitHub

Your repository on GitHub will serve as the source code provider for Render.

### 1.1 Check `.gitignore` (Safety First 🔒)
Make sure your local `.gitignore` file includes `.env` and `venv` so you never commit secret keys or heavy local packages to GitHub.

Ensure your `.gitignore` file contains:
```gitignore
.env
venv/
__pycache__/
.session_cache.json
```

### 1.2 Push Local Code to GitHub
Open your terminal (PowerShell / Command Prompt / Terminal) inside your project directory (`SSE-Learning-Bot`) and run:

```bash
# 1. Initialize git repository (if not already done)
git init

# 2. Add all files and commit
git add .
git commit -m "Initial commit - Ready for Render deployment"

# 3. Rename default branch to main
git branch -M main

# 4. Link to your remote GitHub repository
# Replace <YOUR_GITHUB_USERNAME> and <YOUR_REPO_NAME> with your actual GitHub details
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git

# 5. Push code to GitHub
git push -u origin main
```

---

## Step 2: Create a New Web Service on Render

1. Log into your **[Render Dashboard](https://dashboard.render.com)**.
2. Click the blue **`New +`** button at the top right of the dashboard.
3. Select **`Web Service`** from the drop-down menu.
4. Under **"Connect a repository"**, select your GitHub account.
5. Search for your repository **`SSE-Learning-Bot`** (or whatever name you gave it on GitHub) and click **`Connect`**.

---

## Step 3: Configure Web Service Settings

Render will ask you to fill in details for your new Web Service. Configure them as follows:

| Field | Setting / Value | Notes |
| :--- | :--- | :--- |
| **Name** | `sse-learning-bot` | *(Or any custom name you prefer)* |
| **Language / Runtime** | `Python 3` | Render automatically detects Python |
| **Branch** | `main` | Select the branch you pushed your code to |
| **Region** | Select closest to you | e.g. *Oregon (US West)*, *Singapore*, or *Frankfurt* |
| **Root Directory** | `SSE-Learning-Bot` | ⚠️ **Required**: Set this if your code is inside the `SSE-Learning-Bot` subfolder |
| **Build Command** | `pip install --upgrade pip && pip install -r requirements.txt` | Installs FastAPI, Uvicorn, Deepgram, etc. |
| **Start Command** | `uvicorn backend.main:app --host 0.0.0.0 --port $PORT` | ⚠️ **Crucial**: Uses dynamic `$PORT` provided by Render |
| **Instance Type** | **Free** | $0/month free tier |

> 📁 **CRITICAL ROOT DIRECTORY NOTE**:  
> Because your repository contains the code inside a subfolder named `SSE-Learning-Bot`, you **MUST** set **Root Directory** to `SSE-Learning-Bot` in Render.  
> This allows Render to locate `requirements.txt` and `backend/main.py`.

> ⚠️ **IMPORTANT START COMMAND NOTE**:  
> Render dynamically assigns a web port using the `$PORT` environment variable. Ensure your **Start Command** is exact:  
> `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

---

## Step 4: Configure Environment Variables

Scroll down to the **Environment Variables** section on the same setup screen (or go to the **Environment** tab on the left sidebar).

Add the following keys and values:

### 🔑 Required Environment Variables

| Environment Key | Recommended Value | Description |
| :--- | :--- | :--- |
| `PYTHON_VERSION` | `3.11.9` | Sets the Python version on Render server |
| `GEMINI_API_KEY` | `AIzaSy...` *(Your actual key)* | Google Gemini API Key |
| `GEMINI_MODEL` | `gemini-1.5-flash` | LLM model for teaching lessons & quizzes |
| `DEEPGRAM_API_KEY` | `your_deepgram_api_key_here` | Deepgram API Key for STT & TTS |
| `DEEPGRAM_STT_MODEL` | `nova-3` | Voice-to-text microphone model |
| `DEEPGRAM_TTS_MODEL` | `aura-asteria-en` | Avatar voice model (*aura-asteria-en*, *aura-luna-en*, *aura-arcas-en*) |

### 💡 Optional Environment Variables (For Topic Search)

| Environment Key | Value | Description |
| :--- | :--- | :--- |
| `TAVILY_API_KEY` | `tvly-...` *(Your key)* | Live web topic searching |
| `OPENROUTER_API_KEY` | `sk-or-...` *(Your key)* | OpenRouter model synthesis |
| `OPENROUTER_MODEL` | `nvidia/llama-3.1-nemotron-70b-instruct:free` | Model choice for search synthesis |

---

## Step 5: Deploy & Verify Application

1. Click the blue **`Create Web Service`** button at the bottom.
2. Render will start the **Build & Deploy** process. You can monitor the real-time logs in the dashboard console.
3. You will see progress steps:
   - Cloning repository...
   - Installing dependencies (`pip install -r requirements.txt`)...
   - Build successful 🎉
   - Starting service (`uvicorn backend.main:app --host 0.0.0.0 --port $PORT`)...
   - **`Application startup complete.`**
4. Once the status shows **`Live`** (with a green checkmark), copy your application URL from the top left corner:
   👉 **`https://sse-learning-bot.onrender.com`** (your specific URL name).

### 🧪 Test Your Deployed Application:
1. Click your live `onrender.com` URL in your browser.
2. Verify the **SSE Learning Bot Dashboard** loads with dark mode UI.
3. Upload a sample study file (PDF/DOCX/TXT) or type a study topic.
4. Select **📖 Teach Me** and click **Start Learning Session**.
5. Test avatar audio playback and microphone voice interactions.

---

## Post-Deployment: How Auto-Deploy Works

Render enables **Auto-Deploy** by default for GitHub repositories:
- Whenever you make changes to your local code, simply commit and push to GitHub:
  ```bash
  git add .
  git commit -m "Updated UI styling / added new feature"
  git push origin main
  ```
- Render will automatically detect the new commit on GitHub, re-build your application, and update your live site without any downtime!

---

## Important Free Tier Notes & FAQs

### 1. 💤 Cold Starts (15-Minute Sleep Mode)
- **Behavior**: On Render's Free tier, if your app receives no web requests for 15 minutes, Render puts the server to sleep to save resources.
- **What to expect**: The next time someone visits your URL, the app will take **30 to 50 seconds** to start up (cold start). Subsequent pages and voice API calls will be instant.

### 2. 🔒 Free HTTPS / SSL
- Render automatically generates a free SSL/TLS certificate for your app (`https://`).
- WebSockets (`wss://`) and browser microphone permissions work natively on `https://` without any extra setup.

### 3. 💾 Ephemeral Disk Storage
- Render free web services have an ephemeral file system. Any sessions cached in local JSON files will reset if the web service restarts or re-deploys. All live API responses and study sessions during an active browser session function normally.

---

## Troubleshooting Common Issues

### ❌ Issue 1: `Could not open requirements file: No such file or directory`
- **Cause**: Render is looking in the repository root folder, but your `requirements.txt` is located inside the `SSE-Learning-Bot` subfolder.
- **Solution**: Go to your Render Web Service -> **Settings** -> Scroll to **Root Directory** -> Enter `SSE-Learning-Bot` -> Click **Save Changes**. Render will automatically trigger a new deployment.

### ❌ Issue 2: Build Failed (`Failed to install requirements`)
- **Cause**: Outdated pip or incompatible package version.
- **Solution**: Ensure your **Build Command** is set to:
  `pip install --upgrade pip && pip install -r requirements.txt`
  And verify `PYTHON_VERSION` is set to `3.11.9` in Environment Variables.

### ❌ Issue 2: Service Failed to Bind to Port / Port Error
- **Cause**: Hardcoded port like `8000` in start command.
- **Solution**: Ensure your **Start Command** strictly uses `$PORT`:
  `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

### ❌ Issue 3: 500 Internal Server Error when starting session
- **Cause**: Missing or mistyped `GEMINI_API_KEY` or `DEEPGRAM_API_KEY`.
- **Solution**: Go to your Render dashboard -> Select your Web Service -> Click **Environment** on the left menu. Verify your keys have no extra spaces or quotes.

### ❌ Issue 4: Microphone Permission Denied in Browser
- **Cause**: Browser microphone access blocked.
- **Solution**: Make sure you are accessing the site via **`https://`** (not `http://`). Click the lock 🔒 icon next to the address bar in Chrome/Edge, enable Microphone permissions, and refresh.

---

## 🎯 Quick Reference Cheat Sheet

```text
Build Command:  pip install --upgrade pip && pip install -r requirements.txt
Start Command:  uvicorn backend.main:app --host 0.0.0.0 --port $PORT
Environment:    Python 3 (Set PYTHON_VERSION = 3.11.9)
Required Keys:  GEMINI_API_KEY, DEEPGRAM_API_KEY
```
