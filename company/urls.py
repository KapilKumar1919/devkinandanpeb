from django.urls import path
from company.views import (
    HomePageView, ContactPageView, ThankYouPageView, 
    OurTeamPageView, ProjectsPageView, ServicePageView,
    AboutUsPageView, ProjectDetailPageView, QuotationPageView
    )
from django.contrib.sitemaps.views import sitemap
from company.sitemaps import CustomerSitemap

sitemaps = {
    'customer': CustomerSitemap,
}

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact-us/', ContactPageView.as_view(), name='contact-us'),
    path('quotation/', QuotationPageView.as_view(), name='quotation'),
    path('our-team/', OurTeamPageView.as_view(), name='our-team'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('project/<slug:slug>/', ProjectDetailPageView.as_view(), name='project-detail'),
    path('services/', ServicePageView.as_view(), name='services'),
    path('about-us/', AboutUsPageView.as_view(), name='about-us'),
    path('thank-you/', ThankYouPageView.as_view(), name='thank-you'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
