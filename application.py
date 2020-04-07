from flask import Flask, request, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
import sqlite3

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = "SET YOUR SECRET KEY"

toolbar = DebugToolbarExtension(app)

htmlOpen = '<!DOCTYPE html>'
htmlOpen += '<html>'
htmlOpen += '<head><title>Flask Experiment</title>'
htmlOpen += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">'
htmlOpen += '<style>'
htmlOpen += 'body { max-width: 1500px; margin: auto; margin-top: 20pt;} </style>'
htmlOpen+= '</head>'
htmlOpen += '<body>'

htmlClose = '</body></html>'

@app.route('/')
def chapters_list():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM chapter")
    chapters = cur.fetchall()
    conn.close()
    output = ''
    output += htmlOpen
    output += '<div class="container-fluid">'
    output += '<div class="row"><div class="col-6">'
    output += '<h3>Experimentation in Software Engineering</h3></div>'
    output += '<div class "col-2">'
    output += '<a href="/new">Add New Chapter</a></div></div></div><hr>'
    
    for chapter in chapters:
        output += '<div class="container-fluid">'
        output += '<div class="row">'
        output += '<div class="col-1">Ch #'
        output += str(chapter['chapterNum'])
        output += ': </div><div><b>'
        output += chapter['name']
        output += '</b></div></div>'
        output += '<div>Page Number: '
        output += str(chapter['pageNum'])
        output += '</div>'
        output += '<div>Details:'
        output += chapter['description']
        output += '</div>'
        output += '<div class="row"><div class="col-1"><a href="/edit/'
        output += str(chapter['id'])
        output += '">Edit</a></div>'
        output += '<a href="/delete/'
        output += str(chapter['id'])
        output += '">Delete</a></div>'
        output += '<hr><br>'
        output += '</div>'  
    output += htmlClose 
    return output


@app.route('/new', methods=['POST', 'GET'])
def newChapter():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        chapterNum = request.form['chapterNum']
        pageNum = request.form['pageNum']
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO chapter (name, description, chapterNum, pageNum) VALUES (?, ?, ?, ?)", (name, description, chapterNum, pageNum))
        conn.commit()
        conn.close()
        return redirect(url_for('chapters_list'))
    else:
        output = ''
        output += htmlOpen
        output += '<div class="container-fluid">'
        output += '<div class="row"><div class="col-6">'
        output += '<h3>Add a Chapter</h3></div></div><hr>'
        output += '<div class="container-fluid">'
        output += '<div class="row">'
        output += '<form action="/new" method="post" class="form-inline">'
        output += '<label>Name:</label>'
        output += '<input type="text" name="name" maxlength="50" required><br>'
        output += '<label>Description:</label>'
        output += '<input type="text" name="description" maxlength="250" required><br>'
        output += '<label>Chapter Number:</label>'   
        output += '<input type="number" name="chapterNum" maxlength="50" required><br>'   
        output += '<label>Page Number:</label>'   
        output += '<input type="number" name="pageNum" maxlength="50" required><br>' 
        output += '<a><button type="submit">Save</button></a>'
        output += '<a href="/">Cancel</a>'
        output += '</form></div></div></div>'  
        output += htmlClose 
        return output


@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def update_chapter(id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM chapter WHERE id = ?", str(id))
    editedChapter = cur.fetchone()
    if request.method == 'POST':
        if request.form['editedName']:
            name = request.form['editedName']
        if request.form['editedDescription']:
            description = request.form['editedDescription']
        if request.form['editedChapterNum']:
            chapterNum = request.form['editedChapterNum']
        if request.form['editedPageNum']:  
            pageNum = request.form['editedPageNum']
        cur.execute("UPDATE chapter SET name = ?, description = ?, chapterNum = ?, pageNum = ? WHERE id = ?", (name, description, chapterNum, pageNum,str(id)))
        conn.commit()
        conn.close()
        return redirect(url_for('chapters_list'))
    else: 
        output = ''
        output += htmlOpen
        output += '<div class="container-fluid">'
        output += '<div class="row"><div class="col-6">'
        output += '<h3>Edit a Chapter</h3></div></div><hr>'
        output += '<div class="container-fluid">'
        output += '<div class="row">'
        output += '<form action="/edit/'
        output += str(editedChapter['id'])
        output += '" method="post" class="form-inline">'
        output += '<label>Name:</label>'
        output += '<input type="text" name="editedName" maxlength="50" required value="'
        output += editedChapter['name']
        output += '"><br>'
        output += '<label>Description:</label>'
        output += '<input type="text" name="editedDescription" maxlength="250" required value="'
        output += editedChapter['description']
        output += '"><br>'
        output += '<label>Chapter Number:</label>'   
        output += '<input type="number" name="editedChapterNum" maxlength="50" required value="'
        output += str(editedChapter['chapterNum'])
        output += '"><br>'   
        output += '<label>Page Number:</label>'   
        output += '<input type="number" name="editedPageNum" maxlength="50" required value="'
        output += str(editedChapter['pageNum'])
        output += '"><br>' 
        output += '<a><button type="submit">Save Changes</button></a>'
        output += '<a href="/">Cancel</a>'
        output += '</form></div></div></div>'  
        output += htmlClose 
        return output


@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete_chapter(id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM chapter WHERE id = ?", str(id))
    deletedChapter = cur.fetchone()
    if request.method == 'POST':
        cur.execute("DELETE FROM chapter WHERE id = ?", str(id))
        conn.commit()
        conn.close()
        return redirect(url_for('chapters_list'))
    else:
        output = ''
        output += htmlOpen 
        output += '<div class="container-fluid">'
        output += '<div class="row"><div class="col-6">'
        output += '<h3>Delete a Chapter</h3></div></div><hr>'
        output += '<div class="container-fluid">'
        output += '<div class="row">'
        output += '<form action="/delete/'
        output += str(deletedChapter['id'])
        output += '" method="post">'
        output += '<p>Are you sure you want to delete chapter #'
        output += str(deletedChapter['chapterNum'])
        output += ' - '
        output += deletedChapter['name']
        output += '?</p>'
        output += '<button type="submit">Yes</button>'
        output += '<a href="/">Cancel</a>'
        output += '</form></div></div></div>'
        output += htmlClose 
        return output

if __name__ == '__main__':
    app.debug = True
    app.run()