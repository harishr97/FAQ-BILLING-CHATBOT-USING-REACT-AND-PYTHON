#!/usr/bin/env python3
import logging
import time
import sys
import psycopg2
from flask import Flask, request, jsonify, json
from flask_cors import CORS  # Added CORS import
from psycopg2 import OperationalError, errorcodes, errors

DB_NAME = "chatbot"
DB_USER = "postgres"
DB_PASSWORD = "Welcome@123"
DB_HOST = "54.166.207.117"
DB_PORT = "5432"

app = Flask(__name__)
CORS(app, resources={r"/chat/billing/*": {"origins": "*"}})  # Added CORS configuration

currentTime = time.localtime()
logFile = time.strftime("cnapp_py.%Y-%m-%d.log", currentTime)

logging.basicConfig(filename = logFile, level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info("Current Time: %s" % str(currentTime))

@app.route("/chat/billing/<secretID>/<mon>/<service>")
def get_user_details(secretID, mon, service):
    logger.info("In the get user details method:")
    logger.info("User Details received: %s,%s,%s" % (secretID,mon,service))
	
	try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        logger.info("Database connected successfully")
        curr = conn.cursor()
        curr.execute("select user_name, used_service, amount, address, base_charge, additional_charge, taxes, year, next_bill_cycle, autopay_date, month from public.billing_t where secret_id='%s' and  month='%s' and used_service='%s';" % (secretID,mon,service))
        rows = curr.fetchall()
        if rows:
            name = str(rows[0][0])
            service = str(rows[0][1])
            amo = str(rows[0][2])
            add = str(rows[0][3])
            baseC = str(rows[0][4])
            addC = str(rows[0][5])
            tax = str(rows[0][6])
            yea = str(rows[0][7])
            nextB = str(rows[0][8])
            auto = str(rows[0][9])
            mon = str(rows[0][10])
            logger.info("Amount: %s" % amo)
            logger.info("Name: %s" % name)
            logger.info("Service: %s" % service)
            logger.info("Address: %s" % add)
            logger.info("Base charge: %s" % baseC)
            logger.info("Additional charge: %s" % addC)
            logger.info("Tax: %s" % tax)
            logger.info("Year: %s" % yea)
            logger.info("Next Bill cycle: %s" % nextB)
            logger.info("AutoPay: %s" % auto)
			logger.info("Month: %s" % mon)
            data = {'Name':name,'Service':service,'Amount':amo,'Address':add,'BaseCharge':baseC,'AdditionalCharge':addC,'Tax':tax,'Year':yea,'NextBill':nextB,'AutoPay':auto,'Month':mon}
            return jsonify(data)
    except OperationalError as e:
        logger.info("Connection failure")
        logger.info(e.pgcode)

if __name__ == '__main__':
    app.run(debug=True)