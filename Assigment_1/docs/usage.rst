Usage
=====

Run Grobid:

.. code-block:: bash

   docker run -t --rm -p 8070:8070 grobid/grobid:${latest_grobid_version}-crf

Process PDFs:

.. code-block:: bash

   python grobidClient.py

Generate results:

.. code-block:: bash

   python wordCloud.py
   python countFigures.py
   python extract_links.py