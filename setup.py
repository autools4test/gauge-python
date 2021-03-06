from distutils.core import setup

setup(
    name='getgauge',
    packages=['getgauge', 'getgauge/messages'],
    version='0.2.4',
    description='Enables Python support for Gauge',
    author='Kashish Munjal',
    author_email='kashishmunjal64@gmail.com',
    url='https://github.com/getgauge/gauge-python',
    download_url='https://github.com/getgauge/gauge-python/archive/v0.2.4.zip',
    keywords=['testing', 'gauge', 'gauge-python', 'getgauge', 'automation'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['protobuf==3.3.0', 'redBaron', 'colorama'],
)
