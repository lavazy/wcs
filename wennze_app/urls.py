from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("managed/", views.managed, name="managed"),
    path("cyber/", views.cyber, name="cyber"),
    path("consulting/", views.consulting, name="consulting"),
    path("cloud/", views.cloud, name="cloud"),
    path("solutions/", views.base_solutions, name="solutions"),
    # Managed IT solutions
    path("co_managed/", views.co_managed, name="co_managed"),
    path("assets_management/", views.assets_management, name="assets_management"),
    path("support/", views.support, name="support"),
    path("network_admin/", views.network_admin, name="network_admin"),
    path("server_management/", views.server_management, name="server_management"),
    # CyberSecurity solutions
    path("cyber_risk/", views.cyber_risk, name="cyber_risk"),
    path("dark_web/", views.dark_web, name="dark_web"),
    path("endpoint_solutions/", views.endpoint_solutions, name="endpoint_solutions"),
    path("incident_response/", views.incident_response, name="incident_response"),
    path("pen_testing/", views.pen_testing, name="pen_testing"),

    # IT consulting solutions
    path("business_intelligence/", views.business_intelligence, name="business_intelligence"),
    path("dev_ops/", views.dev_ops, name="dev_ops"),
    path("onshore_it_outscourcing/", views.it_outsourcing, name="it_outsourcing"),
    path("governance_risk_compliance/", views.governance_risk_compliance, name="grc"),
    path("share_point/", views.share_point, name="share_point"),
    path("staff_augmentation/", views.staff_augmentation, name="staff_augmentation"),
    path("virtual_cisco/", views.virtual_cisco, name="virtual_cisco"),
    path("virtual_chief_info_officer/", views.virtual_chief_info_officer, name="vcio"),
    path("web_development/", views.web_development, name="web_development"),

    # ===== Cloud Solutions ===== #
    path("azure/", views.azure, name="azure"),
    path("cloud_storage/", views.cloud_storage, name="cloud_storage"),
    path("google/", views.google, name="google"),
    path("infrastructure_as_a_service/", views.infrastructure_as_a_service, name="iaas"),
    path("private_cloud/", views.private_cloud, name="private_cloud"),
    path("virtual_desktop_infrastructure/", views.virtual_desktop_infrastructure, name="virtual_desktop"),
    
]