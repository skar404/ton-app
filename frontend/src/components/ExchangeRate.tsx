import React, {useEffect, useState} from 'react';
import axios from "axios";
import env from "react-dotenv";


const ExchangeRate: React.FC = () => {
    const apiUrl = env.API_URL;
    const [tonToUsdRate, setTonToUsdRate] = useState<number | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchExchangeRate = async () => {
            try {
                const response = await axios.get(`${apiUrl}exchange-rate`);
                let price_usd = response.data?.tsTON?.price_usd;

                if (!price_usd) {
                    setError('Failed to fetch the exchange rate.');
                } else {
                    setTonToUsdRate(price_usd);
                }
            } catch (err) {
                setError('Failed to reqeust the exchange rate.');
            }
        };
        fetchExchangeRate().then(r => setLoading(false));
    }, []);

    return (
        <div>

            <h1>Exchange rate</h1>
            {loading ?
                <p>Loading...</p>
                : error ?
                    <p>Error: {error}</p> :
                    <p>TON to USD: {tonToUsdRate}</p>
            }
        </div>
    );
};

export default ExchangeRate;