# Generated by Django 3.2.25 on 2024-09-02 22:59

from decimal import Decimal
import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_measurement.models
import measurement.measures.mass
import saleor.core.db.fields
import saleor.core.utils.editorjs
import saleor.core.utils.json_serializer
import saleor.core.weight


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discount', '0001_initial'),
        ('order', '0001_initial'),
        ('tax', '0001_initial'),
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('description_plaintext', models.TextField(blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='category-backgrounds')),
                ('background_image_alt', models.CharField(blank=True, max_length=128)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='collection-backgrounds')),
                ('background_image_alt', models.CharField(blank=True, max_length=128)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
            ],
            options={
                'ordering': ('slug',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DigitalContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('use_default_settings', models.BooleanField(default=True)),
                ('automatic_fulfillment', models.BooleanField(default=False)),
                ('content_type', models.CharField(choices=[('file', 'digital_product')], default='file', max_length=128)),
                ('content_file', models.FileField(blank=True, upload_to='digital_contents')),
                ('max_downloads', models.IntegerField(blank=True, null=True)),
                ('url_valid_days', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('external_reference', models.CharField(blank=True, db_index=True, max_length=250, null=True, unique=True)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('description_plaintext', models.TextField(blank=True)),
                ('search_document', models.TextField(blank=True, default='')),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
                ('search_index_dirty', models.BooleanField(db_index=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('weight', django_measurement.models.MeasurementField(blank=True, measurement=measurement.measures.mass.Mass, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category')),
            ],
            options={
                'ordering': ('slug',),
                'permissions': (('manage_products', 'Manage products.'),),
            },
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(db_index=True, editable=False, null=True)),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('alt', models.CharField(blank=True, max_length=250)),
                ('type', models.CharField(choices=[('IMAGE', 'An uploaded image or an URL to an image'), ('VIDEO', 'A URL to an external video')], default='IMAGE', max_length=32)),
                ('external_url', models.CharField(blank=True, max_length=256, null=True)),
                ('oembed_data', models.JSONField(blank=True, default=dict)),
                ('to_remove', models.BooleanField(default=False)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='product.product')),
            ],
            options={
                'ordering': ('sort_order', 'pk'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(db_index=True, editable=False, null=True)),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('external_reference', models.CharField(blank=True, db_index=True, max_length=250, null=True, unique=True)),
                ('sku', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('track_inventory', models.BooleanField(default=True)),
                ('is_preorder', models.BooleanField(default=False)),
                ('preorder_end_date', models.DateTimeField(blank=True, null=True)),
                ('preorder_global_threshold', models.IntegerField(blank=True, null=True)),
                ('quantity_limit_per_customer', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('weight', django_measurement.models.MeasurementField(blank=True, measurement=measurement.measures.mass.Mass, null=True)),
            ],
            options={
                'ordering': ('sort_order', 'sku'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVariantChannelListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('price_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('cost_price_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('discounted_price_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('preorder_quantity_threshold', models.IntegerField(blank=True, null=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant_listings', to='channel.channel')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='VariantMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant_media', to='product.productmedia')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant_media', to='product.productvariant')),
            ],
            options={
                'unique_together': {('variant', 'media')},
            },
        ),
        migrations.CreateModel(
            name='VariantChannelListingPromotionRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_amount', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('currency', models.CharField(max_length=3)),
                ('promotion_rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variantlistingpromotionrule', to='discount.promotionrule')),
                ('variant_channel_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variantlistingpromotionrule', to='product.productvariantchannellisting')),
            ],
            options={
                'unique_together': {('variant_channel_listing', 'promotion_rule')},
            },
        ),
        migrations.AddField(
            model_name='productvariantchannellisting',
            name='promotion_rules',
            field=models.ManyToManyField(blank=True, help_text='Promotion rules that were included in the discounted price.', through='product.VariantChannelListingPromotionRule', to='discount.PromotionRule'),
        ),
        migrations.AddField(
            model_name='productvariantchannellisting',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_listings', to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='media',
            field=models.ManyToManyField(through='product.VariantMedia', to='product.ProductMedia'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product.product'),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('kind', models.CharField(choices=[('normal', 'A standard product type.'), ('gift_card', 'A gift card product type.')], max_length=32)),
                ('has_variants', models.BooleanField(default=True)),
                ('is_shipping_required', models.BooleanField(default=True)),
                ('is_digital', models.BooleanField(default=False)),
                ('weight', django_measurement.models.MeasurementField(default=saleor.core.weight.zero_weight, measurement=measurement.measures.mass.Mass)),
                ('tax_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_types', to='tax.taxclass')),
            ],
            options={
                'ordering': ('slug',),
                'permissions': (('manage_product_types_and_attributes', 'Manage product types and attributes.'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=35)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductChannelListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('visible_in_listings', models.BooleanField(default=False)),
                ('available_for_purchase_at', models.DateTimeField(blank=True, null=True)),
                ('currency', models.CharField(max_length=3)),
                ('discounted_price_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('discounted_price_dirty', models.BooleanField(default=False)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_listings', to='channel.channel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_listings', to='product.product')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='default_variant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.producttype'),
        ),
        migrations.AddField(
            model_name='product',
            name='tax_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='tax.taxclass'),
        ),
        migrations.CreateModel(
            name='DigitalContentUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('download_num', models.IntegerField(default=0)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='product.digitalcontent')),
                ('line', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='digital_content_url', to='order.orderline')),
            ],
        ),
        migrations.AddField(
            model_name='digitalcontent',
            name='product_variant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='digital_content', to='product.productvariant'),
        ),
        migrations.CreateModel(
            name='CollectionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=35)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.collection')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(db_index=True, editable=False, null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collectionproduct', to='product.collection')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collectionproduct', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionChannelListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_listings', to='channel.channel')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_listings', to='product.collection')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='collections', through='product.CollectionProduct', to='product.Product'),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=35)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', saleor.core.db.fields.SanitizedJSONField(blank=True, null=True, sanitizer=saleor.core.utils.editorjs.clean_editor_js)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariantTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=35)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.productvariant')),
            ],
            options={
                'unique_together': {('language_code', 'product_variant')},
            },
        ),
        migrations.AddIndex(
            model_name='productvariantchannellisting',
            index=django.contrib.postgres.indexes.GinIndex(fields=['price_amount', 'channel_id'], name='product_pro_price_a_fb6bd3_gin'),
        ),
        migrations.AlterUniqueTogether(
            name='productvariantchannellisting',
            unique_together={('variant', 'channel')},
        ),
        migrations.AddIndex(
            model_name='productvariant',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='productvariant_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='productvariant',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='productvariant_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='producttype',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='producttype_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='producttype',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='producttype_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='producttype',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name', 'slug'], name='product_type_search_gin', opclasses=['gin_trgm_ops', 'gin_trgm_ops']),
        ),
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together={('language_code', 'product')},
        ),
        migrations.AddIndex(
            model_name='productmedia',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='productmedia_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='productmedia',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='productmedia_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='productchannellisting',
            index=models.Index(fields=['published_at'], name='product_pro_publish_a3c049_idx'),
        ),
        migrations.AddIndex(
            model_name='productchannellisting',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['discounted_price_amount'], name='product_pro_discoun_3145f3_btree'),
        ),
        migrations.AlterUniqueTogether(
            name='productchannellisting',
            unique_together={('product', 'channel')},
        ),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_document'], name='product_search_gin', opclasses=['gin_trgm_ops']),
        ),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='product_tsearch'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name', 'slug'], name='product_gin', opclasses=['gin_trgm_ops', 'gin_trgm_ops']),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['category_id', 'slug'], name='product_pro_categor_8de99d_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='product_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='product_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='digitalcontent',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='digitalcontent_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='digitalcontent',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='digitalcontent_meta_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='collectiontranslation',
            unique_together={('language_code', 'collection')},
        ),
        migrations.AlterUniqueTogether(
            name='collectionproduct',
            unique_together={('collection', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='collectionchannellisting',
            unique_together={('collection', 'channel')},
        ),
        migrations.AddIndex(
            model_name='collection',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='collection_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='collection_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name', 'slug'], name='collection_search_gin', opclasses=['gin_trgm_ops', 'gin_trgm_ops']),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together={('language_code', 'category')},
        ),
        migrations.AddIndex(
            model_name='category',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='category_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='category_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name', 'slug', 'description_plaintext'], name='category_search_name_slug_gin', opclasses=['gin_trgm_ops', 'gin_trgm_ops', 'gin_trgm_ops']),
        ),
        migrations.AddIndex(
            model_name='category',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['updated_at'], name='updated_at_idx'),
        ),
    ]
