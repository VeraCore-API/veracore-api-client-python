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