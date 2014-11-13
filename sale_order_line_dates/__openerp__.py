# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Dates on Sales Order",
    "version": "1.0",
    "depends": [
        "sale_order_dates",
    ],
    "author": "OdooMRP team",
    "contributors": [
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
    ],
    "category": "Sales Management",
    "website": "http://www.odoomrp.com",
    "summary": "",
    "description": """
Add additional date information to the sales order.
===================================================
You can add the following additional dates to a sales order lines:
------------------------------------------------------------------
    * Requested Date
    """,
    "data": [
        "views/sale_order_view.xml",
    ],
    "installable": True,
}
