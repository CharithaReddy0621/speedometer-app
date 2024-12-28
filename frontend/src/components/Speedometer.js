import React, { useEffect, useState } from 'react';
import axios from '../services/api';
import io from 'socket.io-client';
import ReactSpeedometer from 'react-d3-speedometer';

const socket = io('http://localhost:5000'); // Backend URL

const Speedometer = () => {
    const [speed, setSpeed] = useState(0);

    useEffect(() => {
        // Fetch latest speed on mount
        axios.get('/latest')
            .then(response => setSpeed(response.data.speed))
            .catch(console.error);

        // Listen for real-time updates
        socket.on('update_speed', data => setSpeed(data.speed));

        return () => socket.disconnect();
    }, []);

    return (
        <div>
            <h1>Real-Time Speedometer</h1>
            <ReactSpeedometer maxValue={200} value={speed} />
        </div>
    );
};

export default Speedometer;
