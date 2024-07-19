{
    'name': 'Property Owner Association',
    'version': '1.1',
    'category': 'Services',
    'description': """
This industry is tailor-made for Property Owner Association businesses that aim at managing co-ownership properties. Such a business is complex because it implies managing all the aspects of the properties while fairly splitting the charges.
Moreover, the business is legally regulated in lots of countries under different names: condo in the US, co-ownership in Canada, joint domination in the UK, property syndicate in France, syndic in Belgium, etc
""",
    'depends': [
        'account_check_printing',
        'account_followup',
        'account_payment',
        'accountant',
        'contacts',
        'calendar',
        'documents_product',
        'documents_project_sale',
        'documents_spreadsheet',
        'helpdesk_sale_timesheet',
        'hr',
        'knowledge',
        'sale_subscription',
        'web_studio',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model.xml',
        'data/ir_actions_server.xml',
        'data/ir_model_fields.xml',
        'data/ir_filters.xml',
        'data/ir_default.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_view.xml',
        'data/ir_ui_menu.xml',
        'data/ir_model_access.xml',
        'data/ir_rule.xml',
        'data/project_task_type.xml',
        'data/documents_folder.xml',
        'data/project_project.xml',
        'data/project_task.xml',
        'data/product_product.xml',
        'data/sale_order_template.xml',
        'data/sale_order_template_line.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/x_buildings_tag.xml',
        'data/x_properties_types.xml',
        'data/x_properties_tag.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/account_analytic_account.xml',
        'demo/documents_folder.xml',
        'demo/project_project.xml',
        'demo/res_partner.xml',
        'demo/res_company.xml',
        'demo/x_buildings.xml',
        'demo/x_properties.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_post.xml',
        'demo/project_task.xml',
        'demo/helpdesk_team.xml',
        'demo/helpdesk_ticket.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'condominium/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
    ],
    'images': ['images/main.png'],
}
