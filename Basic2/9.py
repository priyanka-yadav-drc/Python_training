import pkg_resources
installed_packages = pkg_resources.working_set
print(list(installed_packages))