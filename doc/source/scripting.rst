Custom scripts
==============

As in `git <http://git-scm.com>`__, you can write custom scripts to
include them in the command spectrum of papis.

Example: Mail script
--------------------

Imagine you want to write a script to send papers to someone via the email
client ``mutt`` (you can try to do it with another mail client), you could
write the following script called ``papis-mail``:

.. code:: sh

    #! /usr/bin/env bash
    # papis-short-help: Email a paper to my friend

    folder_name=$1
    zip_name="${folder_name}.zip"

    papis -l ${PAPIS_LIB} export --folder --out ${folder_name}
    zip -r ${zip_name} ${folder_name}

    mutt -a ${zip_name}

Papis defines environment variables such as ``PAPIS_LIB`` so that external
scripts can make use of the user input.

To use the script you can put it somewhere in your ``PATH`` or alternatively
inside the ``~/.papis/scripts`` folder. If this is the case then you can run

::

    papis -h

and you will see that there is another command besides the default
called ``mail``. You will see in fact

.. code::

    positional arguments:
      command               For further information for every command, type in 'papis <command> -h'
        add                 Add a document into a given library
        .............       ..........................
        mail                Email a paper to my friend

    optional arguments:
      -h, --help            show this help message and exit
      ... .........         .... ... ...... ....... ........... .. ..... ......

where the description ``Email a paper to my friend`` is there because
we have defined the comment ``# papis-short-help: Email a paper to my friend``
in the header of the script.

Then if you type

::

    papis -l mylib mail this_paper

this will create a folder called ``this_paper`` with a selection of a
document, zip it, and send it to whoever you choose to.

