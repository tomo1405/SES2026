python
import rsa
import urllib.request
from hashlib import sha256
import pytest

def task_func(url):
    try:
        (pub_key, priv_key) = rsa.newkeys(512)

        response = urllib.request.urlopen(url)
        content = response.read()
        hash_value = sha256(content).digest()
        
        signed_hash = rsa.sign(hash_value, priv_key, 'SHA-256').hex()

        return pub_key, signed_hash, hash_value
    except urllib.error.HTTPError as e:
        raise ValueError(f"Server returned an HTTP error: {e.code} {e.reason}") from e
    except urllib.error.URLError as e:
        raise urllib.error.URLError(f"Failed to reach the server. URL might be invalid: {e}") from e
    except rsa.pkcs1.VerificationError as e:
        raise rsa.pkcs1.VerificationError(f"Failed to sign the hash: {e}") from e

def test_task_func():
    # Test case 1: Valid URL
    pub_key, signed_hash, hash_value = task_func('https://www.google.com')
    assert isinstance(pub_key, rsa.PublicKey)
    assert isinstance(signed_hash, str)
    assert isinstance(hash_value, bytes)

    # Test case 2: Invalid URL
    with pytest.raises(urllib.error.URLError):
        task_func('https://www.google.com/invalid')

    # Test case 3: Server error
    with pytest.raises(ValueError):
        task_func('https://httpstat.us/500')

    # Test case 4: Invalid signature
    with pytest.raises(rsa.pkcs1.VerificationError):
        task_func('https://www.google.com')