 #-*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class conv_model(models.Model):
    _name = 'convalidaciones.conv'
    _description = 'convalidaciones.conv'

    fecha = fields.Date(string="Fecha",required=True,default=datetime.today(),help="horas del modulo")
    modulo_id = fields.Many2one("convalidaciones.modulo", string="Módulo")
    alumno_id = fields.Many2one("convalidaciones.alumno", string="Alumno")
    