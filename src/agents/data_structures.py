from typing import Dict, List
from uagents import Model


class UserRawData(Model):
    """
    Model for users raw data.

    Attributes:
        raw_user_data (str): The raw data.
    """
    raw_user_data: str


class PensionSchemeData(Model):
    """
    Model for pension scheme data.

    Attributes:
        raw_pension_scheme_data (str): The pension scheme data.
    """
    raw_pension_scheme_data: str


class DataForRecommendation(Model):
    """
    Model for data to be used for recommendation.

    Attributes:
        processed_user_data (Dict[str, str]): The processed user data.
        processed_scheme (str): The processed pension scheme data.
        current_year (str): The current year.
    """
    processed_user_data: Dict[str, str]
    processed_scheme: str
    current_year: int


class DataFromChainRecommendation(Model):
    """
    Model for data to be used for recommendation x years into the future.

    Attributes:
        base_input (DataForRecommendation): The base input data.
        chain_length (int): The length of the chain.
    """
    base_input: DataForRecommendation
    chain_length: int


class TextReply(Model):
    """
    Model for text reply.

    Attributes:
        text (str): The text reply.
    """
    text: str


class DictionaryReply(Model):
    """
    Model for dictionary reply.

    Attributes:
        dictionary (dict): The dictionary reply.
    """
    dictionary: Dict[str, str]


class ChainDictReply(Model):
    """
    Model for replying to a chained request.

        Attributes:
        dictionary (list): Chained list of DictionaryReply, one for each reached hop
    """
    dict_chain: List[DictionaryReply]