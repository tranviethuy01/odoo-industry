{
    'name': 'Hardware Store',
    'version': '1.0',
    'category': 'Retail',
    'description': """
For Hardware Stores that carry a large selection of products: plumbing, machinery, household, gardening, carpenter and electrical, etc.
Using Point of Sale, Inventory, Sales, Purchase, Accounting, Contact, Employee, Dashboard, Barcode, and Documents to grow their business.
    """,
    'depends': [
        'base_geolocalize',
        'barcodes',
        'contacts',
        'knowledge',
        'pos_sale',
        'purchase_stock',
        'sale_loyalty',
        'sale_margin',
        'sale_purchase',
        'stock_delivery',
    ],
    'data': [
        'data/res_config_setting.xml',
        'data/ir_attachment_pre.xml',
        'data/product_category.xml',
        'data/pos_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/product_pricelist_item.xml',
        'data/pos_payment_method.xml',
        'data/pos_config.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
    ],
    'demo': [
        'demo/product_quantity.xml',
        'demo/stock_warehouse_orderpoint.xml',
        'demo/res_partner.xml',
        'demo/product_supplierinfo.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/function_pickup.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
