from setuptools import setup

setup(
    name='pretty_logging',
    version='0.1',
    description='Package for debug prints',
    url='git@github.com:peh-empire/pretty-debug.git',
    author='Tobias Locker',
    author_email='tobias@tobiaslocker.de',
    license='unlicensed',
    packages=['pretty_logging'],
    scripts=[],
    install_requires=['pandas'],
    zip_safe=False,
    include_package_data=True
)
