{/* 
Interface (CounterState):
   Used for defining a simple object structure 
    (the counter state with just the count property).
Type (CounterContextType):
    Used to define the context type, 
    including both the state and the increment/decrement functions, 
    as well as function signatures.
*/}


export interface CounterState {
    count: number;
}

export enum CounterActionType {
    INCREMENT= "INCREMENT",
    DECREMENT= "DECREMENT"
}

export type CounterAction = 
    | {type: CounterActionType.INCREMENT}
    | {type: CounterActionType.DECREMENT}
    
export type CounterContextType = {
    counter: CounterState;
    increment: () => void;
    decrement: () => void;
}