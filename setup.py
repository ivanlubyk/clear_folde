from setuptools import setup,find_namespace_packages


setup(name='clean_folder',
      version='0.0.3',
      author='ivan_lubyk',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={"console_scripts":['clean-folder = sort_con.sorti:clear_dir']})