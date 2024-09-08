import { useContext } from "react";
import { CounterContextType } from "../types/counterTypes";
import { counterContext } from "./CounterContext";

// Custom hook to consume the CounterContext
export const useCounter = (): CounterContextType => {
    const context = useContext(counterContext)
    if(!context){
        throw new Error("useCounter must be used within a CounterProvider");
    }
    return context
}