import bittensor as bt
from typing import Awaitable
from app.core.wgsynapse import WebgenieTextSynapse, WebgenieImageSynapse
from app.core.solution import Solution
from app.api.v1.utils.htmls import seperate_html_css, is_valid_html

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
        wallet = bt.wallet(name="s-owner", hotkey="s-backend")
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
            timeout=300,
          )
        else:
          return None
        
        if len(response) == 0:
          bt.logging.info("No responses received")
          return None
        else:
          synapse = response[0]
          if synapse.dendrite.status_code == 200:
            html = synapse.html
            if is_valid_html(html):
              cleaned_html, css = seperate_html_css(html)
              return Solution(html=cleaned_html, css=css)
            else:
              return None
          else:
            return None
