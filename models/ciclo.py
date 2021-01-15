 #-*- coding: utf-8 -*-
from odoo import models, fields, api


class ciclo_model(models.Model):
    _name = 'convalidaciones.ciclo'
    _description = 'convalidaciones.ciclo'

    name = fields.Char(string="Ciclo", required="True", index="True",help="nombre de los ciclos", size=10)
    descripcion = fields.Html(string="Descrpición",required="True",help="descipcion de los ciclos")
    modulos = fields.Many2many("convalidaciones.modulo","ciclo",string="Módulos")
  
   
