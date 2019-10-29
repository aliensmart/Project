import sqlite3


class ORM:
    dbpath = ""
    tablename = ""
    fields = []

    def __init__(self, **kwargs):
        raise NotImplementedError

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            fieldlist = ", ".join(self.fields)
            qmarks = ", ".join(['?' for _ in self.fields])
            SQL = """ INSERT INTO {} ({})
            VALUES ({}) """.format(self.tablename, fieldlist, qmarks)
            # equivalent to: self.field for each field
            values = [getattr(self, field) for field in self.fields]
            curs.execute(SQL, values)
            pk = curs.lastrowid
            self.pk = pk
        
    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            set_equals = ", ".join(
                ["{}=?".format(field) for field in self.fields])
            SQL = """ UPDATE {} SET {} WHERE pk=? """.format(
                self.tablename, set_equals)
            values = [getattr(self, field) 
                    for field in self.fields] + [self.pk]
            curs.execute(SQL, values)

    def delete(self):
        if not self.pk:
            raise KeyError(self.__repr__() + " is not a row in " + 
                            self.tablename)
        
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            SQL = """ DELETE FROM {} WHERE pk = ?;""".format(self.tablename)
            curs.execute(SQL, (self.pk,))

    

    @classmethod
    def one_from_where_clause(cls, where_clause="", values=tuple()):
        """ where_clause is something like 'WHERE pk=?' and vlaues is a tuple 
        corresponding to the ?'s in the clause. Returns None or one instance 
        of this class. """
        SQL = "SELECT * FROM {} {}".format(cls.tablename, where_clause)
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            curs.execute(SQL, values)

            row = curs.fetchone()
            if not row:
                return None
            return cls(**row)
    
    @classmethod
    def all_from_where_clause(cls, where_clause="", values=tuple()):
        SQL = "SELECT * FROM {} {}".format(cls.tablename, where_clause)
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            curs.execute(SQL, values)

            rows = curs.fetchall()
            return [cls(**row) for row in rows]

    @classmethod
    def one_from_pk(cls, pk):
        return cls.one_from_where_clause("WHERE pk=?", (pk,))

    @classmethod
    def one_col_from_where_clause(cls, col="", where_clause="", values=tuple()):
        SQL = "SELECT {} FROM {} {}".format(col ,cls.tablename, where_clause)
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            curs.execute(SQL, values)
            column = curs.fetchone()
            if not column:
                return None
            return column["salt"]


    


    def __repr__(self):
        pattern = "<{} ORM: pk={}>"
        return pattern.format(self.tablename, self.pk)
