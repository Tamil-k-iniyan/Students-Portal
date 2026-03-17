

# from flask import Flask, request, redirect
# import psycopg2

# app = Flask(__name__)

# # ---------- DATABASE CONNECTION ----------
# conn = psycopg2.connect(
#     host="localhost",
#     database="project_portal",
#     user="postgres",
#     password="tamil@2006"
# )

# cursor = conn.cursor()


# # ---------- LOGIN PAGE ----------
# @app.route('/')
# def login_page():
#     return """
#     <html>
#     <head>
#     <title>Student Project Portal</title>
#     <style>
#     body{
#         font-family:Arial;
#         background:linear-gradient(135deg,#6a11cb,#2575fc);
#         display:flex;
#         justify-content:center;
#         align-items:center;
#         height:100vh;
#     }
#     .box{
#         background:white;
#         padding:40px;
#         border-radius:10px;
#         text-align:center;
#         width:300px;
#     }
#     input{
#         width:90%;
#         padding:10px;
#         margin:10px;
#     }
#     button{
#         background:#2575fc;
#         color:white;
#         border:none;
#         padding:10px;
#         width:100%;
#     }
#     </style>
#     </head>
#     <body>

#     <div class="box">
#     <h2>Project Portal Login</h2>

#     <form action="/login" method="post">
#     <input name="username" placeholder="Username"><br>
#     <input type="password" name="password" placeholder="Password"><br>
#     <button>Login</button>
#     </form>

#     </div>
#     </body>
#     </html>
#     """


# # ---------- LOGIN CHECK ----------
# @app.route('/login', methods=['POST'])
# def login():

#     username = request.form['username']
#     password = request.form['password']

#     cursor.execute(
#         "SELECT role FROM users WHERE username=%s AND password=%s",
#         (username, password)
#     )

#     result = cursor.fetchone()

#     if result:
#         role = result[0]
#         return redirect("/dashboard/" + role)

#     return "<h3>Invalid Login</h3><a href='/'>Back</a>"


# # ---------- DASHBOARD ----------
# @app.route('/dashboard/<role>')
# def dashboard(role):

#     if role == "student":

#         links = """
#         <a class='card' href='/create_team'>Create Team</a>
#         <a class='card' href='/view_problems'>View Problem Statements</a>
#         """

#         title = "Student Dashboard"

#     elif role == "mentor":

#         links = "<a class='card' href='/view_teams'>View Teams</a>"
#         title = "Mentor Dashboard"

#     elif role == "coordinator":

#         links = "<a class='card' href='/view_problems'>View Problems</a>"
#         title = "Coordinator Dashboard"

#     elif role == "hod":

#         links = "<a class='card' href='/view_teams'>View All Teams</a>"
#         title = "HOD Dashboard"

#     else:
#         return "Invalid Role"

#     return f"""
#     <html>
#     <style>

#     body{{font-family:Arial;background:#f4f6f9;margin:0}}

#     header{{
#         background:#2575fc;
#         color:white;
#         text-align:center;
#         padding:20px;
#     }}

#     .container{{
#         display:flex;
#         justify-content:center;
#         margin-top:50px;
#     }}

#     .card{{
#         background:white;
#         padding:40px;
#         margin:20px;
#         text-decoration:none;
#         color:black;
#         border-radius:10px;
#         box-shadow:0 5px 15px gray;
#         font-size:18px;
#     }}

#     .card:hover{{
#         background:#2575fc;
#         color:white;
#     }}

#     </style>

#     <body>

#     <header>
#     <h1>{title}</h1>
#     </header>

#     <div class="container">
#     {links}
#     </div>

#     <center><a href="/">Logout</a></center>

#     </body>
#     </html>
#     """


# # ---------- CREATE TEAM ----------
# @app.route('/create_team')
# def create_team():

#     return """
#     <h2 style='text-align:center'>Create Team</h2>

#     <form action="/save_team" method="post" style="width:300px;margin:auto">

#     Team Name:<br>
#     <input name="team_name"><br><br>

#     Member 1:<br>
#     <input name="member1"><br><br>

#     Member 2:<br>
#     <input name="member2"><br><br>

#     Member 3:<br>
#     <input name="member3"><br><br>

#     <button>Create Team</button>

#     </form>
#     """


# # ---------- SAVE TEAM ----------
# @app.route('/save_team', methods=['POST'])
# def save_team():

#     team = request.form['team_name']
#     m1 = request.form['member1']
#     m2 = request.form['member2']
#     m3 = request.form['member3']

#     cursor.execute(
#         "INSERT INTO teams (team_name,member1,member2,member3) VALUES (%s,%s,%s,%s)",
#         (team, m1, m2, m3)
#     )

#     conn.commit()

#     return "<h3>Team Created</h3><a href='/dashboard/student'>Back</a>"


# # ---------- VIEW TEAMS ----------
# @app.route('/view_teams')
# def view_teams():

#     cursor.execute("SELECT * FROM teams")

#     rows = cursor.fetchall()

#     html = "<h2 style='text-align:center'>Teams</h2>"

