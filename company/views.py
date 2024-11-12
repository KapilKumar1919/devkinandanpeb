import pandas as pd
import openpyxl

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from company.models import Client, Company, Contact, Job, Service, Quotation
from employee.models import Employee
from country.models import Country
from currency.models import Currency
from company.forms import ContactForm, QuotationForm

def upload_client_details(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']

        try:
            # Assuming the first sheet in the Excel file contains client details
            df = pd.read_excel(excel_file)

            # Ensure that the required columns are present
            required_columns = [
                'Client Name', 'Client Email', 'Client Phone', 'GST', 
                'City', 'State', 'Zip Code', 'Country', 'Client Since (Months)'
            ]
            missing_columns = set(required_columns) - set(df.columns)

            if missing_columns:
                raise ValueError(f'Missing required columns: {missing_columns}')

            for _, row in df.iterrows():
                # Create Client object for each row in the Excel file
                Client.objects.create(
                    company=Company.objects.first(),  # Replace with the actual company
                    name=row['Client Name'],
                    email=row['Client Email'],
                    phone=row['Client Phone'],
                    gst=row['GST'],
                    city=row['City'],
                    state=row['State'],
                    zip_code=row['Zip Code'],
                    country=Country.objects.get(name=row['Country']),  # Replace with the actual country
                    client_since=row['Client Since (Months)'],
                    created_by=request.user,  # Assuming you have a logged-in user
                )

            messages.success(request, 'Client details are uploaded successfully.')

        except Exception as e:
            messages.error(request, f'Error uploading client details: {str(e)}')

    client_admin_url = reverse('admin:company_client_changelist')
    return redirect(client_admin_url)

class DownloadClientDetailsView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=client_details.xlsx'

        # Create a workbook and add a worksheet.
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # Add headers to the worksheet based on your Client model fields
        headers = [
            "Company", "Client Name", "Client Email", "Client Phone",
            "GST", "City", "State", "Zip Code", "Country",
            "Client Since (Months)", "Created By", "Updated By"
        ]
        worksheet.append(headers)

        # Retrieve client records from the database
        clients = Client.objects.all()

        # Add client data to the worksheet
        for client in clients:
            row_data = [
                client.company.business_name, client.name, client.email, client.phone,
                client.gst, client.city, client.state, client.zip_code,
                client.country.name if client.country else '',
                client.client_since, client.created_by.username if client.created_by else '',
                client.updated_by.username if client.updated_by else ''
            ]
            worksheet.append(row_data)

        # Save the workbook to the response
        workbook.save(response)

        return response

download_client_details = DownloadClientDetailsView.as_view()

class CompanyMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.first()
        context['services'] = Service.objects.all()[::2]
        return context

class HomePageView(CompanyMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Job.objects.all().count()
        total_hours_of_work = Job.objects.aggregate(Sum('total_working_hours'))['total_working_hours__sum']
        context['hours_of_work'] = total_hours_of_work if total_hours_of_work else 0
        context['employees'] = Employee.objects.all().count()
        context['services'] = Service.objects.all()[:3]
        context['services_remaining'] = Service.objects.all()[3:6]
        context['clients'] = Client.objects.all()[:6]
        return context

class ThankYouPageView(CompanyMixin, TemplateView):
    template_name = 'thank_you.html'

class ContactPageView(CompanyMixin, TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ContactForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        # Retrieve individual form fields from POST data
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate each field (you can add more specific validation)
        if not name or not mobile or not email or not subject or not message:
            # Handle validation error
            form = ContactForm(request.POST)
            return render(request, self.template_name, {'form': form, 'error_message': 'Please fill in all fields'})

        # Create and save the Contact object
        contact = Contact.objects.create(name=name, mobile=mobile, email=email, subject=subject, message=message)
        contact.save()
        self.send_email_to_customer(contact)
        return redirect('thank-you')

    def send_email_to_customer(self, contact):
        subject = 'Thank you for your inquiry'
        from_email = settings.EMAIL_FROM
        to_email = contact.email  # Use the customer's email address from the Contact model

        # Load the email template
        html_message = render_to_string('email/email_template.html', {'contact': contact})
        plain_message = strip_tags(html_message)

        # Send the email with both plain text and HTML alternatives
        email = EmailMultiAlternatives(subject, plain_message, from_email, [to_email])
        email.attach_alternative(html_message, "text/html")
        email.send()

class OurTeamPageView(CompanyMixin, TemplateView):
    template_name = 'our_team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(is_leader=True)
        return context

class ProjectsPageView(CompanyMixin, TemplateView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()[:6]
        return context

class ServicePageView(CompanyMixin, TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context

class AboutUsPageView(CompanyMixin, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Job.objects.all().count()
        total_hours_of_work = Job.objects.aggregate(Sum('total_working_hours'))['total_working_hours__sum']
        context['hours_of_work'] = total_hours_of_work if total_hours_of_work else 0
        context['employees'] = Employee.objects.all().count()
        context['employee_details'] = Employee.objects.filter(is_leader=True)
        return context

class ProjectDetailPageView(CompanyMixin, DetailView):
    template_name = 'project_detail.html'
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class QuotationPageView(CompanyMixin, TemplateView):
    template_name = 'quotation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = QuotationForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        # Retrieve individual form fields from POST data
        company_name = request.POST.get('companyName')
        contact_person = request.POST.get('contactPerson')
        contact_no = request.POST.get('contactNo')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        address = request.POST.get('address')
        remark = request.POST.get('remark')        
        plan_file = request.FILES.get('planImage')

        # Validate each field (you can add more specific validation)
        if not company_name or not contact_person or not email or not contact_no:
            # Handle validation error
            form = QuotationForm(request.POST, request.FILES)
            return render(request, self.template_name, {'form': form, 'error_message': 'Please fill in all fields'})

        # Create and save the Contact object
        quotation = Quotation.objects.create(
            company_name=company_name,
            contact_person=contact_person,
            contact_no=contact_no,
            email=email,
            subject=subject,
            address=address,
            remark=remark,
            plan_file=plan_file
            )
        quotation.save()
        return redirect('thank-you')
