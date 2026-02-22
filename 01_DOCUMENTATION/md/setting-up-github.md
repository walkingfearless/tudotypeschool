# Setting Up GitHub

A step-by-step guide for workshop students — from creating an account to submitting your first project.

---

## What is GitHub?

GitHub is a platform for storing and sharing files using **Git**, a version control system. In this workshop we use it to distribute teaching materials and collect student projects. Think of it as a shared folder that keeps a full history of every change you make.

---

## Step 1 — Create a GitHub Account

1. Go to [github.com](https://github.com) and click **Sign up**
2. Choose a username, enter your email address and a password
3. Verify your email when prompted
4. The free plan is all you need — do not subscribe to any paid tier

**Username tip:** use something professional and recognisable, such as `firstname-lastname` or `flastname`. This will be part of your public profile URL.

---

## Step 2 — Install GitHub Desktop

GitHub Desktop is a visual application that lets you manage your work without using the command line.

1. Download it from [desktop.github.com](https://desktop.github.com)
2. Install and open it
3. Sign in with your GitHub account when prompted

---

## Step 3 — Clone the Workshop Repository

Cloning creates a local copy of the repository on your computer.

1. In GitHub Desktop, go to **File → Clone Repository**
2. Click the **URL** tab
3. Paste the repository URL provided by your instructor
4. Choose where to save it on your computer (e.g. `Documents/UAlg-TypeWorkshop`)
5. Click **Clone**

You now have a full local copy of all workshop materials.

---

## Step 4 — Set Up Your Project Folder

All student projects live inside `02-UAlg-Type-Workshop/03_PROJECTS/`. A template folder is provided for you to copy.

1. Open the `03_PROJECTS/` folder on your computer
2. Find the folder named `_TEMPLATE`
3. Duplicate it (copy and paste — do not move or rename the original)
4. Rename your copy using the format `firstname-lastname` — for example: `ana-silva`
5. Open `README.md` inside your folder and fill in your name, project name, and a brief description of what you intend to design

Your folder contains four subfolders:

| Folder | What goes here |
|---|---|
| `sources/` | Working files — Fontra, UFO, Glyphs |
| `exports/` | Compiled fonts — TTF, OTF, variable |
| `proofs/` | PDF specimens, test prints, proof sheets |
| `references/` | Sketches, scans, reference images |

---

## Step 5 — Commit and Push Your Work

Committing saves a snapshot of your changes. Pushing sends them to GitHub.

1. Open GitHub Desktop — your changed files appear listed on the left
2. Write a short description in the **Summary** field — for example: `Add initial H and O drawings`
3. Click **Commit to main**
4. Click **Push origin** (top right) to upload your changes to GitHub

Repeat this whenever you make meaningful progress. Treat commits like save points.

---

## File Rules

**Allowed — commit freely:**

- Font source files: `.fontra`, `.ufo`, `.glyphs`, `.designspace`
- Compiled fonts: `.ttf`, `.otf`
- Proofs and specimens: `.pdf`
- Reference images: `.jpg`, `.png`, `.svg`

**Not allowed — do not commit:**

- Adobe source files: `.ai`, `.psd`, `.indd` — these can be hundreds of megabytes
- Video files: `.mp4`, `.mov`, `.avi`
- Compressed archives: `.zip`, `.rar`
- Any single file larger than 50 MB

If you are unsure whether a file is suitable, ask your instructor before committing.

---

## Useful Tips

- **Pull before you work:** before starting a session, click **Fetch origin** in GitHub Desktop to download any updates from your instructor
- **Commit often:** small, frequent commits are much easier to review than one large upload at the end of the semester
- **Write clear summaries:** `Add weight axis test` is more useful than `update` or `changes`
