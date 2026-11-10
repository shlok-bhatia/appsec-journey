
# Day 8 - Git Workflow and Python Fundamentals

## 1. Gitignore

- .gitignore prevents unwanted files from being tracked.
- Used to ignore secrets, virtual environments and cache files.
- .env files can contain sensitive API keys.

Important commands:

```bash
git status
git check-ignore -v .env
git log --all --oneline
```

## 2. README

- README explains the purpose of a repository.
- Describes project structure and learning progress.
- It is the first document visitors usually see.

## 3. Git Branching

- A branch allows independent development.
- Main usually contains stable code.
- Feature branches hold new changes.

Commands:

```bash
git switch main
git pull origin main
git switch -c setup/gitignore-readme
git push -u origin setup/gitignore-readme
```

## 4. Pull Request

- A Pull Request proposes merging changes.
- Changes can be reviewed before merging.
- Helps teams collaborate safely.

Workflow:

Branch -> Commit -> Push -> PR -> Review -> Merge

## 5. Python Virtual Environment

Create:

```bash
python3 -m venv ~/venv
```

Activate:

```bash
source ~/venv/bin/activate
```

Deactivate:

```bash
deactivate
```

- A virtual environment isolates Python packages.
- Prevents dependency conflicts between projects.

## 6. Requests Library

Install:

```bash
pip install requests
```

Example:

```python
import requests

r = requests.get("https://httpbin.org/get")
print(r.status_code)
print(r.text[:200])
```

- requests.get() sends an HTTP GET request.
- status_code returns the HTTP status.
- text returns the response body.

## 7. HTTP Status Codes

- 200: OK
- 201: Created
- 301: Permanent redirect
- 302: Temporary redirect
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

## 8. What I Learned

- How to use .gitignore.
- How to protect secret files from being committed.
- How to write a professional README.
- How to create Git branches and Pull Requests.
- How to create and activate a Python virtual environment.
- How to install and use the requests library.
- How to inspect HTTP status codes.
