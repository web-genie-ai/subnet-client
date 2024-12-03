import bittensor as bt
from typing import Awaitable
from app.core.wgsynapse import WGSynapse
from app.core.task import Task

class WGSynapseService:
    def __init__(self):
        self.bt_meta = bt.metagraph(netuid=214, network="test")

    async def process_response(self, uid: int, async_generator: Awaitable):
      try:
          buffer = ""
          chunk = None
          async for chunk in async_generator:
              if isinstance(chunk, str):
                  buffer += chunk
                  print("===buffer===>", buffer)
          if chunk is not None:
              synapse = chunk
              if isinstance(synapse, WGSynapse):
                  if synapse.dendrite.status_code == 200:
                      synapse.solution.miner_uid = uid
                      return synapse.solution
              else:
                  bt.logging.error(f"Received non-200 status code: {chunk.dendrite.status_code} for uid: {uid}")
                  return None
          else:
              bt.logging.error(f"Synapse is None for uid: {uid}")
              return None
      except Exception as e:
          bt.logging.error(f"Error processing response for uid: {uid}: {e}")
          return None
    
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
        response = await dendrite(
          axons=[test_axon],
          synapse = WGSynapse(
            task=Task(query=prompt, img_data=img_data),
          ),
          timeout=50,
          deserialize=False,
          streaming=False,
        )
        
        if len(response) == 0:
          bt.logging.info("No responses received")
          return None
        else:
          return response[0].solution
