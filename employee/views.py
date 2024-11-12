import openpyxl
import pandas as pd

from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from employee.models import Employee


def upload_employee_details(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']

        try:
            # Assuming the first sheet in the Excel file contains employee details
            df = pd.read_excel(excel_file)

            # Ensure that the required columns are present
            required_columns = [
                'Emp Code', 'Full Name', 'Date of Joining', 'Division', 'Designation',
                'Mobile', 'Emergency Contact', 'Email', 'Current Address',
                'Permanent Address', 'Total Experience', 'Experience with Us',
                'Marital Status', 'Gender', 'Aadhar Card Number', 'PAN',
                'Bank Name', 'Bank Account Number', 'Bank IFSC'
            ]
            missing_columns = set(required_columns) - set(df.columns)

            if missing_columns:
                raise ValueError(f'Missing required columns: {missing_columns}')

            for _, row in df.iterrows():
                # Create Employee object for each row in the Excel file
                Employee.objects.create(
                    emp_code=row['Emp Code'],
                    name=row['Full Name'],
                    date_of_joining=row['Date of Joining'],
                    division=row['Division'],
                    designation=row['Designation'],
                    mobile=row['Mobile'],
                    emergency_contact=row['Emergency Contact'],
                    email=row['Email'],
                    current_address=row['Current Address'],
                    permanent_address=row['Permanent Address'],
                    total_experience=row['Total Experience'],
                    experience_with_new_company=row['Experience with Us'],
                    marital_status=row['Marital Status'],
                    gender=row['Gender'],
                    aadhar_card_number=row['Aadhar Card Number'],
                    pan_card=row['PAN'],
                    bank_name=row['Bank Name'],
                    bank_account_number=row['Bank Account Number'],
                    bank_ifsc=row['Bank IFSC'],
                    updated_by=request.user  # Assuming you have a logged-in user
                )

            messages.success(request, 'Employee details are uploaded successfully.')

        except Exception as e:
            messages.error(request, f'Error uploading employee details: {str(e)}')

    employee_admin_url = reverse('admin:employee_employee_changelist')
    return redirect(employee_admin_url)


class DownloadEmployeeDetailsView(View):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=employee_details.xlsx'

        # Create a workbook and add a worksheet.
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # Add headers to the worksheet based on your Employee model fields
        headers = [
            "Employee Code", "Name", "Date of Joining", "Division", "Designation",
            "Mobile", "Emergency Contact", "Email", "Current Address", "Permanent Address",
            "Total Experience", "Experience with Us", "Marital Status", "Gender",
            "Aadhar Card Number", "PAN", "Bank Name", "Bank Account Number", "Bank IFSC",
            "Updated By"
        ]
        worksheet.append(headers)

        # Retrieve employee records from the database
        employees = Employee.objects.all()

        # Add employee data to the worksheet
        for employee in employees:
            row_data = [
                employee.emp_code, employee.name, employee.date_of_joining, employee.division,
                employee.designation, employee.mobile, employee.emergency_contact, employee.email,
                employee.current_address, employee.permanent_address, employee.total_experience,
                employee.experience_with_new_company, employee.get_marital_status_display(),
                employee.get_gender_display(), employee.aadhar_card_number, employee.pan_card,
                employee.bank_name, employee.bank_account_number, employee.bank_ifsc,
                employee.updated_by.username if employee.updated_by else '',
            ]
            worksheet.append(row_data)

        # Save the workbook to the response
        workbook.save(response)

        return response

download_employee_details = DownloadEmployeeDetailsView.as_view()

