# How to run circuits on quantum devices

This is a set of short tutorial notenooks to help you get started with running circuits on quantum devices. Covered are:

## Contents

### Preliminaries

- [Basic pytket usage](tutorials/1.%20pytket_tutorial.ipynb)
- [Basic Myqos usage](tutorials/2.%20myqos_tutorial.ipynb)
- [Evaluating with discopy](tutorials/3.%20discopy_tutorial.ipynb)

### Backend specifics

IBM

- [IBM introduction](tutorials/4.%20ibmq_explained.ipynb)
- [IBM usage](tutorials/5.%20ibmq_tutorial.ipynb)

Quantinuum

- [Quantinuum introduction](tutorials/6.%20quantinuum_explained.ipynb)
- [Quantinuum usage](tutorials/7.%20quantinuum_tutorial.ipynb)

### Advanced usage

- [Qermit](tutorials/8.%20qermit_tutorial.ipynb)

All of these packages and tools have their own documentation in addition to these tutorials, and these are all more detailed than what is here. The intention here is to have a minimal set of examples all in once place to help you get started with the basics.

Sources of more information for all these packages can be found at the start of each tutorial notebook.

Tp get started, `git clone` the repo to a location of your choice. The tutorial notebooks are numbered in an order that might be helpful, but should be relatively self-contained.

All the requirements should be in the `requirements.txt` file, so you should be able to install them with `pip install -r requirements.txt`. Make sure to use a virtual environment: `python -m venv venv_name`, then `source venv_name/bin/activate`.
