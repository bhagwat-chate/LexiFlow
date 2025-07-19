from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="document_portal",
    version="1.0.0",
    author="Bhagwat Chate",
    author_email="bhagwatsteelnerve@gmail.com",
    description="A full-stack RAG-based document intelligence platform with chat and comparison features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhagwat-chate/document_portal/tree/release/1.0/dev/bhagwat",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10"
)
