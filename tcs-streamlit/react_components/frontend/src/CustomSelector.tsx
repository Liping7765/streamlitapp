import { Streamlit, withStreamlitConnection } from "streamlit-component-lib"
import React from 'react';
import { Select, Value } from 'baseui/select';
import "./style.css"

function CustomSelector() {

    const [value, setValue] = React.useState<Value>([]);

    React.useEffect(() => Streamlit.setFrameHeight(230))

    return (
        <>
        <Select
            options={[
                { grade: 1, grade_value: 1 },
                { grade: 2, grade_value: 2 },
                { grade: 3, grade_value: 3 },
                { grade: 4, grade_value: 4 },
                { grade: 5, grade_value: 5 },
                
            ]}
            placeholder = "filter students by their grades here..."
            labelKey="grade"
            valueKey="grade_value"
            onChange={({ value }) => {
                setValue(value);
                Streamlit.setComponentValue(value);
            }}
            value={value}
        />

        <img 
        src= "https://miro.medium.com/proxy/1*HSisLuifMO6KbLfPOKtLow.jpeg"
        className = "center"
        alt='react_image'
        />
        </>
    );
}
export default withStreamlitConnection(CustomSelector);
