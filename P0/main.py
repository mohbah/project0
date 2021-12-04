from flask import Flask, request, jsonify

from entities.Customer import Customer
from entities.Account import Account
from service_layer.implimentation_services.account_service_impl import AccountServiceImpl
from data_access_layer.Implimentation.customer_postgres_dao import CustomerPostgresDAO
from service_layer.implimentation_services.customer_service_impl import CustomerServiceImpl
from custom_exceptions.CustomException import customexception
from data_access_layer.Implimentation.account_postgres_dao import AccountPostgresDAO
from psycopg import connect, OperationalError, Error

app: Flask = Flask(__name__)

account_dao = AccountPostgresDAO()
account_service = AccountServiceImpl(account_dao)

customer_dao = CustomerPostgresDAO()
customer_service = CustomerServiceImpl(customer_dao)


@app.post("/customer")
def create_customer_entry():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["customerid"],
            customer_data["ssn"],
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["phoneNumber"],
        )
        customer_to_return = customer_service.service_create_customer(new_customer)
        customer_as_dictionary = customer_to_return.make_customer_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json
    except customexception as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/customer")
def get_all_customers_information():
    customers_as_customers = customer_service.service_get_all_customers()
    customers_as_dictionary = []
    for customer in customers_as_customers:
        dictionary_customer = customer.make_customer_dictionary()
        customers_as_dictionary.append(dictionary_customer)
    return jsonify(customers_as_dictionary)


@app.get("/customer/<customer_id>")
def get_customer_information(customer_id: str):
    try:
        result = customer_service.service_get_customer_by_id(int(customer_id))
        result_as_dictionary = result.make_customer_dictionary()
        result_as_jason = jsonify(result_as_dictionary)
        return result_as_jason
    except AttributeError as e:
        exception_dictionary = {"message": "There is No customer with this ID"}
        exception_json = jsonify(exception_dictionary)
        return exception_json








@app.delete("/customer/<customer_id>")
def delete_customer_information(customer_id: str):
    result = customer_service.service_delete_customer_by_id(int(customer_id))
    if result:
        return "Customer with id {} was deleted successfully".format(customer_id)
    else:
        return "something went wrong: Customer with id {} was not deleted".format(customer_id)


@app.patch("/customer/<customer_id>")
def update_customer_information(customer_id: str):
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            int(customer_id),
            customer_data["ssn"],
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["phoneNumber"]
        )
        customer_service.service_update_customer(new_customer)
        return "customer updated successfully!"
    except customexception as e:

        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.post("/account")
def create_account_entry():
  try:
    account_data = request.get_json()
    new_account = Account(
        account_data["accountId"],
        account_data["ballance"],
        account_data["accountNumber"],
        account_data["customerId"]
    )
    account_to_return = account_service.service_create_account(new_account)
    account_as_dictionary = account_to_return.make_Account_dictionary()
    account_as_jason = jsonify(account_as_dictionary)
    return account_as_jason
  except (Exception, Error):
    return ("There is No Customer with this ID!")


@app.get("/account/<account_id>")
def get_account_information(account_id: str):
   try:
    result = account_service.service_get_account_information(int(account_id))
    result_as_dictionary = result.make_Account_dictionary()
    result_as_jason = jsonify(result_as_dictionary)
    return result_as_jason
   except AttributeError :
       exception_dictionary = {"message":"There is No account with this ID" }
       exception_json = jsonify(exception_dictionary)
       return exception_json


@app.get("/account")
def get_all_accounts_information():
    accounts_as_accounts = account_service.service_get_all_accounts_information()
    accounts_as_dictionary = []
    for account in accounts_as_accounts:
        dictionary_account = account.make_Account_dictionary()
        accounts_as_dictionary.append(dictionary_account)
    return jsonify(accounts_as_dictionary)


@app.delete("/account/<account_id>")
def delete_account_information(account_id: str):
    result = account_service.service_delete_account_information(int(account_id))
    if result:
        return "Account with id {} was deleted successfully".format(account_id)
    else:
        return "Something went wrong: account with id {} was not deleted".format(account_id)


@app.get("/<customer_id>")
def get_all_customer_accounts_by_id(customer_id: str):
    accounts_as_accounts = account_service.service_get_all_customer_accounts_by_id(int(customer_id))
    accounts_as_dictionary = []
    for account in accounts_as_accounts:
        dictionary_account = account.make_Account_dictionary()
        accounts_as_dictionary.append(dictionary_account)
    return jsonify(accounts_as_dictionary)


@app.post("/deposit/<account_id>:<amount>")
def deposit_into_account_by_id(account_id: int, amount: int):
    try:
         account_service.service_deposit_into_account_by_id(int(account_id), int(amount))
         return "Thanks for your deposit!"
    except UnboundLocalError:
        return "Something went wrong! Make sure you enter a valid account ID!"


@app.post("/withdrawl/<account_id>:<amount>")
def withdrawl_from_account_by_id(account_id: int, amount: int):

        result = account_service.service_withdraw_from_account_by_id(int(account_id), int(amount))
        if result:
            return "THANKS FOR YOUR BUSINESS!"
        else:
            return "WRONG ACCOUNT ID OR NOT SUFFICIENT BALANCE IN YOUR ACCOUNT!"







@app.post("/transfer/<idtowithdraw>:<idtodeposit>:<amount>")
def transfer_money_between_accounts(idtowithdraw: int, idtodeposit: int, amount: int):
    try:
         result = account_service.service_transfer_money_between_accounts_by_their_ids(int(idtowithdraw),int(idtodeposit),int(amount))
         if result:
            return "Thatnks for your Bussiness!"
         else:
             return "PLEASE  MAKE SURE YOUR ACCOUNT NUMBER IS CORRECT AND/OR YOU HAVE SUFFICIENT BALANCE IN YOUR ACCOUNT!"
    except TypeError:
                return "!"



app.run()
