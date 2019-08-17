# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    trainer=fields.Boolean(string="Trainer", default=False)
    id_especialty = fields.Many2one('training.especialty', string="Especialty")