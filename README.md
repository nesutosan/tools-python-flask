# Repository นี้ เป็นส่วนหนึ่งที่มาจากบทความใน Medium ตาม Link ด้านล่างนี้
> https://medium.com/@nesutosan/chatgpt-คุยกับน้อนยังไงให้ได้งาน-bb58c13bbfa4

# Toolkits

This is a Flask application that provides various tools to enhance your experience.

## Installation

To use this application, you need to have Python 3 installed on your system. You can download it from the official website: https://www.python.org/downloads/.

```
pip install -r requirement.txt
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/nesutosan/tools-python-flask.git
```

2. Change into the project directory:

```bash
cd tools-python-flask
```

3. Install the required Python packages:

```bash
pip install -r requirement.txt
```

4. Run the Flask application:

```javascript
export FLASK_APP=app.py
flask run
```

5. Open your web browser and go to http://localhost:5000 to use the application.

## Customization

You can customize the user interface of the application by modifying the CSS files. The application is currently using the Bootstrap 4 CSS files.

To modify the CSS, you need to download and extract the Bootstrap 4 files from the official website: https://getbootstrap.com/docs/4.0/getting-started/download/.

Then, move the css, js, and fonts directories from the extracted Bootstrap 4 files into the static directory of your Flask application.

Finally, modify the CSS files to customize the appearance of the application.

## File Structure

The file structure of the application is as follows:

```python
tools-python-flask/
├── app.py
├── static/
│   ├── css/
│   │   └── bootstrap.min.css
│   ├── fonts/
│   ├── js/
│   │   └── bootstrap.min.js
│   └── style.css
└── templates/
    ├── 404.html
    ├── base.html
    ├── error.html
    ├── index.html
    ├── merge.html
    ├── pdf.html
    ├── qrcode.html
    └── split.html
```

The `app.py` file contains the Flask application code.

The `static` directory contains the CSS and JavaScript files.

The `templates` directory contains the HTML templates for the application.

## Credits

This application was created by `ChatGPT` 70%.
