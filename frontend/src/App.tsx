import React from 'react';
import './App.css';
import ExchangeRate from "./components/ExchangeRate";
import WalletConnect from "./components/WalletConnect";
import {TonConnectUIProvider} from "@tonconnect/ui-react";

function App() {
    return (
        <div className="App">
            <TonConnectUIProvider
                manifestUrl="https://gist.githubusercontent.com/skar404/3ff44643b2ba31f853201c6bb3125142/raw/a171513ee2c2e81a7ea8711e6d2b82fc52ef7738/tonconnect-manifest.json">
                <WalletConnect/>
                <ExchangeRate/>
            </TonConnectUIProvider>
        </div>
    );
}

export default App;
