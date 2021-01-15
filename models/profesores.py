from odoo import models, fields, api
from random import choice
from datetime import datetime
from odoo.exceptions import ValidationError

class profesores(models.Model):
    _name = 'convalidaciones.profesores'
    _description = 'convalidaciones.profesores'

    name = fields.Char(string="Nombre", required=True, index=True,help="nombre del profespr")  
    apellidos = fields.Char(string="Apellidos", required=True, index=True,help="apellidos del pro")  
    edad = fields.Integer(string="Edad", required=True, index=True, help="edad del ")
    fotografia = fields.Binary()
    dni = fields.Char(string="DNI", required=True, index=True,help="nombre del profespr") 
    alumnos = fields.Many2many("convalidaciones.alumnos", string="Alumnos")
    numalumnos = fields.Integer( string="Numero de alumnos",compute="_calcAlumnos",store=True)

    @api.depends("alumnos")
    def _calcAlumnos(self):
        self.numalumnos = datetime.now()
    @api.constrains("dni")
    def validoDNI(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        letra.upper()
        num = int(self.dni[-1])
        if letras[num%23]!=letra:
            raise ValidationError("Dni es invalido")
