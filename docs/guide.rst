==========
User guide
==========

Installation
============

You need install and register package.

.. code:: console

   pip install atsphinx-revealjs-rtd

.. code:: python

   extensions = [
       ...,  # Your extensions
       "atsphinx.revealjs_rtd",
   ]

Usage
=====

You can use it without especially settings exclude register.

.. code:: console

   sphinx-build -b reavealjs source build/revealjs

Configuration
=============

.. note:: Currently, this does not have configuration variables.
