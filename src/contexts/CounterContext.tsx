import React, { createContext, ReactNode, useReducer } from "react";
import { CounterActionType, CounterContextType, CounterState } from "../types/counterTypes";
import { counterReducer } from "../reducers/counterReducer";

const intialCounterState: CounterState = {
    count: 0
}

// Create the context with undefined default value
export const counterContext = createContext<CounterContextType | undefined>(undefined);

// Props for the provider
interface CounterProviderProps {
    children: ReactNode;
}

// Provider component
export const CounterProvider: React.FC<CounterProviderProps> = ({ children }) => {
    const [counter, dispatch] = useReducer(counterReducer, intialCounterState)
    const increment = () => dispatch({ type: CounterActionType.INCREMENT });
    const decrement = () => dispatch({ type: CounterActionType.DECREMENT });
    return (
        <counterContext.Provider value={{ counter, increment, decrement }} >
            {children}
        </counterContext.Provider>
    )
}