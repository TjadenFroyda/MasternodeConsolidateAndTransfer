from api.responsemodels import BuildTransactionResponseModel, SendTransactionResponseModel
from exceptions import NodeResponseException
import json
import requests as req
from .ErrorResponse import ErrorResponse


def send_transaction(
        uri: str,
        transaction: BuildTransactionResponseModel) -> None:
    """Broadcasts a signed transaction to the network.

    :param str uri: The uri.
    :param BuildTransactionResponseModel transaction: A BuildTransactionResponseModel.
    :return: None
    :raises NodeResponseException: If HTTP post request not successful.
    """
    headers = {'Accept': '*/*', 'Content-Type': 'application/json'}
    data = {'hex': transaction.hex}
    res = req.post(
        url=uri,
        data=json.dumps(data),
        headers=headers)
    if res.status_code == 200:
        print('Sending transaction.')
        response = SendTransactionResponseModel(res)
        print(response)
    else:
        error = ErrorResponse(res)
        raise NodeResponseException(message='Error sending transaction.', response=str(error.json))
