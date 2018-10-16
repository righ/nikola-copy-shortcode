What is this
============
This is nikola `shortcode` plugin to copy files (not document) to output.

Useful for what?
----------------
Nikola does not build not document files. (e.g. PNG, JPG)
We should put it to `images/` or `files/`.

but I wanted to put media files into the same directory that an article file put on no matter what.

This shortcode just copies files matched with specfying glob rule, into the same path in `output/`.

Requirements
============
- Nikola

  - I tested only nikola version 8.

- Python 3.4.

  - Using `pathlib` module.

Usage
=====

Setup
-----

1. Make a `plugins/` directory or the other one according to the config you specified. (e.g. `EXTRA_PLUGINS_DIRS`)
2. Put this plugin (this repository) on the plugins directory.

  .. code-block:: shell
  
    $ git clone https://github.com/righ/nikola-copy-shortcode plugins/copy_shortcode

  You don't have to do the operation so far everytime.
  It is recommended committing the plugin as yours. (it does not matter that is git submodule or not)

Description in a post
---------------------
You have to specify a src files rule (GLOB format).

You can also specify a destination path from a starting point the default directory as second argument.
(this is optional).

.. code-block:: shell

  {{% copy *.png %}}
  {{% copy *.txt ./texts/ %}

