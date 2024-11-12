from django.contrib import sitemaps
from django.urls import reverse
from company.models import Job

class CustomerSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        project_details = Job.objects.all()
        return ['home', 'contact-us', 'our-team', 'projects', 'services', 'about-us', 'quotation'] + list(project_details)

    def location(self, item):
        if isinstance(item, Job):  # Check if the item is a project instance
            return reverse('project-detail', kwargs={'slug': item.slug})
        return reverse(item)