# AI_WORK_AND_LEARN
AI project for me to work and learn AI and ML but also working in a fake project structure including a repo, pipeline, possible orchestration, jira

## Random Python tips and resolved issues

### Pip install in Jupyter
```
pip install "numpy<2.0"
     ^ 

SyntaxError: invalid syntax
```

When trying to run pip install "numpy<2.0" in a cell in jupyter give error pip install "numpy<2.0".

In a Jupyter notebook cell, you need to prefix shell commands like `pip install` with an exclamation mark (`!`) so that the notebook knows to run it as a system command rather than Python code.

### A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.2 as it may crash

This error is happening because NumPy 2.0 introduced breaking changes to its internal structure (specifically its C-API), which means that any libraries compiled against NumPy 1.x may not work properly with 2.x unless they’ve been recompiled or updated

🧠 What’s Going On?

Some libraries (like OpenCV, pandas, or scikit-learn) include compiled C extensions that depend on NumPy’s internal structure.

If those libraries were built using NumPy 1.x, they expect a certain binary layout.

NumPy 2.0 changed that layout—so running those older builds with NumPy 2.x can cause crashes or incompatibility errors.

🛠️ How to Fix It

✅ Option 1: Downgrade NumPy

If your other libraries haven’t been updated for NumPy 2.x yet, the safest fix is to downgrade:
`pip install "numpy<2.0"`

✅ Option 2: Reinstall All Dependencies

If you want to keep NumPy 2.x, you’ll need to reinstall or upgrade all libraries that depend on it so they’re compiled against the new version:

`pip install --force-reinstall --upgrade pandas scikit-learn opencv-python`
✅ Option 3: Use a Virtual Environment

To avoid future conflicts, always work in a clean virtual environment:
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
🔍 How to Check Compatibility in the Future

Check PyPI: Look at the library’s page on pypi.org and scroll to the “Requires” section.

Read Release Notes: Libraries often mention NumPy compatibility in their changelogs.

Use pipdeptree: This tool shows dependency trees and version conflicts:

```
pip install pipdeptree
pipdeptree
```