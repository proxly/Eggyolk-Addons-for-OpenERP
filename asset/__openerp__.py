{
    "name" : "Asset Management System",
    "version" : "0.1",
    "author" : "Roxly Rivero",
    "website" : "http://www.gqwest.com",
    "license" : "GPL-3",
    "category" : "Asset Management",
    "description": """
	This module is for monitoring assets such as:
         * Office Fixtures,
         * Mobile Phones
         * Company Vehicles
         * IT Machines
    """,
    "depends" : [],
    "init_xml" : [],
    "update_xml" : [
        'security/asset_security.xml',
#        'security/ir.model.access.csv',
        'asset.xml',
        'board_asset_view.xml',
    ],
    "demo_xml" : [],
    "installable" : True,
    "certificate" : ''
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

