import os
import streamlit.components.v1 as components

from typing import Tuple


# Now the React interface only accepts an array of 1 or 2 elements.
_component_func = components.declare_component(
    "custom_selector",
    url="http://3.133.104.15:3000",
)


# Edit arguments sent and result received from React component, so the initial input is converted to an array and returned value extracted from the component
def st_custom_selector() -> int:
    component_value = _component_func()
    if not component_value:
        return {"grade": 0}
    else:
        return component_value[0]

