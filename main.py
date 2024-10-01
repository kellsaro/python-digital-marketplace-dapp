from algokit_utils.beta.algorand_client import(
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams
)

# client to connect to localnet
algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
print("Dispense account:", dispenser.address)

# Create algorand account
creator = algorand.account.random()
print("creator address:", creator.address)
print(algorand.account.get_information(creator.address))

algorand.send.payment(
    PayParams(
        sender=dispenser.address, 
        receiver=creator.address, 
        amount=10_000_000
    )
)

print(algorand.account.get_information(creator.address))

sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address, 
        total=1000, 
        asset_name="hackathontoken",
        unit_name="tok",
        manager=creator.address,
        clawback=creator.address,
        freeze=creator.address
    )
)

# extract the Asset ID
asset_id = sent_txn["confirmation"]["asset-index"]
print("Asset ID: ", asset_id)

receiver_acct=algorand.account.random()
print("2nd address:", receiver_acct.address)


# fund receiver_acct account
algorand.send.payment(
    PayParams(
        sender=dispenser.address, 
        receiver=receiver_acct.address, 
        amount=10_000_000
    )
)

asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=,
        receiver=,
    )
)

# start of group transaction
group_txn = algorand.new_group()

# opt in
group_txn.add_asset_opt_in(
    AssetOptInParams(
        sender=receiver_acct.address,
        asset_id=asset_id
    )
)

group_txn.add_payment(
    PayParams(
        sender=receiver_acct.address,
        receiver=creator.address,
        amount=1_000_000
    )
)

group_txn.add_asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acct.address,
        asset_id=asset_id,
        ammount=10
    )
)

# Execute txn group
group_txn.execute()

# Print the entire information from the receiver Account

# Print the amount of the asset the receiver account holds after the transactions

# Print the remaining balance of the creator account