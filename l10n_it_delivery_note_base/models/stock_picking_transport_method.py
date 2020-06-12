# Copyright 2014-2019 Dinamiche Aziendali srl (http://www.dinamicheaziendali.it/)
# @author: Marco Calcagni <mcalcagni@dinamicheaziendali.it>
# @author: Gianmarco Conte <gconte@dinamicheaziendali.it>
# @author: Giuseppe Borruso <gborruso@dinamicheaziendali.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, fields, models


class StockPickingTransportMethod(models.Model):
    _name = 'stock.picking.transport.method'
    _description = "Method of transport"
    _order = 'sequence, name, id'

    active = fields.Boolean(string=_("Active"), default=True)
    sequence = fields.Integer(string=_("Sequence"), index=True, default=10)
    name = fields.Char(string=_("Method name"), index=True, required=True, translate=True)
    note = fields.Html(string=_("Internal note"))

    _sql_constraints = [(
        'name_uniq',
        'unique(name)',
        "This method of transport already exists!"
    )]
