import sqlite3 as sql

class TransactionObject():
    database    = "filiados.db"
    conn        = None
    cur         = None
    connected   = False

    def connect(self):
        TransactionObject.conn      = sql.connect(TransactionObject.database)
        TransactionObject.cur       = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False


def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "CREATE TABLE IF NOT EXISTS filiados (id INTEGER PRIMARY KEY , nome TEXT, contato TEXT, municipio TEXT)")
    trans.persist()
    trans.disconnect()

def insert(nome, contato, municipio):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO filiados VALUES(NULL, ?,?,?)", (nome, contato, municipio))
    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM filiados")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(nome="", contato="", municipio=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM filiados WHERE nome=? or contato=? or municipio=? ", (nome, contato, municipio))
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM filiados WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, nome, contato, municipio):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE filiados SET nome=? or contato=? or municipio=? WHERE id = ?",(nome, contato, municipio, id))
    trans.persist()
    trans.disconnect()

initDB()

