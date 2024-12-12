import bittensor as bt
from typing import Awaitable
from app.core.wgsynapse import WebgenieTextSynapse, WebgenieImageSynapse

class WGSynapseService:
    def __init__(self):
        self.bt_meta = bt.metagraph(netuid=214, network="test")

    async def generate(self, prompt: str, img_data: str):
        vali_ip_list = []
        vali_list = []
        for i in range(len(self.bt_meta.S)):
          if self.bt_meta.S[i] >= 10:
            vali_list.append(i)
            vali_ip_list.append(self.bt_meta.addresses[i])

        print("=== vali_list ===>", vali_list)
        print("=== vali_ip_list ===>", vali_ip_list)

        test_axon = self.bt_meta.axons[2]
        # test_axon_miner = self.bt_meta.axons[1]
        wallet = bt.wallet(name="s-owner", hotkey="s-owner-hval1")
        dendrite = bt.dendrite(wallet=wallet)
        if prompt is not None and prompt != "":
          response = await dendrite(
            axons=[test_axon],
            synapse = WebgenieTextSynapse(
              prompt=prompt,
            ),
            timeout=300,
          )
        elif img_data is not None and img_data != "":
          response = await dendrite(
            axons=[test_axon],
            synapse = WebgenieImageSynapse(
              base64_image=img_data,
            ),
            timeout=50,
          )
        else:
          raise ValueError("No prompt or image data provided")
        
        if len(response) == 0:
          bt.logging.info("No responses received")
          return None
        else:
          return response[0].solution
