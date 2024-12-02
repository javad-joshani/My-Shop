from modeltranslation.translator import register, TranslationOptions
from shop.models import Category,Customer,Profile,Product,Order,Slider

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Customer)
class CustomerTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')

@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('country', 'state', 'city', 'address')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description','category')

@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('address', )

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', )