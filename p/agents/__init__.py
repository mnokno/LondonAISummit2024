from user_input_agent import USER_INPUT_AGENT_ADDRESS
from pension_scheme_agent import PENSION_SCHEME_ADDRESS
from recommendation_agent import RECOMMENDATION_AGENT_ADDRESS

user_input_agent.run()
pension_scheme_agent.run()
recommendation_agent.run()

__all__ = ["USER_INPUT_AGENT_ADDRESS", "PENSION_SCHEME_ADDRESS", "RECOMMENDATION_AGENT_ADDRESS"]