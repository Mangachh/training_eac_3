# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class catalogue(models.Model):
     _name = 'training.catalogue'

     name = fields.Char(size=32, string='Name', index=True, required=True)
     description = fields.Text(string="Description")
     no_hours = fields.Integer(string="no hours")
     active = fields.Boolean('Active', default=True)

"""class trainer(models.Model):
    _name = 'training.trainer'

    name = fields.Char(compute='_trainer_name', size=32, string='Trainer\'s name')
    firstname = fields.Char(size=32, string='Name', index=True, required=True)
    surname1 = fields.Char(size=32, string='Middle name', index=True, required=True)
    surname2 = fields.Char(size=32, string='Last name')
    id_especialty = fields.Many2one('training.especialty', string="Especialty", required=True)

    @api.multi
    def _trainer_name(self):
        for record in self:
            if record.firstname and record.surname1:
                record.name = record.firstname + " " + record.surname1 + " " + record.surname2
            else: record.name = ''          
"""

class especialty(models.Model):
    _name = 'training.especialty'

    name = fields.Char(size=32, string='Name', required=True)

class formative_action(models.Model):
    _name = 'training.formative_action'

    date = fields.Date(required=True, string="Date begin")
    hours_per_session = fields.Integer(string="Hours per session")
    no_sessions = fields.Integer(compute='_no_sessions', string="no sessions")
    id_course = fields.Many2one('training.catalogue', required=True, string="Course")
    no_hours = fields.Integer(related='id_course.no_hours', store=False, string="no hours")
    id_trainer = fields.Many2one('res.partner', string="Trainer", domain=[('trainer', '=', True)])
    participants = fields.Many2many('hr.employee', string="Participants")

    @api.multi
    def _no_sessions(self):
        for record in self:
            if record.no_hours%record.hours_per_session == 0:
                record.no_sessions = record.no_hours/record.hours_per_session
            else: record.no_sessions = record.no_hours/record.hours_per_session+1