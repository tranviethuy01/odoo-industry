# -*- coding: utf-8 -*-
{
    'name': 'Certification organism',
    'version': '1.0',
    'category': 'Industry',
    'description': u"""
This module setup your database to easily use odoo in a certification company.
""",
    'author': 'Odoo S.A.',
    'depends': [
        'web_studio',
        'knowledge',
        'industry_fsm_sale_report',
        'project',
        'hr_timesheet',
        'hr_holidays',
        'crm',
        'sale_timesheet',
        'product_margin',
        'website_appointment'
    ],
    'data': [
        'data/res_config_setting.xml',
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_model_access.xml',
        'data/ir_rule.xml',
        'data/project_task_type.xml',
        'data/account_analytic_plan.xml',
        'data/account_analytic_account.xml',
        'data/worksheet_template.xml',
        'data/project_project.xml',
        'data/product_product.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_member.xml',
        'data/ir_attachment_post.xml',
    ],
    'demo': [
        'demo/website.xml',
        'demo/res_partner.xml',
        'demo/hr_leave.xml',
        'demo/crm_tag.xml',
        'demo/crm_lead.xml',
        'demo/project_tags.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_post_action.xml',
        'demo/website_view.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/x_control_charging_station.xml',
    ],
    'application': False,
    'license': 'OPL-1',
    'images': ['images/main.png'],

}
