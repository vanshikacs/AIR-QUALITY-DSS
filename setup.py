from setuptools import setup, find_packages

setup(
    name="airflow-dss",
    version="1.0.0",
    description="Air Quality Decision Support System",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "plotly>=5.17.0",
        "folium>=0.14.0",
        "streamlit-folium>=0.15.0",
        "requests>=2.31.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
    ],
)