#     for r in rows:

#         html += f"""
#         <div style="width:50%;margin:auto;background:white;
#         padding:20px;margin-top:20px;box-shadow:0 0 10px gray">

#         <h3>{r[1]}</h3>

#         <ul>
#         <li>{r[2]}</li>
#         <li>{r[3]}</li>
#         <li>{r[4]}</li>
#         </ul>

#         </div>
#         """

#     html += "<br><center><a href='/'>Back</a></center>"

#     return html


# # ---------- VIEW PROBLEMS ----------
# @app.route('/view_problems')
# def view_problems():

#     cursor.execute(
#         "SELECT problem_id,title,description FROM problems WHERE status='available'"
#     )

#     rows = cursor.fetchall()

#     html = "<h2 style='text-align:center'>Available Problems</h2>"

#     for r in rows:

#         html += f"""
#         <div style="width:60%;margin:auto;background:white;
#         padding:20px;margin-top:20px;border-radius:10px;
#         box-shadow:0 0 10px gray">

#         <h3>{r[1]}</h3>
#         <p>{r[2]}</p>

#         <a href="/select_problem/{r[0]}">Select This Problem</a>

#         </div>
#         """

#     html += "<br><center><a href='/dashboard/student'>Back</a></center>"

#     return html


# # ---------- SELECT PROBLEM ----------
# @app.route('/select_problem/<int:pid>')
# def select_problem(pid):

#     cursor.execute(
#         "UPDATE problems SET status='selected' WHERE problem_id=%s",
#         (pid,)
#     )

#     conn.commit()

#     return "<h2>Problem Selected</h2><a href='/dashboard/student'>Back</a>"


# # ---------- RUN APP ----------
# if __name__ == "__main__":
#     app.run(debug=True)


#  new features

from flask import Flask, request, redirect
import psycopg2

app = Flask(__name__)

# ---------- DATABASE CONNECTION ----------
conn = psycopg2.connect(
    host="localhost",
    database="project_portal",
    user="postgres",
    password="tamil@2006"
)

cursor = conn.cursor()


# ---------- LOGIN PAGE ----------
@app.route('/')
def login_page():
    return """
    <html>
    <head>
    <title>Student Project Portal</title>
    <style>
    body{
        font-family:Arial;
        background:linear-gradient(135deg,#6a11cb,#2575fc);
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    }
    .box{
        background:white;
        padding:40px;
        border-radius:10px;
        text-align:center;
        width:300px;
    }
    input{
        width:90%;
        padding:10px;
        margin:10px;
    }
    button{
        background:#2575fc;
        color:white;
        border:none;
        padding:10px;
        width:100%;
    }
    </style>
    </head>

    <body>

    <div class="box">
    <h2>Project Portal Login</h2>

    <form action="/login" method="post">
    <input name="username" placeholder="Username"><br>
    <input type="password" name="password" placeholder="Password"><br>
    <button>Login</button>
    </form>

    </div>
    </body>
    </html>
    """


