import re
from odoo import models, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat', 'l10n_latam_identification_type_id')
    def _check_l10n_ni_vat_format(self):
        for partner in self:
            natural_person_pattern = r"^\d{13}[A-Za-z]$"
            juridic_persona_pattern = r"^[Jj]\d{13}$"

            if partner.vat and partner.l10n_latam_identification_type_id.id == self.env.ref('l10n_ni_community.lit_ruc').id:
                if re.fullmatch(natural_person_pattern, partner.vat) or re.fullmatch(juridic_persona_pattern, partner.vat):
                    continue
                else:
                    raise ValidationError(f"Formato de campo no permitido: {partner.name} - {partner.vat}")
            elif partner.vat and partner.l10n_latam_identification_type_id.id == self.env.ref('l10n_ni_community.lit_dni').id:
                if re.fullmatch(natural_person_pattern, partner.vat):
                    continue
                else:
                    raise ValidationError(f"Formato de campo no permitido: {partner.name} - {partner.vat}")
            else:
                continue
