# -*- coding: utf-8 -*-
from email.errors import UndecodableBytesDefect
from logging import exception
from odoo import models, fields, api, exceptions


class Car(models.Model):
    _name = 'odoo_model_advanced.car'
    _description = 'Coche'

    name = fields.Char(string='Modelo')
    number_plate = fields.Char(string='Matrícula')
    cv = fields.Float(string='CV')
    colour = fields.Char(string='Color')
    fuel_litres = fields.Float(string='Litros')
    under_fuel = fields.Boolean(string='Necesita repostar')

    #Definicio de Constraints
    _sql_constraints = [
       # Parametros nombre-restriccion a nivel de sql-mensaje
       ('number_plate_unique','UNIQUE(number_plate)','El número de matricula debe ser único.'),
    ]
    
    #Validacion
    @api.constrains('cv','colour','number_plate')
    def _validate(self):
        if self.colour == "":
            raise exceptions.ValidationError('El nombre del modelo no puede estar en blanco.')
        elif self.cv <= 0:
            raise exceptions.ValidationError('Los Caballos de fuerza, no pueden estar en 0.')
        elif self.number_plate == "":
            raise exceptions.ValidationError('La placa no puede estar vacia.')
    
    # #Validacion de campo
    # @api.constrains('cv')
    # def _validate_cv(self):
    #     if self.cv <= 0:
    #         raise exceptions.ValidationError('Los Caballos de fuerza, no pueden estar en 0.')

    # @api.constrains('name')
    # def _validate_name(self):
    #     if self.name == "":
    #         raise exceptions.ValidationError('El nombre del modelo no puede estar en blanco.')

    @api.onchange('fuel_litres')
    def _check_under_fuel(self):
        if self.fuel_litres < 50:
            self.under_fuel = True
        else:
            self.under_fuel = False
