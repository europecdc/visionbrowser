import asyncio
import visionbrowser

async def main():
    vb_api = visionbrowser.Api()
    token = 'YOUR_TOKEN'
    profiles = await vb_api.get_launched_profiles(token=token)
    print(profiles)

if __name__ == '__main__':
    asyncio.run(main())