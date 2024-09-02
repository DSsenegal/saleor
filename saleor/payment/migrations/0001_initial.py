# Generated by Django 3.2.25 on 2024-09-02 22:59

from decimal import Decimal
import django.contrib.postgres.fields
import django.contrib.postgres.indexes
import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import saleor.core.utils.json_serializer
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0001_initial'),
        ('app', '0001_initial'),
        ('account', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('gateway', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('to_confirm', models.BooleanField(default=False)),
                ('partial', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('charge_status', models.CharField(choices=[('not-charged', 'Not charged'), ('pending', 'Pending'), ('partially-charged', 'Partially charged'), ('fully-charged', 'Fully charged'), ('partially-refunded', 'Partially refunded'), ('fully-refunded', 'Fully refunded'), ('refused', 'Refused'), ('cancelled', 'Cancelled')], default='not-charged', max_length=20)),
                ('token', models.CharField(blank=True, default='', max_length=512)),
                ('total', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('captured_amount', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('currency', models.CharField(max_length=3)),
                ('store_payment_method', models.CharField(choices=[('on_session', 'On session'), ('off_session', 'Off session'), ('none', 'None')], default='none', max_length=11)),
                ('billing_email', models.EmailField(blank=True, max_length=254)),
                ('billing_first_name', models.CharField(blank=True, max_length=256)),
                ('billing_last_name', models.CharField(blank=True, max_length=256)),
                ('billing_company_name', models.CharField(blank=True, max_length=256)),
                ('billing_address_1', models.CharField(blank=True, max_length=256)),
                ('billing_address_2', models.CharField(blank=True, max_length=256)),
                ('billing_city', models.CharField(blank=True, max_length=256)),
                ('billing_city_area', models.CharField(blank=True, max_length=128)),
                ('billing_postal_code', models.CharField(blank=True, max_length=256)),
                ('billing_country_code', models.CharField(blank=True, max_length=2)),
                ('billing_country_area', models.CharField(blank=True, max_length=256)),
                ('cc_first_digits', models.CharField(blank=True, default='', max_length=6)),
                ('cc_last_digits', models.CharField(blank=True, default='', max_length=4)),
                ('cc_brand', models.CharField(blank=True, default='', max_length=40)),
                ('cc_exp_month', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('cc_exp_year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000)])),
                ('payment_method_type', models.CharField(blank=True, max_length=256)),
                ('customer_ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('extra_data', models.TextField(blank=True, default='')),
                ('return_url', models.URLField(blank=True, null=True)),
                ('psp_reference', models.CharField(blank=True, db_index=True, max_length=512, null=True)),
                ('checkout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='checkout.checkout')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='order.order')),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('handle_payments', 'Handle payments'),),
            },
        ),
        migrations.CreateModel(
            name='TransactionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('use_old_id', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('idempotency_key', models.CharField(blank=True, max_length=512, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('message', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('psp_reference', models.CharField(blank=True, max_length=512, null=True)),
                ('available_actions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('charge', 'Charge payment'), ('refund', 'Refund payment'), ('cancel', 'Cancel payment')], max_length=128), default=list, size=None)),
                ('currency', models.CharField(max_length=3)),
                ('charged_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('authorized_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('refunded_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('canceled_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('refund_pending_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('charge_pending_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('authorize_pending_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('cancel_pending_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('app_identifier', models.CharField(blank=True, max_length=256, null=True)),
                ('last_refund_success', models.BooleanField(default=True)),
                ('app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.app')),
                ('checkout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_transactions', to='checkout.checkout')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payment_transactions', to='order.order')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='account.user')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='TransactionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('idempotency_key', models.CharField(blank=True, max_length=512, null=True)),
                ('psp_reference', models.CharField(blank=True, max_length=512, null=True)),
                ('message', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('currency', models.CharField(max_length=3)),
                ('type', models.CharField(choices=[('authorization_success', 'Represents success authorization'), ('authorization_failure', 'Represents failure authorization'), ('authorization_adjustment', 'Represents authorization adjustment'), ('authorization_request', 'Represents authorization request'), ('authorization_action_required', 'Represents additional actions required for authorization.'), ('charge_action_required', 'Represents additional actions required for charge.'), ('charge_success', 'Represents success charge'), ('charge_failure', 'Represents failure charge'), ('charge_back', 'Represents chargeback.'), ('charge_request', 'Represents charge request'), ('refund_success', 'Represents success refund'), ('refund_failure', 'Represents failure refund'), ('refund_reverse', 'Represents reverse refund'), ('refund_request', 'Represents refund request'), ('cancel_success', 'Represents success cancel'), ('cancel_failure', 'Represents failure cancel'), ('cancel_request', 'Represents cancel request'), ('info', 'Represents an info event')], default='info', max_length=128)),
                ('amount_value', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=12)),
                ('app_identifier', models.CharField(blank=True, max_length=256, null=True)),
                ('include_in_calculations', models.BooleanField(default=False)),
                ('app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.app')),
                ('related_granted_refund', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_events', to='order.ordergrantedrefund')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='payment.transactionitem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='account.user')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(blank=True, default='', max_length=512)),
                ('kind', models.CharField(choices=[('external', 'External reference'), ('auth', 'Authorization'), ('pending', 'Pending'), ('action_to_confirm', 'Action to confirm'), ('refund', 'Refund'), ('refund_ongoing', 'Refund in progress'), ('capture', 'Capture'), ('void', 'Void'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], max_length=25)),
                ('is_success', models.BooleanField(default=False)),
                ('action_required', models.BooleanField(default=False)),
                ('action_required_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('currency', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('error', models.TextField(null=True)),
                ('customer_id', models.CharField(max_length=256, null=True)),
                ('gateway_response', models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('already_processed', models.BooleanField(default=False)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='payment.payment')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AddIndex(
            model_name='transactionitem',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='transactionitem_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='transactionitem',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='transactionitem_meta_idx'),
        ),
        migrations.AddConstraint(
            model_name='transactionitem',
            constraint=models.UniqueConstraint(fields=('app_identifier', 'idempotency_key'), name='unique_transaction_idempotency'),
        ),
        migrations.AddConstraint(
            model_name='transactionevent',
            constraint=models.UniqueConstraint(fields=('transaction_id', 'idempotency_key'), name='unique_transaction_event_idempotency'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='payment_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='payment_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=django.contrib.postgres.indexes.GinIndex(fields=['order_id', 'is_active', 'charge_status'], name='payment_pay_order_i_f22aa2_gin'),
        ),
    ]
