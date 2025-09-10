from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

 app=flask( folder)
folder='save'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Profile Upload</title>
</head>
<body>
    <h2>Upload Profile Image</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="profile_img" accept="image/*" required>
        <button type="submit">Upload</button>
    </form>
    <h3>Profile Image:</h3>
    <img src="{% if filename %}{{ url_for('uploaded_file', filename=filename) }}{% else %}https://ui-avatars.com/api/?name=Profile&background=cccccc&color=555555&size=180{% endif %}" style="width:180px;height:180px;border-radius:50%;border:4px solid #333;object-fit:cover;">
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    filename = None
    if request.method == 'POST':
        file = request.files['profile_img']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template_string(HTML, filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return app.send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
