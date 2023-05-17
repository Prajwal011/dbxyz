
from setuptools import setup,find_packages
setup(
    name='toogle_cell',
    version='0.0.1',
    description='My private package from private github repo',
    url='https://github.com/Prajwal011/toggle_cell.git',
    author='PJ',
    author_email='prajwal.aiadventures@gmail.com',
    license='unlicense',
    packages=find_packages(),
    zip_safe=False
    install_requires=[
        'openai',
        'simple_colors'
    ]

)
