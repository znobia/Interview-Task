# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountReportGeneralLedger(models.TransientModel):
    _inherit = "account.report.general.ledger"

    analytic_account_ids = fields.Many2many('account.analytic.account',string='Analytic')


    #add analytic account to used context and used in general report
    def _print_report(self, data):
        data['form'].update(self.read(['analytic_account_ids'])[0])
        analytic = self.env['account.analytic.account'].browse(data['form']['analytic_account_ids'])
        data['form']['used_context'].update({'analytic_account_ids':analytic.ids})
        return super(AccountReportGeneralLedger,self)._print_report(data)