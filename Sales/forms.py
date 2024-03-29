from django import forms
from .models import (
    CustomerDetails,
    SalesOrder,
    SalesBill,
    SalesItem,
    SalesBillDetails
)
from django.contrib.auth.models import User
from django.forms import formset_factory
from Purchase.models import Vendororder
from Utils.utils import  isValidPhoneNumber, isNoneOrEmpty, isValidText
class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['Name','Email','PhoneNo','CustomerType']

    def clean(self):
        """data from the form is fetched using super function"""
        super(CustomerForm, self).clean()
         
        
        phNo = self.cleaned_data.get('PhoneNo')
        name = self.cleaned_data.get('Name')
        
        
        phNoMsg = isValidPhoneNumber(phNo)
        nameMsg = isValidText(name)
       
        

        if isNoneOrEmpty(phNoMsg) == False:
            self.errors['PhoneNo'] = self.error_class([phNoMsg])


        if isNoneOrEmpty(nameMsg) == False:
            self.errors['Name'] = self.error_class([nameMsg])

        
        return self.cleaned_data




class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['CustomerName','CustomerPhoneNo','Product','ProductQuantity','Price','OrderedDate']

class SelectCustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomerDetails.objects.filter(is_deleted=False)
        self.fields['customer'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = SalesBill
        fields = ['customer']

class SalesItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Vendororder.objects.filter()
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'onChange': 'setPriceAndQuantity(this)', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['perprice'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
    class Meta:
        model = SalesItem
        fields = ['stock', 'quantity', 'perprice']
        
SalesItemFormset = formset_factory(SalesItemForm, extra=1)

class PurchaseDetailsForm(forms.ModelForm):
    class Meta:
        model = SalesBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']


