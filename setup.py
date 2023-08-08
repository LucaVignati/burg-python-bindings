import setuptools
from pybind11.setup_helpers import Pybind11Extension, build_ext

bindings = [
    Pybind11Extension("burg_plc",
                      ["python-bindings/python_bindings.cpp"]),
    
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='burg_plc',
                 version='0.0.3',
                 author='Luca Vignati',
                 author_email='luca.vignati@vignati.net',
                 description="Python library for the BURG PLC C++ implementation by Matteo Sacchetto",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/LucaVignati/burg-python-bindings",
                 packages=setuptools.find_packages(),
                 classifiers=[
                     "Programming Language :: Python :: 3",
                 ],
                 install_requires=[
                    'pybind11',
                 ],
                 python_requires='>=3.7',
                 ext_modules=bindings,
                 cmdclass={"build_ext": build_ext}
                 )
