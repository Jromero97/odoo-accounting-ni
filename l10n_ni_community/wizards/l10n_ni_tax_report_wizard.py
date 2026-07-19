from odoo import models, api, fields

class TaxReportWizard(models.TransientModel):
    _name = 'l10n_ni.tax.report.wizard'
    _description = 'Reporte de Impuestos - Formulario 124'
    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)
    company = fields.Many2one('res.company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company.currency_id')
    base_iva_15 = fields.Monetary(readonly=True)
    base_exent = fields.Monetary(readonly=True)
    base_exports = fields.Monetary(readonly=True)
    fiscal_debit_iva = fields.Monetary(readonly=True)
    fiscal_credit_iva = fields.Monetary(readonly=True)

    def _get_tag_balance(self, tag_name):
        tags = self.env['account.account.tag'].search([('name', 'in', [f'+{tag_name}', f'-{tag_name}']), ('applicability', '=', 'taxes'), ('country_id', '=', self.env.ref('base.ni').id)])

        if len(tags) == 0:
            return 0.0
        
        balance_negated = 0.0
        balance_non_negated = 0.0
        
        for tag in tags:
            lines = self.env['account.move.line'].search(
                [
                    ('tax_tag_ids', 'in', tag.id),
                    ('parent_state', '=', 'posted'),
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('company_id', '=', self.company.id)
                ]
            )

            if tag.tax_negate:
                balance_negated += -sum(lines.mapped('balance'))
            else:
                balance_non_negated += sum(lines.mapped('balance'))

        return balance_negated + balance_non_negated

    def action_compute(self):
        self.ensure_one()

        self.base_iva_15 = self._get_tag_balance('Base IVA 15%')
        self.base_exent = self._get_tag_balance('Base Exenta')
        self.base_exports = self._get_tag_balance('Base Exportaciones')
        self.fiscal_debit_iva = self._get_tag_balance('Debito Fiscal IVA')
        self.fiscal_credit_iva = self._get_tag_balance('Credito Fiscal IVA')



