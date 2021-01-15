# -*- coding: utf-8 -*-
from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError

class alumno(models.Model):
    _name = 'convalidaciones.alumno'
    _description = 'convalidaciones.alumno'
    name = fields.Char(string="Nombre", required=True, index=True,help="nombre del alumno")  
    edad = fields.Integer(string="Edad", required=True, index=True, help="edad del alumno")
    localidad = fields.Char(string="Localidad", required=True, index=True, help="localidad del alumno")
    email = fields.Char(string="Email", required=True, index=True, help="email del alumno")
    provincia = fields.Char(string="Provincia", required=True, index=True,help="provincia del alumno")
    fotografia = fields.Binary()
    contra = fields.Char(string="Contraseña", required=False, index=True,default="0",help="password del alumno",size=10)
    convalidaciones=fields.One2many("convalidaciones.conv","alumno_id",string="convalidaciones")
    profesores = fields.Many2many("convalidaciones.profesores",string="profesores")
    def generarCon(self):
        self.ensure_one()
        longitud = 10
        valores = "abcdefghijklmnopqrstuvwxyz0123456789"
        passw = ""
        passw = passw.join([choice(valores) for i in range(longitud)])
        self.contra = passw
        return True
    @api.constrains("edad")
    def _check_longitud(self):
        if len(self.edad) < 14:
            raise ValidationError("Menos")
        return True