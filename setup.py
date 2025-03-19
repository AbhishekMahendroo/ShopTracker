from setuptools import setup, find_packages

setup(
    name="ShopSalesTracker",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pandas", "openpyxl"],
    entry_points={"console_scripts": ["shopsales=main:main"]},
    author="Your Name",
    description="A sales tracking system for small shops",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ShopSalesTracker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
