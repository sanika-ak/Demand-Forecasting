from setuptools import setup, find_packages

setup(
    name="demand_forecast",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "seaborn",
    ],
    entry_points={
        "console_scripts": [
            "demand-forecast=demand_forecast.main:main",
        ],
    },
)
