from odoo import models, fields, api

class ParcAutomobileIntervention(models.Model):
     _name = 'parc_automobile.intervention'

     date = fields.Date('Date d\'acquisition')
     montant_frais = fields.Float()
     prestataire = fields.Char()
     duree = fields.Integer()

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)