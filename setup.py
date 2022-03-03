from setuptools import setup, find_packages

setup(
    name="bullseye-py",
    version="1.0.0",
    author="BullseyeMonitors",
    author_email="<support@bullseye.pw>",
    description=" a py library for connecting to the bullseye monitor web socket. ",
    long_description_content_type="text/markdown",
    long_description="",
    packages=find_packages(),
    install_requires=['websocket-client'],
    keywords=['python', 'monitor', 'bullseye', 'bullseyemonitors'],
)