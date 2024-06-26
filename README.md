## Vision Browser Python API Wrapper

<div>
  <a href="https://pypi.org/project/visionbrowser/">
    <img src="https://img.shields.io/pypi/v/visionbrowser.svg" alt="PyPI Version" />
  </a>
  <a href="https://pypi.org/project/visionbrowser/">
    <img src="https://img.shields.io/pypi/pyversions/visionbrowser.svg" alt="Python Versions" />
  </a>
  <a href="https://pypi.org/project/visionbrowser/">
    <img src="https://img.shields.io/pypi/status/visionbrowser.svg" alt="Development Status" />
  </a>
  <a href="https://pypi.org/project/visionbrowser/">
    <img src="https://img.shields.io/pypi/l/visionbrowser.svg" alt="License" />
  </a>
</div>

Asynchronous Python library for interacting with the Vision Browser API. Allows you to manage browser profiles, folders, and other entities through a convenient interface.

## Installation

```bash
pip install visionbrowser
```

## Usage example

```python
import asyncio
import visionbrowser

async def main():
    vb_api = visionbrowser.Api()
    profiles = await vb_api.get_launched_profiles(token='YOUR_API_TOKEN')
    print(profiles)

if __name__ == '__main__':
    asyncio.run(main())
```

## Available methods

We have a complete list of available functions in the original API documentation. You can view them on the website https://docs.browser.vision.

To use each method you need, you need to define its class.
Example:

```python
import visionbrowser

vb_api = visionbrowser.Api() # For API
vb_profiles = visionbrowser.Profiles() # For Profiles
vb_folders = visionbrowser.Folders() # For Folders
# And other
```
## Error handling

The library raises the following exceptions:

* `visionbrowser.exceptions.FailedConnection`: Error connecting to the API.
* `visionbrowser.exceptions.APIError`: Error returned by the Vision Browser API.

There are also warnings. They are not fully implemented, but there is an example.

```python
await visionbrowser.Api.start_profile(token=token, profile_id=profile_id, folder_id=folder_id)

# If your browser was already launched inside the Vision App, then you cannot launch it through the API, and the code will display:
# WARNING:visionbrowser.api:The port was found to be empty after the application/process returned. Most likely the profile was launched inside Vision, or some other issue occurred.
```
## Examples

See usage examples in the `examples` folder.

---

## Contributing

We will gladly welcome all comments and wishes. 😊\
If you want to contact me, please send me a private message on Github **(europecdc)**.

