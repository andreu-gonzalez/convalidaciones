 #-*- coding: utf-8 -*-
from odoo import models, fields, api


class modulo_model(models.Model):
    _name = 'convalidaciones.modulo'
    _description = 'convalidaciones.modulo'

    name = fields.Char(string="Nombre", required=True,help="nombre de los modeulos",size=10)
    descripcion = fields.Html(string="Descripción",required=False,help="descipcion de los modulos")
    horas = fields.Integer(string="Horas del módulo",required=False,default=8,help="horas del modulo")
    ciclo = fields.Many2many("convalidaciones.ciclo",string="Ciclo")
