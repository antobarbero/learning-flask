from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    # to include other files(static, templates) declared in the MANIFEST.in
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask'
    ],
)
