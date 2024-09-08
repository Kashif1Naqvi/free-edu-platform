import { useCounter } from '../contexts/useCounter';

const CounterControls = () => {
    const { increment, decrement } = useCounter()
    return (
        <div>
            <button onClick={increment} >increment</button>
            <button onClick={decrement} >decrement</button>
        </div>
    );
}

export default CounterControls;
