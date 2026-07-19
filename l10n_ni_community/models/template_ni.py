from odoo import models
from odoo.addons.account.models.chart_template import template

class TemplateNi(models.AbstractModel):
    _inherit = 'account.chart.template'


    @template('ni', 'res.company')
    def _get_ni_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.ni',
                'bank_account_code_prefix': '11',
                'cash_account_code_prefix': '11',
                'transfer_account_code_prefix': '11',
            }
        }

    @template('ni')
    def _get_ni_template_data(self):
        return {
            'code_digits': '4',
            'property_account_receivable_id': 'ni_1102',
            'property_account_payable_id': 'ni_2101',
            'property_account_income_categ_id': 'ni_4101',
            'property_account_expense_categ_id': 'ni_5101',
        }

