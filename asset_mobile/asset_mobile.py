from osv import fields, osv
import time
from tools.translate import _

class asset_mobile(osv.osv):
        _name = "asset.mobile"
        _description = "Mobile Phones"
        _columns = {
            'id' : fields.integer('ID', readonly=True),
            'mobile_no' : fields.char('Mobile No', size=16, required=True, select=True),
            'serial_no_phone' : fields.char('Phone Serial No', size=16, required=True, select=True),
            'brand' : fields.selection([('samsung','Samsung'),('nokia','Nokia'),('sony','Sony Ericsson')], 'Brand'),
            'model' : fields.char('Model', size=32),
            'serial_no_battery' : fields.char('Battery Serial No', size=64),
            'date_of_purchase' : fields.date('Date of Purchase'),
            'invoice_no' : fields.char('Invoice No', size=32),
            'acc_charger' : fields.boolean('Charger'),
            'acc_usb' : fields.boolean('USB Connector'),
            'acc_memory_drive' : fields.boolean('Memory'),
            'acc_memory_size' : fields.char('Memory Size',size=10),
            'mobile_issue_id' : fields.one2many('asset.mobile.issuetracker', 'issue_id', 'Issues'),
            'mobile_movement_id' : fields.one2many('asset.mobile.movement', 'movement_id', 'Phone Movement'),
            }

asset_mobile()


class asset_mobile_issuetracker(osv.osv):
        _name = "asset.mobile.issuetracker"
        _description = "Mobile Phone Issuetracker"
        _columns = {
                'id' : fields.integer('ID', readonly=True),
                'category' : fields.selection([
                        ('billing','Billing'),
                        ('technical','Technical'),
                        ], 'Category'),
                'issue_id' : fields.many2one('asset.mobile', 'Mobile Phones', ondelete='cascade', select=True),
                'date' : fields.date('Date First Experienced'),
                'issue_details' : fields.text('Issue Details'),
                'status' : fields.selection([
                        ('o','Open'),
                        ('c','Closed'),
                        ], 'Status'),
                }
        _defaults = {
                'status': 'o'
                }
        
asset_mobile_issuetracker()

class asset_mobile_movement(osv.osv):
        _name = "asset.mobile.movement"
        _description = "Phone Movement"
        _columns = {
                'id' : fields.integer('ID', readonly=True,),
                'assigned_to' : fields.many2one('hr.employee', 'Employee', size=64, required=True),
                'date' : fields.date('Date'),
                'condition' : fields.selection([
                        ('bnew','Brand New'),
                        ('secondhand','Second Hand'),
                        ('damaged','Damaged'),
                        ('stolen','Stolen')], 'Status'),
                'remarks' : fields.text('Remarks'),
                'movement_id': fields.many2one('asset.mobile', 'Mobile Phones', ondelete='cascade', select=True),
                }
        _defaults = {
                'condition': 'bnew'
                }

asset_mobile_movement()

class asset_mobile_plans(osv.osv):
    _name="asset.mobile.plans"
    _description="Mobile Phone Plans Monitoring"
    _columns = {
                'id' : fields.integer('ID', readonly=True),
                'account_number' : fields.char('Account Number', size=32, required=True),
                'mobile_number' : fields.char('Mobile Number', size=32, required=True),

                'assigned_to' : fields.many2one('hr.employee', 'Employee', size=64, required=True),
                'credit_limit' : fields.char('Credit Limit', size=32, required=True),
                'telco' : fields.selection([
                                ('globe','Globe'),
                                ('smart','Smart'),
                                ('sun','Sun')], 'Telephone Company'),
		'soa_ids' : fields.one2many('asset.mobile.soa', 'plan_id', 'Statement of Accounts for Mobile Phone Plans'),
        }

asset_mobile_plans()

class asset_mobile_soa(osv.osv):
        _name="asset.mobile.soa"
        _description="Statement of Accounts for Mobile Phone Plans"
        _columns={
                'id' : fields.integer('ID', readonly=True),
                'soa_number' : fields.char('SOA Number', size=32, required=True),
                'statement_date' : fields.date('Statement Date'),
                'start_billing' : fields.date('Billing Period Start'),
                'end_billing' : fields.date('Billing Period End'),
                'total' : fields.float('Total Charges', digits=(16,2)),
                'plan_id' : fields.many2one('asset.mobile.plans', 'Mobile Phone Plans Monitoring', ondelete='cascade', select=True),

        }

asset_mobile_soa()

