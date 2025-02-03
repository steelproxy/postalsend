# Postal Sender Library

This is a library to send messages with the Postal server API.

## Installation

```bash
pip install postalsend
```


## Usage

```python
import postalsend
``` 

## Login

```python
postalsend.login(server, api_key)
```

## Send a message

```python
postalsend.send(from_address, to_address, subject, text)
```

## Setup push notifications

```python
postalsend.push_setup(to_address, from_address)
```

## Send a push notification

```python
postalsend.push_send(subject, text)
``` 

## Example

```python
python examples/send-mail.py
``` 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.    


