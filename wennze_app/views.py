from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def managed(request):
    return render(request, "managed.html")

def cyber(request):
    return render(request, "cyber.html")

def consulting(request):
    return render(request, "consulting.html")

def cloud(request):
    return render(request, "cloud.html")

def base_solutions(request):
    return render(request, "base_solutions.html")

# ====== Managed IT services solutions ======= #
def co_managed(request):
    return render(request, "co-managed.html")

def assets_management(request):
    return render(request, "it_assets.html")

def support(request):
    return render(request, "support.html")

def network_admin(request):
    return render(request, "network_admin.html")

def server_management(request):
    return render(request, "server_management.html")

# ====== Cybersecurity services solutions ======= #
def cyber_risk(request):
    return render(request, "cyber_risk.html")

def dark_web(request):
    return render(request, "dark_web.html")

def endpoint_solutions(request):
    return render(request, "endpoint_solutions.html")

def incident_response(request):
    return render(request, "incident_response.html")

def pen_testing(request):
    return render(request, "pen_testing.html")

# ===== IT consulting solutions ====== #
def business_intelligence(request):
    return render(request, "business_intelligence.html")

def dev_ops(request):
    return render(request, "dev_ops.html")

def it_outsourcing(request):
    return render(request, "it_outsourcing.html")

def governance_risk_compliance(request):
    return render(request, "grc.html")

def share_point(request):
    return render(request, "share_point.html")

def staff_augmentation(request):
    return render(request, "staff_augmentation.html")

def virtual_cisco(request):
    return render(request, "virtual_cisco.html")

def virtual_chief_info_officer(request):
    return render(request, "vcio.html")

def web_development(request):
    return render(request, "web_dev.html")

# ===== Cloud Services ===== #
def azure(request):
    return render(request, "azure.html")

def cloud_storage(request):
    return render(request, "cloud_storage.html")

def google(request):
    return render(request, "google.html")

def infrastructure_as_a_service(request):
    return render(request, "iaas.html")

def private_cloud(request):
    return render(request, "private_cloud.html")

def virtual_desktop_infrastructure(request):
    return render(request, "virtual_desktop.html")




