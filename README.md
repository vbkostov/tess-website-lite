# TESS Website Lite

This is a test repo for liter version of a website


# To Do

- Add a TESS Planets counter to the homepage a la https://github.com/KeplerGO/kepler-dashboard
- Fix TOC to be a sidebar 
- Clean up blog post image directory
- Add cool where is TESS pointing now CSS widget 

# How to use:

`git clone ...`

To install `poetry` you can use:
`pip install poetry --upgrade`

Then `cd` into the directory
`cd tess-website-lite`
`poetry install`

This will install all the right dependencies, in a local file so it will not clash with your other packages.

Use

`poetry run make devserver`

Navigate to http://127.0.0.1:8000/ in your browser. You can change the .md files and it will update the website as you type. ctrl + c in terminal to quit the devserver. 
