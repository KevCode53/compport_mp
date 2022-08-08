from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

# Create your views here.

# class MaintenancePDFView(PDFTemplateView):
#     template_name = "maintenances/maintenance_pdf.html"
#     filename = "maintenance_report.pdf"
#     cmd = "maintenance"

#     def get_context_data(self, **kwargs):
#         return super(MaintenancePDFView, self).get_context_data(
#           pagesize="A4",
#           title="Maintenance Report",
#           **kwargs
#         )


def MaintenancePDFView(request):
  context = {}
  html = render_to_string("maintenances/report.html", context)

  response = HttpResponse(content_type="application/pdf")
  response["Content-Disposition"] = "inline; report.pdf"

  font_config = FontConfiguration()
  HTML(string=html).write_pdf(response, font_config=font_config)

  return response
