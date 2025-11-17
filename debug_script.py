import os
from github import Github
from google import genai

# Environment Variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BUILD_LOG_PATH = os.getenv("BUILD_LOG") # .buildozer/android/.../log.txt

# GitHub aur Gemini Client setup
g = Github(GITHUB_TOKEN)
repo = g.get_repo(os.environ.get('GITHUB_REPOSITORY'))
client = genai.Client(api_key=GEMINI_API_KEY)
model_name = 'gemini-2.5-flash' 

def get_log_content(path):
    """Log file se aakhri 200 lines (jahan error hota hai) padhta hai."""
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        return "".join(lines[-200:]) # Sirf aakhri 200 lines dekhen
    except Exception as e:
        return f"Error reading log file: {e}"

def run_gemini_diagnosis(log_content):
    """Gemini API ko call karke error diagnose karta hai."""
    
    prompt = f"""
    Aap KivyMD/Buildozer ke expert hain.
    Neeche diye gaye Android build log ko dekhen.
    Mera maqsad APK banana hai, lekin build fail ho gaya hai.
    
    1. Error ki **asli wajah** (root cause) kya hai? (Masalan: Missing dependency, wrong version, ya Kivy code bug)
    2. Ise theek karne ke liye **sabsay behtareen fix** kya hai? (Code change ya buildozer.spec change)
    
    Yahi diagnosis aur fix mujhe seedhe GitHub Pull Request mein comment karna hai.

    BUILD LOG (Last 200 lines):
    {log_content}
    """
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Gemini API Call Failed: {e}"

if __name__ == "__main__":
    log_content = get_log_content(BUILD_LOG_PATH)
    
    if not log_content or "Error reading log file" in log_content:
        # Agar log file bhi na mile to GitHub Issue bana den
        repo.create_issue(
            title="⚠️ CRITICAL: Build Log Not Found for Gemini Diagnosis",
            body="The build failed, and the log file could not be accessed for Gemini analysis."
        )
        sys.exit(1)

    diagnosis = run_gemini_diagnosis(log_content)
    
    # Diagnosis ko seedhe GitHub Issues mein post karen
    issue_title = f"🤖 KivyMD Build Failure Diagnosis by Gemini"
    issue_body = f"## 🧠 Gemini Build Diagnosis\n\n**Build Failed on Commit:** `{os.environ.get('GITHUB_SHA')}`\n\n---\n\n{diagnosis}\n\n---\n\n*Yeh diagnosis Gemini AI ne build log ki buniyad par kiya hai.*"
    
    repo.create_issue(title=issue_title, body=issue_body)
    print("Diagnosis posted to GitHub Issues.")
