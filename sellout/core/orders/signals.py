from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from sellout.orders.models import OrderLine


def set_order_line_calculated_fields(line):
    # do not update fields if the order is locked
    if line.order.locked:
        return
    line.name = line.variant.name
    line.price_tax_excl = line.variant.price_tax_excl
    line.price_tax_incl = line.variant.price_tax_incl


def set_order_calculated_fields(order):
    order.item_count = 0
    order.product_total_tax_excl = 0
    order.product_total_tax_incl = 0
    for line in order.order_lines.all():
        order.item_count += line.quantity
        order.product_total_tax_excl += line.price_tax_excl * line.quantity
        order.product_total_tax_incl += line.price_tax_incl * line.quantity
