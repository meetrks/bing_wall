# bing_wall

A simple python script which will scrap https://bing.com home page and get the image of the day. It will automatically set the desktop wallpaper (only for linux based os).

## Installation Guide
Pre Requirements-

- Python >= 2.7
- git

**Get the source code from git-**

`git clone https://github.com/pingrs/blog.git`

**Create virtual environment and install dependencies-**
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
**Set crontab to execute the script everyday mid night-**

`0 0 * * * cd your_project_path && source env/bin/activate && python bing.py`

