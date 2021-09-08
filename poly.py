from ethjsonrpc import EthJsonRpc
c = EthJsonRpc('polygon-rpc.com', 443, tls=True)


#### Issuing mMATIC / Polygon side

# 1. Request payment to address

# 2. Wait for payment to address
    # Data: amount, Cardano address (from metadata)



#### Redeeming mMATIC / Polygon side

# 1. Receive notification that mMATIC has been burned on Cardano
    # Data:

#


burn_addr = '0x000000000000000000000000000000000000dead'
print("Burn address balance:", c.eth_getBalance(burn_addr, 'latest'))
