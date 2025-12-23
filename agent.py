from typing import TypedDict, Optional
from langgraph.graph import StateGraph
from tools import check_eligibility, save_application

class AgentState(TypedDict):
    name: Optional[str]
    age: Optional[int]
    income: Optional[int]
    scheme: Optional[str]
    result: Optional[str]

def planner(state: AgentState):
    if state.get("age") is None:
        return "ASK_AGE"
    if state.get("income") is None:
        return "ASK_INCOME"
    return "CHECK_ELIGIBILITY"

def executor(state: AgentState):
    scheme = check_eligibility(state)
    if scheme:
        state["scheme"] = scheme
        save_application(state, scheme)
        state["result"] = "ELIGIBLE"
    else:
        state["result"] = "NOT_ELIGIBLE"
    return state

def build_agent():
    graph = StateGraph(AgentState)
    graph.add_node("planner", planner)
    graph.add_node("executor", executor)
    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    return graph.compile()
