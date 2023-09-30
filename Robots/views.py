
from django.http import HttpResponse
import openpyxl
from .models import Robot

def export_data_to_xlsx(request):
    workbook = openpyxl.Workbook()

    versions = Robot.objects.values_list('version', flat=True).distinct()

    models = Robot.objects.values_list('model', flat=True).distinct()

    for model in models:
        model_sheet = workbook.create_sheet(f'Model {model}')

        headers = ['Модель', 'Версия', 'Количество за неделю']
        model_sheet.append(headers)

        for version in versions:
            robot_data = Robot.objects.filter(model=model, version=version)
            for data_row in robot_data:
                row = [data_row.model, data_row.version, data_row.count_week]
                model_sheet.append(row)

    del workbook["Sheet"]

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'
    workbook.save(response)

    return response
