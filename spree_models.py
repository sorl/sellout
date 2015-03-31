# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class FriendlyIdSlugs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    slug = models.CharField(max_length=-1)
    sluggable_id = models.IntegerField()
    sluggable_type = models.CharField(max_length=50, blank=True)
    scope = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friendly_id_slugs'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class SpreeAddresses(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    firstname = models.CharField(max_length=-1, blank=True)
    lastname = models.CharField(max_length=-1, blank=True)
    address1 = models.CharField(max_length=-1, blank=True)
    address2 = models.CharField(max_length=-1, blank=True)
    city = models.CharField(max_length=-1, blank=True)
    zipcode = models.CharField(max_length=-1, blank=True)
    phone = models.CharField(max_length=-1, blank=True)
    state_name = models.CharField(max_length=-1, blank=True)
    alternative_phone = models.CharField(max_length=-1, blank=True)
    company = models.CharField(max_length=-1, blank=True)
    state_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_addresses'


class SpreeAdjustments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    source_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=-1, blank=True)
    adjustable_id = models.IntegerField(blank=True, null=True)
    adjustable_type = models.CharField(max_length=-1, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True)
    mandatory = models.NullBooleanField()
    eligible = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    state = models.CharField(max_length=-1, blank=True)
    order_id = models.IntegerField(blank=True, null=True)
    included = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'spree_adjustments'


class SpreeAssets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    viewable_id = models.IntegerField(blank=True, null=True)
    viewable_type = models.CharField(max_length=-1, blank=True)
    attachment_width = models.IntegerField(blank=True, null=True)
    attachment_height = models.IntegerField(blank=True, null=True)
    attachment_file_size = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    attachment_content_type = models.CharField(max_length=-1, blank=True)
    attachment_file_name = models.CharField(max_length=-1, blank=True)
    type = models.CharField(max_length=75, blank=True)
    attachment_updated_at = models.DateTimeField(blank=True, null=True)
    alt = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_assets'


class SpreeCalculators(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=-1, blank=True)
    calculable_id = models.IntegerField(blank=True, null=True)
    calculable_type = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    preferences = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'spree_calculators'


class SpreeCountries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    iso_name = models.CharField(max_length=-1, blank=True)
    iso = models.CharField(max_length=-1, blank=True)
    iso3 = models.CharField(max_length=-1, blank=True)
    name = models.CharField(max_length=-1, blank=True)
    numcode = models.IntegerField(blank=True, null=True)
    states_required = models.NullBooleanField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_countries'


