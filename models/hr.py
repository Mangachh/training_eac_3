from odoo import models, fields


class Employee(models.Model):
    _inherit = "hr.employee"

    formative_actions = fields.Many2many('training.formative_action', string="Employee Formative Actions")
