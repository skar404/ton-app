import React, {useMemo, useState} from 'react';
import {useTonConnectUI, useTonWallet, useTonAddress} from '@tonconnect/ui-react';
import {Tonstakers} from "tonstakers-sdk";


const WalletConnect: React.FC = () => {
    const address = useTonAddress();
    const wallet = useTonWallet();
    const connector = useTonConnectUI()[0]
    const [error, setError] = useState<string | null>(null);

    const tonstakers = useMemo(() => {
        return new Tonstakers({
            connector: {
                wallet: {
                    account: wallet?.account,
                },
                sendTransaction: async (transactionDetails) => {
                    await connector.sendTransaction(transactionDetails)
                },
                onStatusChange: (callback) => {
                    connector.onStatusChange(callback)
                },
            },
        })
    }, [address,])

    const stakeInput = React.useRef<HTMLInputElement>(null);
    const unStakeInput = React.useRef<HTMLInputElement>(null);

    const unStake = () => {
        tonstakers.unstake(
            unStakeInput.current?.value ? Number(unStakeInput.current?.value) : 0
        ).catch(e => {
            setError(e.message)
        })
    }

    const stake = () => {
        tonstakers.stake(stakeInput.current?.value ? Number(stakeInput.current?.value) : 0).catch(e => {
            setError(e.message)
        })
    }

    return (
        <div>
            <h1>Wallet connect </h1>
            <header>
                <span>My App with React UI</span>
                {
                    wallet ?
                        <div>
                            <h3>Address: {address}</h3>
                            {error ? <h2>Error: {error}</h2> : null}
                            <input ref={stakeInput} type="number"/>
                            <button onClick={stake}>Stake
                            </button>

                            <input ref={unStakeInput} type="number"/>
                            <button onClick={unStake}>Unstake
                            </button>

                            <button onClick={() => {
                                connector.disconnect()
                            }}>Disconnect
                            </button>
                        </div>
                        : <button onClick={() => connector.openModal()}>Connect</button>
                }
            </header>
        </div>
    );
};

export default WalletConnect;
