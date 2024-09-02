# Generated by Django 3.2.25 on 2024-09-02 22:59

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import saleor.core.db.fields
import saleor.core.utils.editorjs
import saleor.core.utils.json_serializer
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDiscount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('type', models.CharField(choices=[('sale', 'Sale'), ('voucher', 'Voucher'), ('manual', 'Manual'), ('promotion', 'Promotion'), ('order_promotion', 'Order promotion')], default='manual', max_length=64)),
                ('value_type', models.CharField(choices=[('fixed', 'fixed'), ('percentage', '%')], default='fixed', max_length=10)),
                ('value', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('amount_value', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('currency', models.CharField(max_length=3)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('translated_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('voucher_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ('created_at', 'id'),
            },
        ),
        migrations.CreateModel(
            name='CheckoutLineDiscount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('type', models.CharField(choices=[('sale', 'Sale'), ('voucher', 'Voucher'), ('manual', 'Manual'), ('promotion', 'Promotion'), ('order_promotion', 'Order promotion')], default='manual', max_length=64)),
                ('value_type', models.CharField(choices=[('fixed', 'fixed'), ('percentage', '%')], default='fixed', max_length=10)),
                ('value', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('amount_value', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('currency', models.CharField(max_length=3)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('translated_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('voucher_code', models.CharField(blank=True, max_length=255, null=True)),
                ('unique_type', models.CharField(blank=True, choices=[('sale', 'Sale'), ('voucher', 'Voucher'), ('manual', 'Manual'), ('promotion', 'Promotion'), ('order_promotion', 'Order promotion')], max_length=64, null=True)),
            ],
            options={
                'ordering': ('created_at', 'id'),
            },
        ),
        migrations.CreateModel(
            name='OrderDiscount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('type', models.CharField(choices=[('sale', 'Sale'), ('voucher', 'Voucher'), ('manual', 'Manual'), ('promotion', 'Promotion'), ('order_promotion', 'Order promotion')], default='manual', max_length=64)),
                ('value_type', models.CharField(choices=[('fixed', 'fixed'), ('percentage', '%')], default='fixed', max_length=10)),
                ('value', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('amount_value', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('currency', models.CharField(max_length=3)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('translated_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('voucher_code', models.CharField(blank=True, max_length=255, null=True)),
                ('old_id', models.PositiveIntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'ordering': ('created_at', 'id'),
            },
        ),
        migrations.CreateModel(
            name='OrderLineDiscount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('type', models.CharField(choices=[('sale', 'Sale'), ('voucher', 'Voucher'), ('manual', 'Manual'), ('promotion', 'Promotion'), ('order_promotion', 'Order promotion')], default='manual', max_length=64)),
                ('value_type', models.CharField(choices=[('fixed', 'fixed'), ('percentage', '%')], default='fixed', max_length=10)),
                ('value', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('amount_value', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('currency', models.CharField(max_length=3)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('translated_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('voucher_code', models.CharField(blank=True, max_length=255, null=True)),
                ('unique_type', models.CharField(blank=True, choices=[('sale', 'Sale'), ('voucher', 'Voucher'), ('manual', 'Manual'), ('promotion', 'Promotion'), ('order_promotion', 'Order promotion')], max_length=64, null=True)),
            ],
            options={
                'ordering': ('created_at', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('catalogue', 'Catalogue'), ('order', 'Order')], default='catalogue', max_length=255)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('old_sale_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_notification_scheduled_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name', 'pk'),
                'permissions': (('manage_discounts', 'Manage promotions and vouchers.'),),
            },
        ),
        migrations.CreateModel(
            name='PromotionEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('type', models.CharField(choices=[('promotion_created', 'Promotion created'), ('promotion_updated', 'Promotion updated'), ('promotion_started', 'Promotion started'), ('promotion_ended', 'Promotion ended'), ('rule_created', 'Rule created'), ('rule_updated', 'Rule updated'), ('rule_deleted', 'Rule deleted')], max_length=255)),
                ('parameters', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='PromotionRule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('catalogue_predicate', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder)),
                ('order_predicate', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder)),
                ('reward_value_type', models.CharField(blank=True, choices=[('fixed', 'fixed'), ('percentage', '%')], max_length=255, null=True)),
                ('reward_value', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('reward_type', models.CharField(blank=True, choices=[('subtotal_discount', 'subtotal_discount'), ('gift', 'gift')], max_length=255, null=True)),
                ('old_channel_listing_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('variants_dirty', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='PromotionRule_Variants',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionRuleTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=35)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=35)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('type', models.CharField(choices=[('entire_order', 'Entire order'), ('shipping', 'Shipping'), ('specific_product', 'Specific products, collections and categories')], default='entire_order', max_length=20)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('usage_limit', models.PositiveIntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('apply_once_per_order', models.BooleanField(default=False)),
                ('apply_once_per_customer', models.BooleanField(default=False)),
                ('single_use', models.BooleanField(default=False)),
                ('only_for_staff', models.BooleanField(default=False)),
                ('discount_value_type', models.CharField(choices=[('fixed', 'fixed'), ('percentage', '%')], default='fixed', max_length=10)),
                ('countries', django_countries.fields.CountryField(blank=True, max_length=749, multiple=True)),
                ('min_checkout_items_quantity', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='VoucherCode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(db_index=True, max_length=255, unique=True)),
                ('used', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('voucher', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='discount.voucher')),
            ],
            options={
                'ordering': ('-created_at', 'code'),
            },
        ),
        migrations.CreateModel(
            name='VoucherTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=35)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='discount.voucher')),
            ],
            options={
                'ordering': ('language_code', 'voucher', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='VoucherCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(max_length=254)),
                ('voucher_code', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='discount.vouchercode')),
            ],
            options={
                'ordering': ('voucher_code', 'customer_email', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='VoucherChannelListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_value', models.DecimalField(decimal_places=3, max_digits=12)),
                ('currency', models.CharField(max_length=3)),
                ('min_spent_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voucher_listings', to='channel.channel')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_listings', to='discount.voucher')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
