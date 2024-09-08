import { CounterState, CounterActionType, CounterAction } from '../types/counterTypes';


export const counterReducer = (state: CounterState, action: CounterAction) => {
    switch(action.type){
        case CounterActionType.INCREMENT:
            return {
                count: state.count + 1
            }
        case CounterActionType.DECREMENT:
            return {
                count:state.count - 1
            }
    }
}