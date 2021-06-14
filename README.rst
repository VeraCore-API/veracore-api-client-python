*******************
VeraCore API Client
*******************

.. image:: https://api.travis-ci.org/veracore-api/veracore-api-client-python.svg?branch=master
   :target: https://travis-ci.org/veracore-api/veracore-api-client-python

.. image:: https://readthedocs.org/projects/veracore-api-client/badge/?version=latest
   :target: http://veracore-api-client.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

The VeraCore API Client is a basic VeraCore.com REST API client built for Python 3.5, 3.6, 3.7 and 3.8.

=============

You can find out more regarding the API in the `Official VeraCore.com REST API Documentation`_

.. _Official VeraCore.com REST API Documentation: https://support.veracore.com/support/s/apiobject

The Swagger documentation can be found here: `https://{domain}.veracore.com/VeraCore/Public.Api/swagger/ui/index`
* Replace `{domain}` with your VeraCore domain name

Examples
--------------------------
Retrieving orders that are in an unprocessed state:

.. code-block:: python

    from veracore_api_client import VeraCore
    from veracore_api_client.constants import ORDER_STATUS_UNPROCESSED


    veracore = VeraCore(username='APIUsername', password='APIPassword', system_id='APISystemID', domain='VCDomain.veracore.com')
    orders = veracore.get_orders(order_status=ORDER_STATUS_UNPROCESSED)

    for order in orders:
      print('ID: %s | Status: %s | Stream: %s | Ordered By: %s | Ship To: %s' % (
         order['ID'], order['CurrentOrderStatus'], order['OrderClassification']['OrderProcessingStream'],
         order['OrderedBy']['Name'], ','.join([shipment['ShipTo']['Name'] for shipment in order['Shipments']])
      ))

Authors & License
--------------------------

This package is released under an open source GNU GPL v3 license. This package was originally created by Eli Keimig.

The latest build status can be found at `Travis CI`_

.. _Eli Keimig: https://github.com/cyclops26
.. _GitHub Repo: https://github.com/veracore-api/veracore-api-client-python
.. _Travis CI: https://travis-ci.com/veracore-api/veracore-api-client-python
