from setuptools import setup, find_packages


with open('requirements.txt') as req_txt:
    required = [line for line in req_txt.read().splitlines() if line]

try:
    # noinspection PyUnresolvedReferences
    import pypandoc
    # noinspection PyUnresolvedReferences
    from os import path
    here = path.abspath(path.dirname(__file__))
    long_description = pypandoc.convert(path.join(here, 'README.md'), 'rst'),
except RuntimeError:
    long_description = ""
except ImportError:
    long_description = ""

setup(
    name='scs_analysis',
    version='0.1.3',
    description='Information management and analysis tools for South Coast Science data consumers.',
    author='South Coast Science',
    author_email='contact@southcoastscience.com',
    url='https://github.com/south-coast-science/scs_analysis',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    scripts=[
        'src/scs_analysis/aws_api_auth.py',
        'src/scs_analysis/aws_mqtt_client.py',
        'src/scs_analysis/aws_mqtt_control.py',
        'src/scs_analysis/aws_topic_history.py',
        'src/scs_analysis/aws_topic_publisher.py',
        'src/scs_analysis/csv_reader.py',
        'src/scs_analysis/csv_writer.py',
        'src/scs_analysis/histo_chart.py',
        'src/scs_analysis/localised_datetime.py',
        'src/scs_analysis/multi_chart.py',
        'src/scs_analysis/node.py',
        'src/scs_analysis/osio_api_auth.py',
        'src/scs_analysis/osio_mqtt_client.py',
        'src/scs_analysis/osio_mqtt_control.py',
        'src/scs_analysis/osio_topic_history.py',
        'src/scs_analysis/osio_topic_publisher.py',
        'src/scs_analysis/sample_average.py',
        'src/scs_analysis/sample_conv.py',
        'src/scs_analysis/sample_error.py',
        'src/scs_analysis/sample_interval.py',
        'src/scs_analysis/sample_max.py',
        'src/scs_analysis/sample_midpoint.py',
        'src/scs_analysis/sample_min.py',
        'src/scs_analysis/sample_regression.py',
        'src/scs_analysis/single_chart.py',
        'src/scs_analysis/socket_receiver.py',
        'src/scs_analysis/uds_receiver.py',
    ],
    install_requires=required,
    platforms=['any'],
    python_requires=">=3.3",
    extras_require={
        'dev': [
            'pypandoc'
        ]
    }
)
