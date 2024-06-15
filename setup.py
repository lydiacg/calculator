from setuptools import setup, find_packages

VERSION = "0.0.5"
DESCRIPTION = "Calculator class"
LONG_DESCRIPTION = "A calculator class built for a project"

# Setting up
setup(
        name="calculator_lydiacg", 
        version=VERSION,
        author="Lydia Gasson",
        author_email="lydiagasson@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=["python", "first package", "calculator"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)