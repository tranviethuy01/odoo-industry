{
    'name': 'Bike Leasing',
    'version': '1.0',
    'category': 'Services',
    'description': """
This module is a complete solution for the bike leasing industry, simplifying lease management, bike tracking, and customer service. It's perfect for businesses aiming to streamline operations and embrace the growing trend of sustainable mobility.
""",
    'depends': [
        'base_automation',
        'calendar',
        'knowledge',
        'payment_custom',
        'purchase_stock',
        'sale_management',
        'sale_planning',
        'sale_service',
        'sign',
        'stock_delivery',
        'web_studio',
        'website_helpdesk',
        'website_payment',
        'website_sale',
        'theme_vehicle',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_server.xml',
        'data/base_automation.xml',
        'data/ir_default.xml',
        'data/product_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/product_pricelist.xml',
        'data/product_pricelist_item.xml',
        'data/delivery_carrier.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/ir_attachment_post.xml',
        'data/website_view.xml',
        'data/payment_provider.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/website.xml',
        'demo/res_partner.xml',
        'demo/hr_employee.xml',
        'demo/product_supplierinfo.xml',
        'demo/product_template.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/website_view.xml',
        'demo/website_theme_apply.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
        'demo/helpdesk_ticket.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'bike_leasing/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
        "data/website_view.xml",
        "demo/website_view.xml",
    ],
    'images': ['images/main.png'],
}
