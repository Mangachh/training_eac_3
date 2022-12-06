# -*- coding: utf-8 -*-

from odoo import models, fields, api

class catalogue(models.Model):
     _name = 'training.catalogue'

     name = fields.Char(size=32, string='Name', index=True, required=True)
     description = fields.Text(string="Description")
     no_hours = fields.Integer(string="no hours")
     active = fields.Boolean('Active', default=True)

class formative_action(models.Model):
    _name = 'training.formative_action'

    date = fields.Date(required=True, string="Date begin")
    hours_per_session = fields.Integer(string="Hours per session")
    no_sessions = fields.Integer(compute='_no_sessions', string="no sessions")
    id_course = fields.Many2one('training.catalogue', required=True, string="Course")
    no_hours = fields.Integer(related='id_course.no_hours', store=False, string="no hours")
    id_trainer = fields.Many2one('res.partner', string="Trainer")
    participants = fields.Many2many('hr.employee', string="Participants")

    @api.depends('hours_per_session', 'no_hours')
    def _no_sessions(self):
        if self.hours_per_session == 0:
            self.no_sessions = 0
        else:
            if self.no_hours%self.hours_per_session == 0:
                self.no_sessions = self.no_hours/self.hours_per_session
            else:
                self.no_sessions = (self.no_hours/self.hours_per_session)+1