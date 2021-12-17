from odoo import models, fields, api

class ParcAutomobileAssurance(models.Model):
     _name = 'parc_automobile.assurance'
     _rec_name = 'nom_assurance'

     nom_assurance = fields.Char('Nom de l\'assurance')
     num_agence = fields.Integer()
     date_debut = fields.Date('Date de début')
     date_fin = fields.Date('Date de fin')
     prime_totale = fields.Float()

     vehicule_ids = fields.One2many(comodel_name='parc_automobile.vehicule', inverse_name='assurance_id')