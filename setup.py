from setuptools import setup

setup(
    name="django-box",
    packages=['dj_box'],
    version='0.1.0',
    author="Ross Crawford-d'Heureuse",
    license="MIT",
    author_email="ross@lawpal.com",
    url="https://github.com/rosscdh/django-box",
    description="A Django app for integrating with box webhooks",
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'django-braces',
    ]
)
