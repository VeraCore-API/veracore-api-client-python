""" VeraCore API Client Unit Testing Constants """
import datetime


TOKEN_EXPIRATION = datetime.datetime.now() + datetime.timedelta(days=30)

LOGIN_SUCCESS_RESPONSE = {
    "UtcExpirationDate": "%s.0000000Z" % TOKEN_EXPIRATION.strftime(
        '%Y-%m-%dT%H:%M:%S'),
    "Token": "FAKE_JWT_AUTH_TOKEN_FOR_UNIT_TESTING_ONLY",
    "Error": None
}

LOGIN_FAILURE_RESPONSE = {
    "UtcExpirationDate": None,
    "Token": None,
    "Error": "Invalid Requested System"
}

GET_ORDERS_RESPONSE = {
    'Orders': [
        {
            "ID": "12345",
            "PurchaseOrder": "12345",
            "ReferenceNumber": "12345",
            "Comments": None,
            "CurrentOrderStatus": "Unprocessed",
            "OrderDates": {
                "UTCOrderDate": "2021-06-09T16:43:00",
                "ServerDateCaptured": "2021-06-09T14:02:05",
                "NeededByDate": None
            },
            "OrderClassification": {
                "CustomerCode": None,
                "Store": None,
                "Department": None,
                "Vendor": None,
                "OrderEntryView": "Default",
                "OrderProcessingStream": "HI / AK - Air Shipping-5#Ice - M-Tu",
                "ProjectID": None,
                "ProjectDescription": None,
                "CampaignID": None,
                "DistributionID": None,
                "DistributionCenter": None,
                "RushOrder": False,
                "ResponseMedia": None,
                "SourceType": None,
                "Source": None,
                "SourceDetail": None,
                "SourceDetailIssueDate": None
            },
            "OrderedBy": {
                "Name": "John Smith",
                "Company": "",
                "Title": None,
                "Address1": "123 River Street",
                "Address2": "",
                "Address3": None,
                "City": "Bakersville",
                "State": "TX",
                "PostalCode": "12345",
                "Country": "US",
                "Phone": "1234567890",
                "Fax": None,
                "Email": "example@null.com",
                "UniqueIdentifier": None,
                "TaxExemptFlag": "0",
                "TaxExemptID": None,
                "TaxExemptApprovedFlag": "0",
                "CommercialFlag": "0"
            },
            "Shipments": [
                {
                    "ShipTo": {
                        "Name": "John Smith",
                        "Company": "",
                        "Title": None,
                        "Address1": "123 River Street",
                        "Address2": "",
                        "Address3": None,
                        "City": "Bakersville",
                        "State": "TX",
                        "PostalCode": "12345",
                        "Country": "US",
                        "Phone": None,
                        "Fax": None,
                        "Email": None,
                        "UniqueIdentifier": None,
                        "TaxExemptFlag": "0",
                        "TaxExemptID": None,
                        "TaxExemptApprovedFlag": "0",
                        "CommercialFlag": "0"
                    },
                    "ShippingUnits": [
                        {
                            "ShipFrom": {
                                "Company": "",
                                "Address1": None,
                                "Address2": None,
                                "Address3": None,
                                "City": None,
                                "State": None,
                                "PostalCode": None,
                                "Country": None,
                                "Phone": None
                            },
                            "RequestedShippingOption": "Ground",
                            "RequestedFreightCarrier": "OTHER",
                            "RequestedFreightService": "2ND DAY AIR",
                            "RequestedFreightCode": "BST_G",
                            "Comments": "",
                            "SignatureRequirement": None,
                            "TotalWeight": 6.25,
                            "TotalWeightType": "lbs",
                            "PackageType": {
                                "Description": None,
                                "Weight": None,
                                "WeightType": None,
                                "Dimensions": {
                                    "Measurement": "Inches",
                                    "Length": None,
                                    "Width": None,
                                    "Height": None
                                },
                                "PackageCarrierID": None
                            },
                            "Items": [
                                {
                                    "LineNumber": 999999,
                                    "ID": "UNIT_TEST_PRODUCT",
                                    "Title": "Unit Test Product",
                                    "QuantityOrdered": 2,
                                    "Pricing": {
                                        "Price": None,
                                        "PriceType": "Each"
                                    },
                                    "Products": [
                                        {
                                            "ID": "UNIT_TEST_PRODUCT",
                                            "Description": "Unit Test Product",
                                            "Weight": 10.0000,
                                            "QuantityOrdered": 2,
                                            "WeightType": "oz",
                                            "Options": [
                                                {
                                                    "SizeCode": None,
                                                    "SizeDescription": None,
                                                    "ColorCode": None,
                                                    "ColorDescription": None
                                                }
                                            ],
                                            "Transportation": {
                                                "CountryOfOrigin": None,
                                                "TariffCode": None,
                                                "CustomsValue": None,
                                                "InsuranceValue": None,
                                                "CommodityDescription": None,
                                                "NMFCNumber": None,
                                                "FreightClass": None
                                            }
                                        }
                                    ]
                                }
                            ],
                            "FreightAccount": {
                                "ThirdPartyBillingType": "0",
                                "AccountNumber": None,
                                "Name": "",
                                "Company": None,
                                "Address1": None,
                                "Address2": None,
                                "Address3": None,
                                "City": None,
                                "State": None,
                                "PostalCode": None,
                                "Country": None,
                                "Phone": None
                            }
                        }
                    ],
                    "ReturnAddress": {
                        "Name": None,
                        "Company": "Unit Test Corp.",
                        "Address1": "123 Testing Ave.",
                        "Address2": "",
                        "Address3": "",
                        "City": "Unit",
                        "State": "TX",
                        "PostalCode": "12345",
                        "Country": "US",
                        "Phone": "123-456-7890"
                    }
                }
            ]
        }
    ]
}
