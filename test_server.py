import requests

print(
    requests.post(
        "http://127.0.0.1:8000",
        json={
            "from_email": "ymarvintan@gmail.com",
            "content": "We are thrilled to unveil QuantumScan, the latest breakthrough from NexusTech. This cutting-edge solution revolutionizes data security with its advanced encryption capabilities. Explore a new realm of protection with QuantumScan today!"
            
        }
    ).json()
)