import { useCounter } from '../contexts/useCounter';

const CounterDisplay = () => {
    const { counter } = useCounter()
    return (
        <div>
            {counter.count}
        </div>
    );
}

export default CounterDisplay;
