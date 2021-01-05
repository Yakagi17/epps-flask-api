from app import db, app



class Mahasiswa(db.Model):
    __tablename__ = 'Mahasiswa'
    npm = db.Column(db.(10), primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    no_hp = db.Column(db.String(12), index=True, unique=True)


class Staff(db.Model):
    pass

class Psikolog(db.Model):
    pass

class Data_EPPS(db.Model):
    pass

class Tes_EPPS(db.Model):
    pass

class Prodi(db.Model):
    pass

class Kantor(db.Model):
    pass

class Hasil_Tes_EPPS(db.Model):
    pass

class Skor_Tes_EPPS(db.Model):
    pass