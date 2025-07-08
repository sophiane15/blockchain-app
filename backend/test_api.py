import requests

def test_backend():
    response = requests.get("https://votre-backend.onrender.com/chain")
    assert response.status_code == 200
    assert "chain" in response.json()

if __name__ == "__main__":
    test_backend()
    print("✅ Backend tests passed!")
