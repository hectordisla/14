# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Car(models.Model):
    _name = 'odoo_model_advanced.car'
    _description = 'Coche'

    name = fields.Char(string='Modelo')
    number_plate = fields.Char(string='Matrícula')
    cv = fields.Float(string='CV')
    colour = fields.Char(string='Color')
    fuel_litres = fields.Float(string='Litros')

    #Definicio de Constraints
    #_sql_constraints = [
    #    # Parametros nombre-restriccion a nivel de sql-mensaje
    #    ('number_plate_unique','UNIQUE(number_plate)','El número de matricula debe ser único.'),
    #]

    @api.constrains('cv')
    def _validate_cv(self):
        if self.cv <= 0:
            raise exceptions.ValidationError('Los Caballos de fuerza, no pueden estar en 0.')


