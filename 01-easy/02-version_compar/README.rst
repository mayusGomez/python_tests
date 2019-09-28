==========
Question 
==========
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.


=========
Answer
=========

Create functionalities for manage software versions. Have the functionality 'compare_versions' that receive 
2 versions and returns whether one is greater than, equal, or less than the other. This package only allow compare version with three integer or less, separated by ".". Example: "1.0", "2.1.0", "1".


Instalation
===============
- python 3.6 installed
- clone repository: $git clone ...
- Locate to the folder: cd b_version_compar
- Create virtual environment: $virtualenv --python python3 venv
- Install requirements: $pip install -r requirements.txt
- For test, run $pytest

To execute, please generate the wheel: $python setup.py bdist_wheel and install 
with the command: $pip install versions-1.0.0-py3-none-any.whl


.. code-block:: python

    from versions import compare_versions
    compare_versions('1.2.3', '2.1.0') # "Version '1.2.3' is less than '2.1.0'"
    assert compare_versions('1', '2') # "Version '1' is less than '2'"
    compare_versions('1', '1.0.0') # "Version '1' is equal to '1.0.0'"