class SpreeCreditCards(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    month = models.CharField(max_length=-1, blank=True)
    year = models.CharField(max_length=-1, blank=True)
    cc_type = models.CharField(max_length=-1, blank=True)
    last_digits = models.CharField(max_length=-1, blank=True)
    address_id = models.IntegerField(blank=True, null=True)
    gateway_customer_profile_id = models.CharField(max_length=-1, blank=True)
    gateway_payment_profile_id = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=-1, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    payment_method_id = models.IntegerField(blank=True, null=True)
    default = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'spree_credit_cards'


class SpreeCustomerReturns(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    number = models.CharField(max_length=-1, blank=True)
    stock_location_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_customer_returns'


class SpreeGateways(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=-1, blank=True)
    name = models.CharField(max_length=-1, blank=True)
    description = models.TextField(blank=True)
    active = models.NullBooleanField()
    environment = models.CharField(max_length=-1, blank=True)
    server = models.CharField(max_length=-1, blank=True)
    test_mode = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    preferences = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'spree_gateways'


class SpreeInventoryUnits(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    state = models.CharField(max_length=-1, blank=True)
    variant_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    shipment_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    pending = models.NullBooleanField()
    line_item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_inventory_units'


class SpreeLineItems(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    variant_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    currency = models.CharField(max_length=-1, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax_category_id = models.IntegerField(blank=True, null=True)
    adjustment_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_tax_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    promo_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    included_tax_total = models.DecimalField(max_digits=10, decimal_places=2)
    pre_tax_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_line_items'


class SpreeLogEntries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    source_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=-1, blank=True)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_log_entries'


class SpreeOptionTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True)
    presentation = models.CharField(max_length=100, blank=True)
    position = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_option_types'


class SpreeOptionTypesPrototypes(models.Model):
    prototype_id = models.IntegerField(blank=True, null=True)
    option_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_option_types_prototypes'


class SpreeOptionValues(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    position = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True)
    presentation = models.CharField(max_length=-1, blank=True)
    option_type_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_option_values'


class SpreeOptionValuesVariants(models.Model):
    variant_id = models.IntegerField(blank=True, null=True)
    option_value_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_option_values_variants'


class SpreeOrders(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    number = models.CharField(max_length=32, blank=True)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=-1, blank=True)
    adjustment_total = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    bill_address_id = models.IntegerField(blank=True, null=True)
    ship_address_id = models.IntegerField(blank=True, null=True)
    payment_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_method_id = models.IntegerField(blank=True, null=True)
    shipment_state = models.CharField(max_length=-1, blank=True)
    payment_state = models.CharField(max_length=-1, blank=True)
    email = models.CharField(max_length=-1, blank=True)
    special_instructions = models.TextField(blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    currency = models.CharField(max_length=-1, blank=True)
    last_ip_address = models.CharField(max_length=-1, blank=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    shipment_total = models.DecimalField(max_digits=10, decimal_places=2)
    additional_tax_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    promo_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    channel = models.CharField(max_length=-1, blank=True)
    included_tax_total = models.DecimalField(max_digits=10, decimal_places=2)
    item_count = models.IntegerField(blank=True, null=True)
    approver_id = models.IntegerField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    confirmation_delivered = models.NullBooleanField()
    considered_risky = models.NullBooleanField()
    guest_token = models.CharField(max_length=-1, blank=True)
    canceled_at = models.DateTimeField(blank=True, null=True)
    canceler_id = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    state_lock_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spree_orders'


class SpreeOrdersPromotions(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    promotion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_orders_promotions'


class SpreePaymentCaptureEvents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_payment_capture_events'


class SpreePaymentMethods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=-1, blank=True)
    name = models.CharField(max_length=-1, blank=True)
    description = models.TextField(blank=True)
    active = models.NullBooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    display_on = models.CharField(max_length=-1, blank=True)
    auto_capture = models.NullBooleanField()
    preferences = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'spree_payment_methods'


class SpreePayments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=-1, blank=True)
    payment_method_id = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True)
    response_code = models.CharField(max_length=-1, blank=True)
    avs_response = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    number = models.CharField(max_length=-1, blank=True)
    cvv_response_code = models.CharField(max_length=-1, blank=True)
    cvv_response_message = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_payments'


class SpreePreferences(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    value = models.TextField(blank=True)
    key = models.CharField(unique=True, max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_preferences'


class SpreePrices(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    variant_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=-1, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_prices'


class SpreeProductOptionTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    position = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    option_type_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_product_option_types'


class SpreeProductProperties(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    value = models.CharField(max_length=-1, blank=True)
    product_id = models.IntegerField(blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_product_properties'


class SpreeProducts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1)
    description = models.TextField(blank=True)
    available_on = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=-1, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=-1, blank=True)
    tax_category_id = models.IntegerField(blank=True, null=True)
    shipping_category_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    promotionable = models.NullBooleanField()
    meta_title = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_products'


class SpreeProductsPromotionRules(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    promotion_rule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_products_promotion_rules'


class SpreeProductsTaxons(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    taxon_id = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)  # AutoField?
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_products_taxons'


class SpreePromotionActionLineItems(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    promotion_action_id = models.IntegerField(blank=True, null=True)
    variant_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_promotion_action_line_items'


class SpreePromotionActions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    promotion_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_promotion_actions'


class SpreePromotionCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    code = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_promotion_categories'


class SpreePromotionRules(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    promotion_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    product_group_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    code = models.CharField(max_length=-1, blank=True)
    preferences = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'spree_promotion_rules'


class SpreePromotionRulesUsers(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    promotion_rule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_promotion_rules_users'


class SpreePromotions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    description = models.CharField(max_length=-1, blank=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    starts_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True)
    type = models.CharField(max_length=-1, blank=True)
    usage_limit = models.IntegerField(blank=True, null=True)
    match_policy = models.CharField(max_length=-1, blank=True)
    code = models.CharField(max_length=-1, blank=True)
    advertise = models.NullBooleanField()
    path = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    promotion_category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_promotions'


class SpreeProperties(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    presentation = models.CharField(max_length=-1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_properties'


class SpreePropertiesPrototypes(models.Model):
    prototype_id = models.IntegerField(blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_properties_prototypes'


class SpreePrototypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_prototypes'


class SpreeRefundReasons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    active = models.NullBooleanField()
    mutable = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_refund_reasons'


class SpreeRefunds(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    payment_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    refund_reason_id = models.IntegerField(blank=True, null=True)
    reimbursement_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_refunds'


class SpreeReimbursementCredits(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reimbursement_id = models.IntegerField(blank=True, null=True)
    creditable_id = models.IntegerField(blank=True, null=True)
    creditable_type = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_reimbursement_credits'


class SpreeReimbursementTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    active = models.NullBooleanField()
    mutable = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_reimbursement_types'


class SpreeReimbursements(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    number = models.CharField(max_length=-1, blank=True)
    reimbursement_status = models.CharField(max_length=-1, blank=True)
    customer_return_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_reimbursements'


class SpreeReturnAuthorizationReasons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    active = models.NullBooleanField()
    mutable = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_return_authorization_reasons'


class SpreeReturnAuthorizations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    number = models.CharField(max_length=-1, blank=True)
    state = models.CharField(max_length=-1, blank=True)
    order_id = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    stock_location_id = models.IntegerField(blank=True, null=True)
    return_authorization_reason_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_return_authorizations'


class SpreeReturnItems(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    return_authorization_id = models.IntegerField(blank=True, null=True)
    inventory_unit_id = models.IntegerField(blank=True, null=True)
    exchange_variant_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    pre_tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    included_tax_total = models.DecimalField(max_digits=12, decimal_places=4)
    additional_tax_total = models.DecimalField(max_digits=12, decimal_places=4)
    reception_status = models.CharField(max_length=-1, blank=True)
    acceptance_status = models.CharField(max_length=-1, blank=True)
    customer_return_id = models.IntegerField(blank=True, null=True)
    reimbursement_id = models.IntegerField(blank=True, null=True)
    exchange_inventory_unit_id = models.IntegerField(blank=True, null=True)
    acceptance_status_errors = models.TextField(blank=True)
    preferred_reimbursement_type_id = models.IntegerField(blank=True, null=True)
    override_reimbursement_type_id = models.IntegerField(blank=True, null=True)
    resellable = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'spree_return_items'


class SpreeRoles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_roles'


class SpreeRolesUsers(models.Model):
    role_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_roles_users'


class SpreeShipments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tracking = models.CharField(max_length=-1, blank=True)
    number = models.CharField(max_length=-1, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipped_at = models.DateTimeField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    stock_location_id = models.IntegerField(blank=True, null=True)
    adjustment_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_tax_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    promo_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    included_tax_total = models.DecimalField(max_digits=10, decimal_places=2)
    pre_tax_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_shipments'


class SpreeShippingCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_shipping_categories'


class SpreeShippingMethodCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    shipping_method_id = models.IntegerField()
    shipping_category_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_shipping_method_categories'


class SpreeShippingMethods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    display_on = models.CharField(max_length=-1, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tracking_url = models.CharField(max_length=-1, blank=True)
    admin_name = models.CharField(max_length=-1, blank=True)
    tax_category_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_shipping_methods'


class SpreeShippingMethodsZones(models.Model):
    shipping_method_id = models.IntegerField(blank=True, null=True)
    zone_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_shipping_methods_zones'


class SpreeShippingRates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    shipment_id = models.IntegerField(blank=True, null=True)
    shipping_method_id = models.IntegerField(blank=True, null=True)
    selected = models.NullBooleanField()
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tax_rate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_shipping_rates'


class SpreeSkrillTransactions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=-1, blank=True)
    amount = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=-1, blank=True)
    transaction_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    payment_type = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_skrill_transactions'


class SpreeStateChanges(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    previous_state = models.CharField(max_length=-1, blank=True)
    stateful_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    stateful_type = models.CharField(max_length=-1, blank=True)
    next_state = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_state_changes'


class SpreeStates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    abbr = models.CharField(max_length=-1, blank=True)
    country_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_states'


class SpreeStockItems(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stock_location_id = models.IntegerField(blank=True, null=True)
    variant_id = models.IntegerField(blank=True, null=True)
    count_on_hand = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    backorderable = models.NullBooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_stock_items'


class SpreeStockLocations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    default = models.BooleanField()
    address1 = models.CharField(max_length=-1, blank=True)
    address2 = models.CharField(max_length=-1, blank=True)
    city = models.CharField(max_length=-1, blank=True)
    state_id = models.IntegerField(blank=True, null=True)
    state_name = models.CharField(max_length=-1, blank=True)
    country_id = models.IntegerField(blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True)
    phone = models.CharField(max_length=-1, blank=True)
    active = models.NullBooleanField()
    backorderable_default = models.NullBooleanField()
    propagate_all_variants = models.NullBooleanField()
    admin_name = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_stock_locations'


class SpreeStockMovements(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stock_item_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=-1, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    originator_id = models.IntegerField(blank=True, null=True)
    originator_type = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_stock_movements'


class SpreeStockTransfers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=-1, blank=True)
    reference = models.CharField(max_length=-1, blank=True)
    source_location_id = models.IntegerField(blank=True, null=True)
    destination_location_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    number = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_stock_transfers'


class SpreeStores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    url = models.CharField(max_length=-1, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    seo_title = models.CharField(max_length=-1, blank=True)
    mail_from_address = models.CharField(max_length=-1, blank=True)
    default_currency = models.CharField(max_length=-1, blank=True)
    code = models.CharField(max_length=-1, blank=True)
    default = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_stores'


class SpreeTaxCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    description = models.CharField(max_length=-1, blank=True)
    is_default = models.NullBooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tax_code = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_tax_categories'


class SpreeTaxRates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    amount = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    zone_id = models.IntegerField(blank=True, null=True)
    tax_category_id = models.IntegerField(blank=True, null=True)
    included_in_price = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=-1, blank=True)
    show_rate_in_label = models.NullBooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_tax_rates'


class SpreeTaxonomies(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_taxonomies'


class SpreeTaxons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parent_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    permalink = models.CharField(max_length=-1, blank=True)
    taxonomy_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    icon_file_name = models.CharField(max_length=-1, blank=True)
    icon_content_type = models.CharField(max_length=-1, blank=True)
    icon_file_size = models.IntegerField(blank=True, null=True)
    icon_updated_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    meta_title = models.CharField(max_length=-1, blank=True)
    meta_description = models.CharField(max_length=-1, blank=True)
    meta_keywords = models.CharField(max_length=-1, blank=True)
    depth = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_taxons'


class SpreeTaxonsPromotionRules(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    taxon_id = models.IntegerField(blank=True, null=True)
    promotion_rule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_taxons_promotion_rules'


class SpreeTaxonsPrototypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    taxon_id = models.IntegerField(blank=True, null=True)
    prototype_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_taxons_prototypes'


class SpreeTrackers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    analytics_id = models.CharField(max_length=-1, blank=True)
    active = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_trackers'


class SpreeUsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    encrypted_password = models.CharField(max_length=128, blank=True)
    password_salt = models.CharField(max_length=128, blank=True)
    email = models.CharField(unique=True, max_length=-1, blank=True)
    remember_token = models.CharField(max_length=-1, blank=True)
    persistence_token = models.CharField(max_length=-1, blank=True)
    reset_password_token = models.CharField(max_length=-1, blank=True)
    perishable_token = models.CharField(max_length=-1, blank=True)
    sign_in_count = models.IntegerField()
    failed_attempts = models.IntegerField()
    last_request_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.CharField(max_length=-1, blank=True)
    last_sign_in_ip = models.CharField(max_length=-1, blank=True)
    login = models.CharField(max_length=-1, blank=True)
    ship_address_id = models.IntegerField(blank=True, null=True)
    bill_address_id = models.IntegerField(blank=True, null=True)
    authentication_token = models.CharField(max_length=-1, blank=True)
    unlock_token = models.CharField(max_length=-1, blank=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    spree_api_key = models.CharField(max_length=48, blank=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(max_length=-1, blank=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    confirmation_sent_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spree_users'


class SpreeVariants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sku = models.CharField(max_length=-1)
    weight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    depth = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_master = models.NullBooleanField()
    product_id = models.IntegerField(blank=True, null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    cost_currency = models.CharField(max_length=-1, blank=True)
    track_inventory = models.NullBooleanField()
    tax_category_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    stock_items_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spree_variants'


class SpreeZoneMembers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    zoneable_id = models.IntegerField(blank=True, null=True)
    zoneable_type = models.CharField(max_length=-1, blank=True)
    zone_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spree_zone_members'


class SpreeZones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=-1, blank=True)
    description = models.CharField(max_length=-1, blank=True)
    default_tax = models.NullBooleanField()
    zone_members_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    kind = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = 'spree_zones'
