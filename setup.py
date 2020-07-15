from setuptools import setup

setup(
    name='pretty',
    version='0.1',
    description='Package for debug prints',
    url='git@github.com:peh-empire/pretty-debug.git',
    author='Tobias Locker',
    author_email='tobias@tobiaslocker.de',
    license='unlicensed',
    packages=['pretty'],
    scripts=[],
    install_requires=['pandas'],
    zip_safe=False,
    include_package_data=True
)
