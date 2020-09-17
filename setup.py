from setuptools import setup

# Open README when Executing Program
def readme():
    with open('README.txt') as r:
        return r.read()

setuptools.setup(
      name='disk_space_checker',
      version='1.0',
      scripts=['disk_space_checker/calculate_partition_status.py','disk_space_checker/calculate_partition_thresholds.py','disk_space_checker/check_arguments.py','disk_space_checker/find_triggered_partitions.py','disk_space_checker/output_connectwise_results.py','disk_space_checker/output_console_messages.py','disk_space_checker/summarize_results.py'],
      description='Calculates disk space status on each partition to be critical / warning based on various calculations / thresholds',
      long_description=readme(), # Auto add the README to the long description attribute
      author='KM', 
      author_email='kyle@skycomp.ca',
      packages=setuptools.find_packages(), 
      include_package_data=True,
      zip_safe=False,	

      classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: Windows",
      ],  

)