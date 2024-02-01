{
    'name': 'Software Reseller',
    'version': '1.0',
    'category': 'Retail',
    'description': u"""
This setup if for IT companies reselling software licenses, and consulting services.🚀 
The typical sale is a 1 year Oracle Database license that is purchased to Oracle, and resold to client at a margin, with extra services to setup the database.
""",
    'depends': [
        'project',
        'knowledge',
        'sale_purchase',
        'sale_timesheet',
        'sale_planning',
        'sale_subscription',
    ],
    'data': [
        'data/ir_attachment_pre.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
        'data/project_task_type.xml',
        'data/product_category.xml',
        'data/account_analytic_plan.xml',
        'data/account_analytic_account.xml',
        'data/project_project.xml',
        'data/uom_category.xml',
        'data/uom_uom.xml',
        'data/planning_role.xml',
        'data/product_product.xml',
        'data/sale_subscription_plan.xml',
        'data/sale_order_template.xml',
        'data/sale_order_template_line.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/product_supplierinfo.xml',
        'demo/product_product.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/project_task.xml',
        'demo/purchase_order_confirm.xml',
        'demo/planning_slot.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
