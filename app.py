from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM preguntas ORDER BY RAND() LIMIT 1")
    data = cur.fetchall()
    cur.close()

    return render_template('preguntas.html', preguntas=data )


@app.route('/admin/preguntas')
def preguntas():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM preguntas")
    data = cur.fetchall()
    cur.close()

    return render_template('preguntas_admin.html', preguntas=data )

@app.route('/admin/preguntas/insert', methods = ['POST'])
def insertpregunta():

    if request.method == "POST":
        flash("Pregunta insertada")
        pregunta = request.form['pregunta']
        respuesta_true_a = request.form['respuesta_true_a']
        respuesta_false_b = request.form['respuesta_false_b']
        respuesta_false_c = request.form['respuesta_false_c']
        respuesta_false_d = request.form['respuesta_false_d']
        respuesta_false_e = request.form['respuesta_false_e']
        respuesta_false_f = request.form['respuesta_false_f']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO preguntas (pregunta, respuesta_true_a, respuesta_false_b, respuesta_false_c, respuesta_false_d, respuesta_false_e, respuesta_false_f) VALUES (%s, %s, %s, %s, %s, %s, %s)", (pregunta, respuesta_true_a, respuesta_false_b, respuesta_false_c, respuesta_false_d, respuesta_false_e, respuesta_false_f))
        mysql.connection.commit()

        return redirect(url_for('preguntas'))

@app.route('/admin/preguntas/delete/<string:id_data>', methods = ['GET'])
def deletepregunta(id_data):
    flash("Pregunta eliminada")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM preguntas WHERE id=%s", (id_data,))
    mysql.connection.commit()

    return redirect(url_for('preguntas'))

@app.route('/admin/preguntas/update',methods=['POST','GET'])
def updatepregunta():

    if request.method == 'POST':
        id_data = request.form['id']
        pregunta = request.form['pregunta']
        respuesta_true_a = request.form['respuesta_true_a']
        respuesta_false_b = request.form['respuesta_false_b']
        respuesta_false_c = request.form['respuesta_false_c']
        respuesta_false_d = request.form['respuesta_false_d']
        respuesta_false_e = request.form['respuesta_false_e']
        respuesta_false_f = request.form['respuesta_false_f']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE preguntas
               SET pregunta=%s, respuesta_true_a=%s, respuesta_false_b=%s, respuesta_false_c=%s, respuesta_false_d=%s, respuesta_false_e=%s, respuesta_false_f=%s
               WHERE id=%s
            """, (pregunta, respuesta_true_a, respuesta_false_b, respuesta_false_c, respuesta_false_d, respuesta_false_e, respuesta_false_f, id_data))
        flash("Pregunta actualizada")
        mysql.connection.commit()

        return redirect(url_for('preguntas'))


@app.route('/hilo')
def hilo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM mensajes")
    data = cur.fetchall()
    cur.close()

    return render_template('hilo.html', mensajes=data )

@app.route('/hilo/insert', methods = ['POST'])
def insertmensajehilo():

    if request.method == "POST":
        flash("Mensaje enviado")
        titulo = request.form['titulo']
        mensaje = request.form['mensaje']
        user_id = request.form['user_id']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mensajes (titulo, mensaje, user_id) VALUES (%s, %s, %s)", (titulo, mensaje, user_id))
        mysql.connection.commit()

        return redirect(url_for('hilo'))


@app.route('/admin/mensajes')
def mensajes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM mensajes")
    data = cur.fetchall()
    cur.close()

    return render_template('mensajes_admin.html', mensajes=data )

@app.route('/admin/mensajes/insert', methods = ['POST'])
def insertmensaje():

    if request.method == "POST":
        flash("Mensaje enviado")
        titulo = request.form['titulo']
        mensaje = request.form['mensaje']
        user_id = request.form['user_id']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mensajes (titulo, mensaje, user_id) VALUES (%s, %s, %s)", (titulo, mensaje, user_id))
        mysql.connection.commit()

        return redirect(url_for('mensajes'))


@app.route('/admin/mensajes/delete/<string:id_data>', methods = ['GET'])
def deletemensaje(id_data):
    flash("Mensaje eliminado")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM mensajes WHERE id=%s", (id_data,))
    mysql.connection.commit()

    return redirect(url_for('mensajes'))

@app.route('/admin/mensajes/update',methods=['POST','GET'])
def updatemensaje():

    if request.method == 'POST':
        id_data = request.form['id']
        titulo = request.form['titulo']
        mensaje = request.form['mensaje']
        user_id = request.form['user_id']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE mensajes
               SET titulo=%s, mensaje=%s, user_id=%s
               WHERE id=%s
            """, (titulo, mensaje, user_id, id_data))
        flash("Mensaje editado")
        mysql.connection.commit()

        return redirect(url_for('mensajes'))

if __name__ == "__main__":
    app.run(debug=True)