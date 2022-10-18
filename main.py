import streamlit as st
import requests

question = st.text_input("Role")

import requests

response = requests.post("https://api.ai21.com/studio/v1/experimental/j1-grande-instruct/complete",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={
        "prompt": "Classify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest: \nare there still day tickets on site today?\nClass:\nTicket availability \n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nHow do I pay for my accommodation/stay?\nClass:\nPayment options\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nare there any current Corona rules to be observed?\nClass:\nCovid\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nhow much is the entrance fee?\nClass:\nPrice\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\ndo I need tickets in advance (for infants, birthday children, free ticket holders, annual pass holders)? / Do I have to buy my ticket online? / Can I arrive spontaneously? / Can I buy my ticket on site?\nClass:\nPurchase options\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nIs the hotel dog friendly?\nClass:\nOther\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\ncan I change my ticket or cancel it free of charge?\nClass:\n Cancel conditions \n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n- Restaurant \n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nwhen can I arrive and where?\nClass:\nArrival/departure time\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nIs the pool heated? Do you provide towels in the pool?\nClass:\nOther\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nIs my voucher still valid and how and for what can I use it?\nClass:\nVoucher\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nAre there any age restrictions for the day stay/ overnight stay/ attractions?\nClass:\nAge restriction\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nAre there lactose-free/gluten-free/vegan dishes in the restaurants? Can you find menus online?\nClass:\nRestaurant menue\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant \n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nWhere can I leave my luggage until I move into the accommodation?\nClass:\nLuggage\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nWhat are the prices in the restaurants?\nClass:\nRestaurant prices\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\nHow is the towels & bed linen and the location of the cottages.\nClass:\nEquipement\n\n##\n\nClassify the requests below using the flowing classifiers:\n- Price\n- Purchase options\n- Ticket types\n- Change fee\n- Covid\n- Arrival/departure time\n- Luggage\n- Cancel conditions\n- Payment options\n- Vouchers\n- Ticket availability \n- Parking\n- Equipement \n- Restaurant menu\n- Restaurant prices\n- Age restriction\n\nIf none if these classifiers apply write Other exactly. \n\nRequest:\n" + question,
        "numResults": 1,
        "maxTokens": 25,
        "temperature": 0,
        "topKReturn": 0,
        "topP":1,
        "countPenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "frequencyPenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "presencePenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
      },
      "stopSequences":["##"]
    }
)

if response.status_code != 200:
    raise Exception(f"Completion request failed with status {response.status_code}")

answer = response.json()["completions"][0]["data"]["text"]

st.write(answer)
