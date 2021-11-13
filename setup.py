from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'gcsfs==2021.11.0',
    'pandas==1.3.4',
    'scikit-learn==0.22',
    'google-cloud-storage==1.42.3',
    's3fs',
    'pygeohash',
    'category_encoders',
    'termcolor',
    'mlflow',
    'xgboost==0.90',
    'memoized_property',
    'psutil']

setup(
    name='TaxiFareModel',
    version='1.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Taxi Fare Prediction Pipeline'
)