# ---------- LOGIN CHECK ----------
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    cursor.execute(
        "SELECT role FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    result = cursor.fetchone()

    if result:
        role = result[0]
        return redirect("/dashboard/" + role)

    return "<h3>Invalid Login</h3><a href='/'>Back</a>"


# ---------- DASHBOARD ----------
@app.route('/dashboard/<role>')
def dashboard(role):

    if role == "student":

        links = """
        <a class='card' href='/create_team'>Create Team</a>
        <a class='card' href='/view_problems'>View Problem Statements</a>
        <a class='card' href='/project_request'>Submit Project Request</a>
        """

        title = "Student Dashboard"

    elif role == "mentor":

        links = "<a class='card' href='/view_teams'>View Teams</a>"
        title = "Mentor Dashboard"

    elif role == "coordinator":

        links = """
        <a class='card' href='/view_problems'>View Problems</a>
        <a class='card' href='/project_requests'>Project Requests</a>
        """
        title = "Coordinator Dashboard"

    elif role == "hod":

        links = "<a class='card' href='/view_teams'>View All Teams</a>"
        title = "HOD Dashboard"

    else:
        return "Invalid Role"

    return f"""
    <html>
    <style>

    body{{font-family:Arial;background:#f4f6f9;margin:0}}

    header{{
        background:#2575fc;
        color:white;
        text-align:center;
        padding:20px;
    }}

    .container{{
        display:flex;
        justify-content:center;
        margin-top:50px;
    }}

    .card{{
        background:white;
        padding:40px;
        margin:20px;
        text-decoration:none;
        color:black;
        border-radius:10px;
        box-shadow:0 5px 15px gray;
        font-size:18px;
    }}

    .card:hover{{
        background:#2575fc;
        color:white;
    }}

    </style>

    <body>

    <header>
    <h1>{title}</h1>
    </header>

    <div class="container">
    {links}
    </div>

    <center><a href="/">Logout</a></center>

    </body>
    </html>
    """


# ---------- CREATE TEAM ----------
@app.route('/create_team')
def create_team():

    return """
    <h2 style='text-align:center'>Create Team</h2>

    <form action="/save_team" method="post" style="width:300px;margin:auto">

    Team Name:<br>
    <input name="team_name"><br><br>

    Member 1:<br>
    <input name="member1"><br><br>

    Member 2:<br>
    <input name="member2"><br><br>

    Member 3:<br>
    <input name="member3"><br><br>

    <button>Create Team</button>

    </form>
    """


# ---------- SAVE TEAM ----------
@app.route('/save_team', methods=['POST'])
def save_team():

    team = request.form['team_name']
    m1 = request.form['member1']
    m2 = request.form['member2']
    m3 = request.form['member3']

    cursor.execute(
        "INSERT INTO teams (team_name,member1,member2,member3) VALUES (%s,%s,%s,%s)",
        (team, m1, m2, m3)
    )

    conn.commit()

    return "<h3>Team Created</h3><a href='/dashboard/student'>Back</a>"


# ---------- VIEW TEAMS ----------
@app.route('/view_teams')
def view_teams():

    cursor.execute("SELECT * FROM teams")

    rows = cursor.fetchall()

    html = "<h2 style='text-align:center'>Teams</h2>"

    for r in rows:

        html += f"""
        <div style="width:50%;margin:auto;background:white;
        padding:20px;margin-top:20px;box-shadow:0 0 10px gray">

        <h3>{r[1]}</h3>

        <ul>
        <li>{r[2]}</li>
        <li>{r[3]}</li>
        <li>{r[4]}</li>
        </ul>

        </div>
        """

    html += "<br><center><a href='/'>Back</a></center>"

    return html


# ---------- VIEW PROBLEMS ----------
@app.route('/view_problems')
def view_problems():

    cursor.execute(
        "SELECT problem_id,title,description FROM problems WHERE status='available'"
    )

    rows = cursor.fetchall()

    html = "<h2 style='text-align:center'>Available Problems</h2>"

    for r in rows:

        html += f"""
        <div style="width:60%;margin:auto;background:white;
        padding:20px;margin-top:20px;border-radius:10px;
        box-shadow:0 0 10px gray">

        <h3>{r[1]}</h3>
        <p>{r[2]}</p>

        <a href="/select_problem/{r[0]}">Select This Problem</a>

        </div>
        """

    html += "<br><center><a href='/dashboard/student'>Back</a></center>"

    return html


# ---------- SELECT PROBLEM ----------
@app.route('/select_problem/<int:pid>')
def select_problem(pid):

    cursor.execute(
        "UPDATE problems SET status='selected' WHERE problem_id=%s",
        (pid,)
    )

    conn.commit()

    return "<h2>Problem Selected</h2><a href='/dashboard/student'>Back</a>"


# ---------- PROJECT REQUEST PAGE ----------
@app.route('/project_request')
def project_request():

    return """
    <h2 style='text-align:center'>Submit Project Request</h2>

    <form action="/submit_project" method="post"
    style="width:400px;margin:auto">

    Team Name:<br>
    <input name="team_name"><br><br>

    Project Title:<br>
    <input name="title"><br><br>

    Description:<br>
    <textarea name="description"></textarea><br><br>

    <button>Submit Request</button>

    </form>
    """


# ---------- SAVE PROJECT REQUEST ----------
@app.route('/submit_project', methods=['POST'])
def submit_project():

    team = request.form['team_name']
    title = request.form['title']
    desc = request.form['description']

    cursor.execute(
        "INSERT INTO project_requests(team_name,project_title,description) VALUES (%s,%s,%s)",
        (team,title,desc)
    )

    conn.commit()

    return "<h3>Project Request Submitted</h3><a href='/dashboard/student'>Back</a>"


# ---------- VIEW PROJECT REQUESTS ----------
@app.route('/project_requests')
def project_requests():

    cursor.execute("SELECT * FROM project_requests")

    rows = cursor.fetchall()

    html = "<h2 style='text-align:center'>Project Requests</h2>"

    for r in rows:

        html += f"""
        <div style="width:60%;margin:auto;background:white;
        padding:20px;margin-top:20px;border-radius:10px;
        box-shadow:0 0 10px gray">

        <h3>{r[2]}</h3>
        <p>{r[3]}</p>

        Status: {r[4]} <br><br>

        <a href="/approve_project/{r[0]}">Approve</a> |
        <a href="/reject_project/{r[0]}">Reject</a>

        </div>
        """

    html += "<br><center><a href='/dashboard/coordinator'>Back</a></center>"

    return html


# ---------- APPROVE PROJECT ----------
@app.route('/approve_project/<int:id>')
def approve_project(id):

    cursor.execute(
        "UPDATE project_requests SET status='Approved', locked=TRUE WHERE id=%s",
        (id,)
    )

    conn.commit()

    return redirect('/project_requests')


# ---------- REJECT PROJECT ----------
@app.route('/reject_project/<int:id>')
def reject_project(id):

    cursor.execute(
        "UPDATE project_requests SET status='Rejected' WHERE id=%s",
        (id,)
    )

    conn.commit()

    return redirect('/project_requests')


# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)