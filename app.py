from flask import Flask,render_template,request,redirect,url_for,session,flash
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key="secret123"

# ---------------- DATABASE CONFIG ----------------

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Pearlin@01102006'
app.config['MYSQL_DB']='college_portal'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)
bcrypt=Bcrypt(app)

# ---------------- LOGIN ----------------

@app.route('/',methods=['GET','POST'])
def login():

    if request.method=='POST':

        email=request.form.get('email')
        password=request.form.get('password')
        role=request.form.get('role')

        if not role:
            flash("Please select role","danger")
            return redirect(url_for('login'))

        cur=mysql.connection.cursor()

        cur.execute("SELECT * FROM users WHERE email=%s AND role=%s",(email,role))
        user=cur.fetchone()

        if user and bcrypt.check_password_hash(user['password'],password):

            session['logged_in']=True
            session['id']=user['id']
            session['name']=user['name']
            session['role']=user['role']

            if role=="Student":
                return redirect(url_for('student_dashboard'))

            elif role=="Mentor":
                return redirect(url_for('mentor_dashboard'))

            elif role=="Coordinator":
                return redirect(url_for('coordinator_dashboard'))

            elif role=="HOD":
                return redirect(url_for('hod_dashboard'))

        else:
            flash("Invalid Login","danger")

    return render_template("login.html")

# ---------------- STUDENT ----------------

@app.route("/student")
def student_dashboard():

    if 'logged_in' not in session:
        return redirect(url_for('login'))

    cur=mysql.connection.cursor()

    cur.execute("SELECT * FROM problem_statements")
    problems=cur.fetchall()

    return render_template(
        "dashboard_student.html",
        name=session['name'],
        problems=problems
    )

# ---------------- MENTOR ----------------

@app.route("/mentor")
def mentor_dashboard():

    if 'logged_in' not in session:
        return redirect(url_for('login'))

    cur=mysql.connection.cursor()

    cur.execute("""
    SELECT teams.id,problem_statements.title
    FROM teams
    JOIN problem_statements
    ON teams.problem_id=problem_statements.id
    WHERE mentor_id=%s
    """,(session['id'],))

    teams=cur.fetchall()

    return render_template(
        "dashboard_mentor.html",
        name=session['name'],
        teams=teams
    )

# ---------------- COORDINATOR ----------------

@app.route("/coordinator")
def coordinator_dashboard():

    if 'logged_in' not in session:
        return redirect(url_for('login'))

    cur=mysql.connection.cursor()

    cur.execute("SELECT * FROM problem_statements")
    problems=cur.fetchall()

    cur.execute("SELECT COUNT(*) as total FROM problem_statements")
    total=cur.fetchone()['total']

    cur.execute("SELECT COUNT(*) as available FROM problem_statements WHERE status='available'")
    available=cur.fetchone()['available']

    cur.execute("SELECT COUNT(*) as closed FROM problem_statements WHERE status='closed'")
    closed=cur.fetchone()['closed']

    return render_template(
        "dashboard_coordinator.html",
        name=session['name'],
        problems=problems,
        total=total,
        available=available,
        closed=closed
    )

# ---------------- HOD ----------------

@app.route("/hod")
def hod_dashboard():

    if 'logged_in' not in session:
        return redirect(url_for('login'))

    cur=mysql.connection.cursor()

    cur.execute("""
    SELECT teams.id,
    problem_statements.title,
    users.name as mentor
    FROM teams
    JOIN problem_statements
    ON teams.problem_id=problem_statements.id
    JOIN users
    ON teams.mentor_id=users.id
    """)

    teams=cur.fetchall()

    return render_template(
        "dashboard_hod.html",
        name=session['name'],
        teams=teams
    )

# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()
    flash("Logged out successfully","success")
    return redirect(url_for('login'))

# ---------------- RUN APP ----------------

if __name__=="__main__":
    app.run(debug=True)