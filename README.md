# WebGenieAI Subnet Interface

This is a interface for WebGenieAI Subnet.

## Installation
Follow these steps to install the WebGenieAI Subnet Interface:

1. Clone the repository:

```bash
git clone https://github.com/web-genie-ai/subnet-client.git
cd subnet-client
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
# On Windows:
venv\Scripts\activate

# On macOS and Linux:
source venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python main.py
```

## Usage

```bash
curl --location 'http://209.145.56.217:8000/api/v1/generate' \
--header 'Content-Type: application/json' \
--data '{
    "prompt": "Build hello world page"
}'
```
