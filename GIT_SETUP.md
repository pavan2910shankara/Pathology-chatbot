# Connect This Project to Git

## 1. Install Git

1. Download Git for Windows: https://git-scm.com/download/win  
2. Run the installer. Use default options (including "Git from the command line and also from 3rd-party software").  
3. Close and reopen PowerShell or your terminal so `git` is recognized.

## 2. Initialize the Repository (first time only)

Open PowerShell and run:

```powershell
cd "c:\Users\PAVANKUMAR.M\Documents\Pathology - chatbot"
git init
git add .
git commit -m "Initial commit: Pathology FAQ chatbot with audio"
```

## 3. Connect to GitHub (or another remote)

### Option A: Create a new repo on GitHub

1. Go to https://github.com/new  
2. Create a repository (e.g. `pathology-faq-chatbot`). **Do not** add a README, .gitignore, or license if you already have files.  
3. Copy the repository URL (e.g. `https://github.com/YourUsername/pathology-faq-chatbot.git`).

Then run:

```powershell
git remote add origin https://github.com/pavan2910shankara/Pathology-chatbot.git
git branch -M main
git push -u origin main
```

### Option B: Use SSH (if you use SSH keys)

```powershell
git remote add origin git@github.com:pavan2910shankara/Pathology-chatbot.git
git branch -M main
git push -u origin main
```

## 4. After the first push

- **Push changes:** `git add .` → `git commit -m "Your message"` → `git push`  
- **Pull updates:** `git pull`

## Notes

- The `.gitignore` file is already in the project so Python cache and common IDE/OS files are not committed.  
- The `audio/` folder and `faq_data.js` are **included** by default. If the repo gets too large, you can add `audio/*.mp3` to `.gitignore` and regenerate audio with `python build_faq_data.py` after clone.
