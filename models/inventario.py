from utils.db import db
from dataclasses import dataclass
from models.producto import Producto

@dataclass
class Inventario(db.Model):
    __tablename__ = 'inventarios'
    
    inventario_id = db.Column(db.Integer, primary_key=True)
    fecha_actualizacion = db.Column(db.DateTime)
    motivo = db.Column(db.String(250))
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.producto_id'))
        
    def __init__ (self,fecha_actualizacion,motivo,producto_id):
        self.fecha_actualizacion = fecha_actualizacion
        self.motivo = motivo
        self.producto_id = producto_id